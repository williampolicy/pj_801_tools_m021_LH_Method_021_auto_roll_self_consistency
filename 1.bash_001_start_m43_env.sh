# conda env
echo "conda env "
conda deactivate


conda activate /home/kangxiaowen/code_lh_server/code_lh_pj_ai/envs/pj_51_lighthope_m43_env

echo "export - cmd line - proect your eyes. by xiaowen kang. 2025. 82"
export PS1='\[\e[38;5;110m\]${CONDA_DEFAULT_ENV:+(${CONDA_DEFAULT_ENV##*/}) }\[\e[38;5;251m\]\W \[\e[38;5;110m\]❯\[\e[0m\] '
