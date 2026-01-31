from debugger.plot_utils import plot_loss_curves

train_losses = [0.9, 0.7, 0.5, 0.3, 0.2]
val_losses = [0.95, 0.8, 0.75, 0.78, 0.82]

plot_loss_curves(train_losses, val_losses)


