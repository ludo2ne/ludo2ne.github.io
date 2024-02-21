def process_pgn(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Remplace les " par `"`
    lines = [line.replace('"', '`"`') for line in lines]

    # Supprime les lignes vides
    lines = [line for line in lines if line.strip()]

    with open(output_file, 'w') as f:
        f.write(''.join(lines))


if __name__ == "__main__":
    input_file_path = "docs/hobbies/chess-games.pgn"
    output_file = "docs/hobbies/chess-tempo-viewer.txt"
    process_pgn(input_file_path, output_file)
    print("Traitement terminé. Résultat sauvegardé dans", output_file)
