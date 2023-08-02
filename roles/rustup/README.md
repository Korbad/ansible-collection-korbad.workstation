# Rust Development


https://stackoverflow.com/questions/46885292/how-to-launch-a-rust-application-from-visual-studio-code


Using the integrated terminal
Run the following command in the integrated terminal:

cargo run
TLDR:
Install rust-analyzer and Native debugger based on LLDB extensions, then use the Run menu (then see the terminal for the result/output):

You may install these extensions using the terminal commands (and then restart the vscode):

# apt install musl lldb libssl-dev
code --install-extension vadimcn.vscode-lldb
code --install-extension rust-lang.rust-analyzer
code --install-extension bungcip.better-toml