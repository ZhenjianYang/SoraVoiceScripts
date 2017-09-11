from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(610490, -10, -60800, 0)
    OP_6C(225000, 0)
    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x10)
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrPos(0x101, 610110, -10, -60540, 180)
    SetChrPos(0x102, 609200, 0, -59580, 180)
    SetChrPos(0x107, 610360, 0, -59200, 180)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0xFE,
        "*siiiigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "I really am just no good.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #2
        0x101,
        (
            "#506F???\x02\x03",

            "Okay, what's with the long face?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        "Hmm? Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "It's just that my superior is kinda\x01",
            "peeved at me. My...very beautiful\x01",
            "superior...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "...So, did you want something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#006FYeah, I just needed to\x01",
            "ask a question.\x02\x03",

            "We're looking for a small\x01",
            "orbal engine, the kind that\x01",
            "fits into a haulage vehicle.\x02\x03",

            "This looks like the right\x01",
            "place to find one...\x02\x03",

            "...but do you know specifically\x01",
            "where we should look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "An orbment for a haulage\x01",
            "vehicle, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "And what are you planning\x01",
            "to do with it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010FThere's a vehicle up the road\x01",
            "that's broken down.\x02\x03",

            "It looks like the orbal engine\x01",
            "is the source of the problem.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #10
        0xFE,
        "Ahh, okay. No problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "You're just looking to\x01",
            "swap it out, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "That shouldn't be too difficult.\x02",
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0x94A16, 0xFFFFFFE2, 0xFFFF0C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x94B7E, 0xA, 0xFFFF0074, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x94A16, 0xFFFFFFE2, 0xFFFF0C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x94F98, 0xFFFFFFD8, 0xFFFF0D94, 0xBB8, 0x0)
    OP_8C(0xFE, 360, 400)

    ChrTalk(    #13
        0xFE,
        "Here you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "It's the only one I've got,\x01",
            "so make sure you don't lose\x01",
            "it along the way!\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x0, 0x258, 0x7D0, 0x0)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        "\x07\x00Received \x07\x02Drive Orbment\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_94(0x1, 0xFE, 0xB4, 0x258, 0x7D0, 0x0)

    ChrTalk(    #16
        0x101,
        "#000FThank you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        (
            "#010FOkay, let's take this\x01",
            "over to Wong.\x02\x03",

            "They're probably still on\x01",
            "the Tratt Plains Road.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #18
        0x101,
        "#000FYeah, probably.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "You folks be careful, too.\x02",
    )

    CloseMessageWindow()

    def lambda_66D():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66D)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #20
        0x107,
        (
            "#060FWe will.\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#010FIf you'll excuse us, then...\x02",
    )

    CloseMessageWindow()
    OP_3E(0x346, 1)
    OP_28(0x29, 0x4, 0x8)
    OP_28(0x29, 0x1, 0x10)
    OP_28(0x29, 0x1, 0x20)
    OP_A2(0x2)
    EventEnd(0x0)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
