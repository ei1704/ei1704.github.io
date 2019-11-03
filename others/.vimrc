set encoding=euc-jp 
set virtualedit=onemore
set fileencoding=euc-jp
set number "行番号"
set ruler "カーソルの位置
syntax on
colorscheme molokai
let g:molokai_original=1
let g:rehash256=1
set t_Co=256
set showmatch
set matchtime=1
filetype plugin indent on
set tabstop=2
"↓smartindentで増減する幅
set shiftwidth=2
"↓前の行の構文によって次の行のインデントを増減する
set smartindent
"↓前の行のインデントを継続
set autoindent
"↓タブ入力を複数の空白入力に置き換える
set expandtab
set backspace=indent,eol,start "バックスペースを有効化
"↓コメントの色"
"hi Comment ctermfg=lightcyan   
set mouse=a "ネズミ操作ON
set ttymouse=xterm2
hi StatusLine ctermfg=black ctermbg=lightgreen
set cursorline "カーソルがいる行に下線を表示
set cursorcolumn "カーソル列
set whichwrap=b,s,h,l,<,>,[,] "矢印で行またぎ
"↓カーソル行の色
"highlight CursorLine ctermbg=darkgray
"↓かぁそるれつのいろ
"highlight cursorcolumn ctermbg=darkgray 
set nobackup "バックアップ作成阻止"
set noswapfile
set wildmode=list:longest "コマンドラインとか補完しちゃう"
"↓c++のてんぷれぇと
autocmd BufNewFile *.cpp 0r $HOME/.vim/.cpp.txt 
set laststatus=2 "すてぇたすばぁのはば
"set cmdheight=3
"↓背景色に合わせる
"set background=dark"↓行番号の色
highlight LineNr ctermfg=darkgray 
set numberwidth=3
nnoremap Y y$
" ファイル名表示
set statusline=%F
" 変更チェック表示
set statusline+=%m
" 読み込み専用かどうか表示
set statusline+=%r
" ヘルプページなら[HELP]と表示
set statusline+=%h
" プレビューウインドウなら[Prevew]と表示
set statusline+=%w
" これ以降は右寄せ表示
set statusline+=%=
"set statusline+=[†VSCode†]
" file encoding
"set statusline+=[ENC=]
set statusline+=[C=%c%V] " 何列目にカーソルがあるか - 画面上の何列目にかぁそるがあるか
" 現在行数/全行数
set statusline+=[L=%l/%L]
"卍卍卍
set statusline+=[使用中のエディタはemacsです]
set statusline+=[安全第一]
hi StatusLine ctermfg=black ctermbg=gray
set hidden
"ぜんかくすぺぇすひょうじ
hi DoubleByteSpace term=underline ctermbg=green
match DoubleByteSpace /　/
"ふかしもじのひょうじ
"set list
"ほかん
"set listchars=tab:>>,trail:-,nbsp:%,eol:$,extends:>,precedes:<
"------------------------------------------------------"
"きぃまっぴんぐ
"じゅうじそうさ
nnoremap w <Up>
nnoremap s <Down>
nnoremap a <Left>
nnoremap d <Right>
inoremap <C-w> <Up>
inoremap <C-s> <Down>
inoremap <C-a> <Left>
inoremap <C-d> <Right>
vnoremap <C-w> <Up>
vnoremap <C-s> <Down>
vnoremap <C-a> <Left>
vnoremap <C-d> <Right>
"いんさぁともぉど
inoremap <C-@> <Esc>
inoremap <C-j> <BS>
inoremap <C-l> <CR>
"inoremap ( ()<LEFT>
"inoremap [ []<LEFT>
"inoremap { {}<Left>
"inoremap {<Enter> {}<Left><CR><BS><BS>
"そのた  
nnoremap e $
nnoremap q ^
nnoremap r gg
nnoremap f <S-g>
"ぜんせんたく
nnoremap z gg<S-v><S-g> 
"こぴぃ
nmap c gg<S-v><S-g>"+y
"いんでんとちょうせい
nmap x gg<S-v><S-g>=
"python専用仕様
autocmd FileType python setl autoindent
autocmd FileType python setl smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class
autocmd FileType python setl tabstop=8 expandtab shiftwidth=4 softtabstop=4
