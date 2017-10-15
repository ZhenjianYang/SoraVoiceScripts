from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
    Fade(1000)
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
        "\x07\x05There is a card trapped between the pages.\x02",
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
            "\x07\x05'The door has already been opened.\x01",
            "Join the [Dance of the Valorous].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #2
        0x101,
        "#1019FOh! Look what I found!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x108,
        (
            "#073FOh, I get it. I guess this is\x01",
            "technically considered Republican\x01",
            "territory...\x02\x03",

            "#072FIt absolutely is a 'foreign manse.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        (
            "#044FAnd the Blue Knight is a character\x01",
            "from the novel, I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #5
        0x101,
        (
            "#1009FGeez... He sure is detail-oriented.\x02\x03",

            "#1000FAnyway, I got a feeling that this\x01",
            "next one's the last of 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x104,
        (
            "#035F'Dance of the Valorous'...\x01",
            "Well, now where could that be?\x02",
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
