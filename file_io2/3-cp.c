#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include "main.h"
#include <unistd.h>

/**
 * main - check the code
 * @argc: no. of params
 * @argv: array of params
 *
 * Return: Always 0.
 */
int main(int argc, char *argv[])
{
	char *fone, *ftwo;
	int fdone, fdtwo, sz = 1024, wr = 0, *buffer[1024];

	if (argc != 3)
	{
		dprintf(STDERR_FILENO, "Usage: cp file_from file_to\n");
		exit(97);
	}

	fone = argv[1];
	ftwo = argv[2];
	fdone = open(fone, O_RDONLY);
	fdtwo = open(ftwo, O_WRONLY | O_CREAT | O_TRUNC, 0664);

	if (fdone < 0)
	{
		dprintf(STDERR_FILENO, "Error: Can't read from file %s\n", fone);
		exit(98);
	}
	if (fdtwo < 0)
	{
		dprintf(STDERR_FILENO, "Error: Can't write to %s\n", ftwo);
		exit(99);
	}

	while (sz != 0)
	{
		sz = read(fdone, buffer, 1024);
		if (sz < 0)
		{
			dprintf(STDERR_FILENO, "Error: Can't read from file %s\n", fone);
			exit(98);
		}
		
		wr = write(fdtwo, buffer, sz);
		if (wr < 0)
		{
			dprintf(STDERR_FILENO, "Error: Can't write to %s\n", ftwo);
			exit(99);
		}
	}

	if (close(fdone) < 0)
	{
		dprintf(STDERR_FILENO, "Error: Can't close fd %d\n", fdone);
		exit(100);
	}

	if (close(fdtwo) < 0)
	{
		dprintf(STDERR_FILENO, "Error: Can't close fd %d\n", fdtwo);
		exit(100);
	}

	return (0);
}
