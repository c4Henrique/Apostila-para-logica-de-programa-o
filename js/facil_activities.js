document.addEventListener('DOMContentLoaded', () => {
    // Funcionalidade para mostrar/esconder solução
    const solutionButtons = document.querySelectorAll('.solution-button');
    solutionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const solutionId = button.dataset.targetId;
            const solutionContent = document.getElementById(solutionId);
            
            if (solutionContent.style.display === 'none') {
                solutionContent.style.display = 'block';
                button.textContent = 'Ocultar Solução';
            } else {
                solutionContent.style.display = 'none';
                button.textContent = 'Solução';
            }
        });
    });

    // Funcionalidade para copiar código
    const copyButtons = document.querySelectorAll('.copy-button');
    copyButtons.forEach(button => {
        button.addEventListener('click', async () => {
            const codeId = button.dataset.targetId;
            const codeBlock = document.getElementById(codeId);

            if (codeBlock) {
                try {
                    // Use Clipboard API for modern browsers
                    await navigator.clipboard.writeText(codeBlock.textContent);
                    button.textContent = 'Copiado!';
                    setTimeout(() => {
                        button.textContent = 'Copiar';
                    }, 2000);
                } catch (err) {
                    // Fallback for older browsers or if Clipboard API is not available
                    console.error('Erro ao copiar texto: ', err);
                    const textarea = document.createElement('textarea');
                    textarea.value = codeBlock.textContent;
                    document.body.appendChild(textarea);
                    textarea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textarea);

                    button.textContent = 'Copiado!';
                    setTimeout(() => {
                        button.textContent = 'Copiar';
                    }, 2000);
                }
            }
        });
    });
}); 