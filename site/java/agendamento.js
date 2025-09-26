const urlAgendamento = 'http://127.0.0.1:5000/barbearia/agendamento';


async function criarAgendamento(event) {
    event.preventDefault(); 

    const cliente_id = localStorage.getItem('user_id'); 
    const profissional = document.getElementById('barbeiro').value;
    const servico = document.getElementById('servico').value;
    const data = document.getElementById('data').value;
    const hora = document.getElementById('hora').value;

    if (!profissional || !servico || !data || !hora) {
        alert("Preencha todos os campos do agendamento.");
        return;
    }

   
    const token = localStorage.getItem('token');
    if (!token) {
        alert("Você precisa estar logado para agendar.");
        return;
    }

    try {
        const response = await fetch(urlAgendamento, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` 
            },
            body: JSON.stringify({ cliente_id, profissional, servico, data, hora })
        });

        const dataResp = await response.json();

        if (response.ok) {
            alert("Agendamento realizado com sucesso!");
            document.querySelector('.form-agendamento').reset();

            window.location.href = '../html/home_perfil.html';
        } else {
            alert(dataResp.erro || "Erro ao criar agendamento. Tente novamente.");
        }

    } catch (error) {
        console.error("Erro ao conectar com a API:", error);
        alert("Erro no servidor. Tente novamente mais tarde.");
    }
}

document.querySelector('.form-agendamento').addEventListener('submit', criarAgendamento);
