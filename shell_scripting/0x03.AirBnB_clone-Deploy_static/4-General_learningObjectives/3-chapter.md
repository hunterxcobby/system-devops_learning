A tgz archive, also known as a tarball, is a type of compressed archive file that is commonly used in Unix and Linux systems. It combines multiple files into a single archive and compresses them using the gzip compression algorithm. The name "tgz" comes from combining "tar," which is the archival tool used to create the archive, and "gz," which stands for gzip compression.

Here's a breakdown of what a tgz archive consists of:

1. **Tar**: Tar is a file archiving utility that creates a single file containing multiple files and directories. It does not compress the files, but rather creates a consolidated archive. Tar preserves file attributes such as permissions, timestamps, and directory structures.

2. **Gzip**: Gzip is a file compression utility that reduces the size of files using the gzip compression algorithm. It compresses individual files or streams of data, often used in conjunction with tar to create compressed archive files.

When you create a tgz archive, you're essentially using tar to bundle files and directories into a single archive and then using gzip to compress the archive, resulting in a single compressed file with the ".tgz" extension.

To create a tgz archive, you typically use the following command in a Unix or Linux terminal:

```
tar czf archive.tgz files...
```

- `c`: Create a new archive.
- `z`: Compress the archive using gzip.
- `f`: Specify the filename of the archive.

And to extract the contents of a tgz archive, you use the following command:

```
tar xzf archive.tgz
```

- `x`: Extract files from the archive.
- `z`: Decompress the archive using gzip.
- `f`: Specify the filename of the archive.

Tgz archives are commonly used for packaging files and directories for distribution or backup purposes due to their efficient compression and ease of use.