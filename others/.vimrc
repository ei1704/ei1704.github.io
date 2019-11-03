set encoding=euc-jp 
set virtualedit=onemore
set fileencoding=euc-jp
set number "���ֹ�"
set ruler "��������ΰ���
syntax on
colorscheme molokai
let g:molokai_original=1
let g:rehash256=1
set t_Co=256
set showmatch
set matchtime=1
filetype plugin indent on
set tabstop=2
"��smartindent������������
set shiftwidth=2
"�����ιԤι�ʸ�ˤ�äƼ��ιԤΥ���ǥ�Ȥ���������
set smartindent
"�����ιԤΥ���ǥ�Ȥ��³
set autoindent
"���������Ϥ�ʣ���ζ������Ϥ��֤�������
set expandtab
set backspace=indent,eol,start "�Хå����ڡ�����ͭ����
"�������Ȥο�"
"hi Comment ctermfg=lightcyan   
set mouse=a "�ͥ������ON
set ttymouse=xterm2
hi StatusLine ctermfg=black ctermbg=lightgreen
set cursorline "�������뤬����Ԥ˲�����ɽ��
set cursorcolumn "����������
set whichwrap=b,s,h,l,<,>,[,] "����ǹԤޤ���
"����������Ԥο�
"highlight CursorLine ctermbg=darkgray
"�����������ĤΤ���
"highlight cursorcolumn ctermbg=darkgray 
set nobackup "�Хå����å׺����˻�"
set noswapfile
set wildmode=list:longest "���ޥ�ɥ饤��Ȥ��䴰�����㤦"
"��c++�ΤƤ�פ줧��
autocmd BufNewFile *.cpp 0r $HOME/.vim/.cpp.txt 
set laststatus=2 "���Ƥ������Ф��ΤϤ�
"set cmdheight=3
"���طʿ��˹�碌��
"set background=dark"�����ֹ�ο�
highlight LineNr ctermfg=darkgray 
set numberwidth=3
nnoremap Y y$
" �ե�����̾ɽ��
set statusline=%F
" �ѹ������å�ɽ��
set statusline+=%m
" �ɤ߹������Ѥ��ɤ���ɽ��
set statusline+=%r
" �إ�ץڡ����ʤ�[HELP]��ɽ��
set statusline+=%h
" �ץ�ӥ塼������ɥ��ʤ�[Prevew]��ɽ��
set statusline+=%w
" ����ʹߤϱ���ɽ��
set statusline+=%=
"set statusline+=[��VSCode��]
" file encoding
"set statusline+=[ENC=]
set statusline+=[C=%c%V] " �����ܤ˥������뤬���뤫 - ���̾�β����ܤˤ������뤬���뤫
" ���߹Կ�/���Կ�
set statusline+=[L=%l/%L]
"������
set statusline+=[������Υ��ǥ�����emacs�Ǥ�]
set statusline+=[�������]
hi StatusLine ctermfg=black ctermbg=gray
set hidden
"���󤫤����ڤ����Ҥ礦��
hi DoubleByteSpace term=underline ctermbg=green
match DoubleByteSpace /��/
"�դ����⤸�ΤҤ礦��
"set list
"�ۤ���
"set listchars=tab:>>,trail:-,nbsp:%,eol:$,extends:>,precedes:<
"------------------------------------------------------"
"�����ޤäԤ�
"���夦��������
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
"���󤵤��Ȥ⤩��
inoremap <C-@> <Esc>
inoremap <C-j> <BS>
inoremap <C-l> <CR>
"inoremap ( ()<LEFT>
"inoremap [ []<LEFT>
"inoremap { {}<Left>
"inoremap {<Enter> {}<Left><CR><BS><BS>
"���Τ�  
nnoremap e $
nnoremap q ^
nnoremap r gg
nnoremap f <S-g>
"���󤻤󤿤�
nnoremap z gg<S-v><S-g> 
"���Ԥ�
nmap c gg<S-v><S-g>"+y
"����Ǥ�Ȥ��礦����
nmap x gg<S-v><S-g>=
"python���ѻ���
autocmd FileType python setl autoindent
autocmd FileType python setl smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class
autocmd FileType python setl tabstop=8 expandtab shiftwidth=4 softtabstop=4
