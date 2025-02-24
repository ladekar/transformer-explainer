from graphviz import Digraph

# Create a Digraph object
dot = Digraph(comment='Advanced Transformer Architecture', format='png')
dot.attr(rankdir='LR', size='8,5')

# Define input components
dot.node('Input', 'Input\nEmbeddings', shape='box')
dot.node('PE', 'Positional\nEncoding', shape='box')
dot.node('Add', 'Add & Norm', shape='box')

# Define encoder layers (simplified as three layers)
dot.node('Enc1', 'Encoder Layer 1\n(Multi-Head Self-Attention\n+ Feed Forward)', shape='box')
dot.node('Enc2', 'Encoder Layer 2\n(Multi-Head Self-Attention\n+ Feed Forward)', shape='box')
dot.node('Enc3', 'Encoder Layer 3\n(Multi-Head Self-Attention\n+ Feed Forward)', shape='box')

# Define decoder layers (simplified as three layers)
dot.node('Dec1', 'Decoder Layer 1\n(Masked Self-Attention\n+ Cross-Attention\n+ Feed Forward)', shape='box')
dot.node('Dec2', 'Decoder Layer 2\n(Masked Self-Attention\n+ Cross-Attention\n+ Feed Forward)', shape='box')
dot.node('Dec3', 'Decoder Layer 3\n(Masked Self-Attention\n+ Cross-Attention\n+ Feed Forward)', shape='box')

# Define output layer
dot.node('Output', 'Output\n(Linear + Softmax)', shape='box')

# Build the encoder path
dot.edge('Input', 'PE', label='Add')
dot.edge('PE', 'Add')
dot.edge('Add', 'Enc1')
dot.edge('Enc1', 'Enc2')
dot.edge('Enc2', 'Enc3')

# Build the decoder path (assumes shifted right inputs for decoding)
dot.edge('Input', 'Dec1', label='Shifted Right')
dot.edge('Dec1', 'Dec2')
dot.edge('Dec2', 'Dec3')

# Connect encoder output to each decoder layer with cross-attention (simplified)
dot.edge('Enc3', 'Dec1', label='Cross-Attn')
dot.edge('Enc3', 'Dec2', label='Cross-Attn')
dot.edge('Enc3', 'Dec3', label='Cross-Attn')

# Connect final decoder output to the output projection
dot.edge('Dec3', 'Output', label='Projection')

# Render and view the diagram (this creates a file "advanced_transformer_architecture.png")
dot.render('advanced_transformer_architecture', view=True)
