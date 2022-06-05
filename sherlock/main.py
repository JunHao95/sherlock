from gooey import Gooey, GooeyParser


@Gooey(target="python3 ./sherlock.py", program_name='CSI Spy Program on Emails', suppress_gooey_flag=True)
def main():
    parser = GooeyParser(description="Extracting Platforms that a particular Email has created an account")
    ffmpeg = parser.add_argument_group('Platform Extraction Information')
    ffmpeg.add_argument('--usernames',
                        metavar='Input Email Address',
                        help='The Email Address that you want to check on',
                        required=True,
                        widget = "Textarea",
                        gooey_options={'initial_value':"Enter email here"})

    parser.parse_args()

if __name__ == '__main__':
    main()
