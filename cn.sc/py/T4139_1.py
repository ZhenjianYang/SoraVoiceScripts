from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4139_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4139.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4139_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-60500, 0, -44360, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -59600, 0, -45100, 270)
    SetChrPos(0x105, -58710, 0, -44550, 270)
    SetChrPos(0x104, -58080, 0, -45950, 270)
    SetChrPos(0x108, -57070, 0, -45700, 270)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        (
            "\x07\x05书页之间\x01",
            "夹着一张卡。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05　　　门已打开。　\x01",
            "参加『勇者们的舞会』吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #2
        0x101,
        "#1019F这、这种地方……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x108,
        (
            "#073F原来如此，这个地方地区\x01",
            "是在共和国的管辖区内……\x02\x03",

            "#072F正是所谓『异国之馆』吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        (
            "#044F而『苍之骑士』\x01",
            "看来是小说的登场人物。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #5
        0x101,
        (
            "#1009F真是的……\x01",
            "够会给人\x01",
            "添麻烦的。\x02\x03",

            "#1000F不过，看来这是最后了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x104,
        (
            "#035F『勇者们的舞会』啊……\x01",
            "那么，是说哪个地方呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x40)
    OP_28(0xC4, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
