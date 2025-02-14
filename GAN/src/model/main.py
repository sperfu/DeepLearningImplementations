import os
import argparse


def launch_training(**kwargs):

    # Launch training
    train_GAN.train(**kwargs)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Train model')
    parser.add_argument('--backend', type=str, default="theano", help="theano or tensorflow")
    parser.add_argument('--dset', type=str, default="mnist", help="mnist or celebA")
    parser.add_argument('--batch_size', default=32, type=int, help='Batch size')
    parser.add_argument('--n_batch_per_epoch', default=200, type=int, help="Number of training epochs")
    parser.add_argument('--nb_epoch', default=400, type=int, help="Number of batches per epoch")
    parser.add_argument('--epoch', default=10, type=int, help="Epoch at which weights were saved for evaluation")
    parser.add_argument('--nb_classes', default=2, type=int, help="Number of classes")
    parser.add_argument('--do_plot', default=False, type=bool, help="Debugging plot")
    parser.add_argument('--bn_mode', default=2, type=int, help="Batch norm mode")
    parser.add_argument('--img_dim', default=64, type=int, help="Image width == height")
    parser.add_argument('--noise_scale', default=0.5, type=float, help="variance of the normal from which we sample the noise")
    parser.add_argument('--label_smoothing', default=False, type=bool, help="Whether to smooth the positive labels when training D")
    parser.add_argument('--label_flipping', default=0, type=float, help="Probability (0 to 1.) to flip the labels when training D")

    args = parser.parse_args()

    assert args.dset in ["mnist", "celebA"]

    # Set the backend by modifying the env variable
    if args.backend == "theano":
        os.environ["KERAS_BACKEND"] = "theano"
    elif args.backend == "tensorflow":
        os.environ["KERAS_BACKEND"] = "tensorflow"

    # Import the backend
    import keras.backend as K

    # manually set dim ordering otherwise it is not changed
    if args.backend == "theano":
        image_dim_ordering = "th"
        K.set_image_dim_ordering(image_dim_ordering)
    elif args.backend == "tensorflow":
        image_dim_ordering = "tf"
        K.set_image_dim_ordering(image_dim_ordering)

    import train_GAN

    # Set default params
    d_params = {"mode": "train_GAN",
                "dset": args.dset,
                "batch_size": args.batch_size,
                "n_batch_per_epoch": args.n_batch_per_epoch,
                "nb_epoch": args.nb_epoch,
                "model_name": "CNN",
                "epoch": args.epoch,
                "nb_classes": args.nb_classes,
                "do_plot": args.do_plot,
                "image_dim_ordering": image_dim_ordering,
                "bn_mode": args.bn_mode,
                "img_dim": args.img_dim,
                "label_smoothing": args.label_smoothing,
                "label_flipping": args.label_flipping,
                "noise_scale": args.noise_scale,
                }

    # Launch training
    launch_training(**d_params)
