def process_file(input_file, output_file):
  """ Keep only main documents content of CISI.ALL """
  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    in_document = False  # Flag to track if we're inside a document section
    document_content = []
    for line in f_in:
      line = line.strip()  # Remove leading/trailing whitespace
      if line.startswith(".I"):
        in_document = True
        f_out.write(line + "\n")  # Write the line with .I
        document_content = []  # Clear content for a new document
      elif line.startswith(".X"):
        in_document = False
        if document_content:
          f_out.write("\n".join(document_content) + "\n\n")  # Write document content with double newline
      elif in_document:
        document_content.append(line)  # Append content lines within a document

# Set your file paths
input_file = "CISI.ALL"
output_file = "CISI.doc.txt"

process_file(input_file, output_file)

print(f"Main document content extracted (including .I lines) and saved to: {output_file}")
