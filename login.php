<?php 
//Define os dados de login ( Futuramente será via DB)

$usuario_correto = "admin";
$senha_correta = "123456";

// Dados do formulário

$usuario = $_POST['username'] ?? '';
$senha = $_POST['password'] ?? '';

// Verifica se estão corretos

if($usuario === $usuario_correto && $senha === $senha_correta) {
    header("Location: index.html");
    exit;
} else {
    // Redireciona de volta com erro
    header("Location: login.html?error=1");
    exit;
}
?>