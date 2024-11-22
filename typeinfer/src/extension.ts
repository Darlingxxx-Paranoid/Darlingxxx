import * as vscode from 'vscode';
import * as path from 'path';
import * as cp from 'child_process';
import * as fs from 'fs';

// 添加全局缓存对象
let typeCache: { [key: string]: { [key: string]: string } } = {};

export function activate(context: vscode.ExtensionContext) {
	console.log('Extension "typeinfer" is activating...');

	// 添加类型推断命令
	let inferTypes = vscode.commands.registerCommand('typeinfer.inferTypes', async () => {
		const editor = vscode.window.activeTextEditor;
		if (!editor) {
			vscode.window.showWarningMessage('No active editor!');
			return;
		}

		if (editor.document.languageId !== 'python') {
			vscode.window.showWarningMessage('Not a Python file!');
			return;
		}

		// 显示进度提示
		await vscode.window.withProgress({
			location: vscode.ProgressLocation.Notification,
			title: "TypeInfer",
			cancellable: false
		}, async (progress) => {
			progress.report({ message: "Inferring types..." });

			try {
				await editor.document.save();
				const filePath = editor.document.uri.fsPath;

				const pythonPath = 'python';
				const InferPath = path.join(context.extensionPath, 'Infer.py');
				
				const result = await new Promise<string>((resolve, reject) => {
					cp.exec(
						`${pythonPath} "${InferPath}" "${filePath}"`,
						(error, stdout, stderr) => {
							if (error) {
								reject(error);
								return;
							}
							if (stderr) {
								reject(new Error(stderr));
								return;
							}
							resolve(stdout);
						}
					);
				});

				// 更新缓存
				try {
					const typeInfo = JSON.parse(result);
					typeCache[filePath] = typeInfo;
					
					// 创建新文档显示结果
					const resultDoc = await vscode.workspace.openTextDocument({
						content: result,
						language: 'json'
					});
					
					await vscode.window.showTextDocument(resultDoc, {
						viewColumn: vscode.ViewColumn.Beside
					});

					vscode.window.showInformationMessage('Type inference completed and cached!');
				} catch (e) {
					vscode.window.showErrorMessage('Failed to parse type inference results');
				}

			} catch (error) {
				vscode.window.showErrorMessage(`Error: ${error instanceof Error ? error.message : String(error)}`);
			}
		});
	});

	// 添加变量类型推断命令
	let inferSelectedVariable = vscode.commands.registerCommand('typeinfer.inferSelectedVariable', async () => {
		const editor = vscode.window.activeTextEditor;
		if (!editor) {
			vscode.window.showWarningMessage('No active editor!');
			return;
		}

		const selection = editor.selection;
		const selectedText = editor.document.getText(selection);
		if (!selectedText) {
			vscode.window.showWarningMessage('No text selected!');
			return;
		}

		const filePath = editor.document.uri.fsPath;
		
		// 检查缓存中是否有该文件的类型信息
		if (typeCache[filePath] && typeCache[filePath][selectedText]) {
			// 如果缓存中有结果，直接使用缓存
			const varType = typeCache[filePath][selectedText];
			vscode.window.showInformationMessage(
				`Variable "${selectedText}" is of type: ${varType} (from cache)`
			);
			return;
		}

		// 如果缓存中没有，先运行整个文件的类型推断
		try {
			await editor.document.save();
			const pythonPath = 'python';
			const InferPath = path.join(context.extensionPath, 'Infer.py');
			
			const result = await new Promise<string>((resolve, reject) => {
				cp.exec(
					`${pythonPath} "${InferPath}" "${filePath}"`,
					(error, stdout, stderr) => {
						if (error) {
							reject(error);
							return;
						}
						if (stderr) {
							reject(new Error(stderr));
							return;
						}
						resolve(stdout);
					}
				);
			});

			// 更新缓存并查找选中变量的类型
			try {
				const typeInfo = JSON.parse(result);
				typeCache[filePath] = typeInfo;
				
				// 检查推断结果中是否包含选中的变量
				if (typeInfo[selectedText]) {
					vscode.window.showInformationMessage(
						`Variable "${selectedText}" is of type: ${typeInfo[selectedText]}`
					);
				} else {
					vscode.window.showWarningMessage(
						`Could not infer type for variable "${selectedText}"`
					);
				}
			} catch (e) {
				vscode.window.showErrorMessage('Failed to parse type inference results');
			}

		} catch (error) {
			vscode.window.showErrorMessage(
				`Error inferring type: ${error instanceof Error ? error.message : String(error)}`
			);
		}
	});

	// 注册命令
	context.subscriptions.push(inferTypes);
	context.subscriptions.push(inferSelectedVariable);

	console.log('Extension "typeinfer" is now fully activated!');
}

export function deactivate() {}
