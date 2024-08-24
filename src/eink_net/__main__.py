import os
import pathlib
import sys

from PIL import ImageFont, Image, ImageDraw


repo_root = pathlib.Path(__file__).parent.parent.parent
epd = repo_root / "third_party" / "e-Paper" / "RaspberryPi_JetsonNano" / "python"
picdir = epd / "pic"
libdir = epd / "lib"
sys.path.append(str(libdir))


from waveshare_epd import epd2in7_V2


def main():
    try:
        epd = epd2in7_V2.EPD()

        epd.init()
        epd.Clear()
        epd.init_Fast()

        font18 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 18)

        Limage = Image.new("1", (epd.width, epd.height), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Limage)
        draw.text((2, 0), sys.stdin.read(), font=font18, fill=0)
        epd.display_Fast(epd.getbuffer(Limage))
    finally:
        epd.sleep()
        epd2in7_V2.epdconfig.module_exit(cleanup=True)


if __name__ == "__main__":
    main()
