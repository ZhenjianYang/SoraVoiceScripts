from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4111_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
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
    OP_6D(1120, 0, 63720, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 1620, 0, 63260, 0)
    SetChrPos(0x105, 3140, 0, 62800, 315)
    SetChrPos(0x104, 2160, 0, 61840, 0)
    SetChrPos(0x108, 700, 0, 61860, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1015FHmm... So the 'aged general'\x01",
            "is probably General Morgan.\x02\x03",

            "In that case, is this the\x01",
            "'onlooker of time'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x105,
        "#042FI'd say it's likely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x104,
        "#030FWe'll need to check inside.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        (
            "\x07\x05Estelle asked and received permission from the owners\x01",
            "of the house to investigate the clock.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_6D(-4940, 0, 64160, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    SetChrPos(0xD, -1600, 0, 64260, 90)
    SetChrPos(0xE, -2180, 0, 63520, 90)
    SetChrPos(0xF, -1600, 0, 64800, 90)
    SetChrPos(0x101, 1660, 0, 62460, 0)
    SetChrPos(0x105, -560, 0, 62280, 45)
    SetChrPos(0x104, -240, 0, 61160, 45)
    SetChrPos(0x108, -1620, 0, 61240, 45)
    FadeToBright(1000, 0)

    def lambda_332():
        OP_6D(-940, 0, 64160, 3000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_332)
    Sleep(1200)
    OP_8E(0x101, 0x67C, 0x0, 0xF8AC, 0x3E8, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #4
        "\x07\x05Upon inspection, they found a card stuck to the back.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05'The second key is in the city.\x01",
            "Seek the [Symbol Perched on the Ground].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #6
        0x108,
        "#3P#074FAs we thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        "My...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "To think something like that\x01",
            "was in this house!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #9
        0x101,
        (
            "#1016FWell, this guy isn't the type to\x01",
            "harm people who aren't involved\x01",
            "in his weird plans, so don't worry.\x02\x03",

            "#1000FBest to close up tight at night just\x01",
            "in case there's any more mischief,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xE,
        "Y-Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        "Yes, we'll be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        "#030FAll right, shall we continue?\x02",
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x4)
    OP_28(0xC4, 0x1, 0x8)
    OP_64(0x0, 0x1)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_43(0xF, 0x0, 0x6, 0x2)
    SetChrPos(0xF, -1460, 0, 64920, 180)
    OP_A2(0x2)
    EventEnd(0x4)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
