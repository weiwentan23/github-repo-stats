from io import StringIO
import textwrap
import os
import logging
import shutil
import sys

log = logging.getLogger()
MD_REPORT = StringIO()


def main() -> None:
    MD_REPORT.write(
        textwrap.dedent(
            """
    ## Top referrers and paths
    Note: Each data point in the plots shown below is influenced by the 14 days
    leading up to it. Each data point is the arithmetic mean of the "unique
    visitors per day" metric, built from a time window of 14 days width, and
    plotted at the right edge of that very time window. That is, these plots
    respond slowly to change (narrow peaks are smoothed out).
    """
        )
    )
    output_directory = "summary"
    if os.path.exists(output_directory):
        if not os.path.isdir(output_directory):
            log.error(
                "The specified output directory path does not point to a directory: %s",
                output_directory,
            )
            sys.exit(1)

        log.info("Remove output directory: %s", output_directory)
        shutil.rmtree(output_directory)

    log.info("Create output directory: %s", output_directory)
    os.makedirs(output_directory)

    md_report_filepath = os.path.join(output_directory, "summary.txt")
    with open(md_report_filepath, "wb") as f:
        f.write(MD_REPORT.getvalue().encode("utf-8"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
