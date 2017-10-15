from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Helmuth',                              # 9
        'Norche',                               # 10
        'Martin',                               # 11
        'Marian',                               # 12
        'Helena',                               # 13
        'Katrina',                              # 14
        'Dalia',                                # 15
        'Rianne',                               # 16
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


    AddCharChip(
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01230 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01350 ._CH',             # 06
        'ED6_DT07/CH01480 ._CH',             # 07
        'ED6_DT27/CH03005 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01230P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01350P._CP',             # 06
        'ED6_DT07/CH01480P._CP',             # 07
        'ED6_DT27/CH03005P._CP',             # 08
    )

    DeclNpc(
        X                   = 60000,
        Z                   = 0,
        Y                   = 2950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 60530,
        Z                   = 0,
        Y                   = 62340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 115690,
        Z                   = 0,
        Y                   = 60750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 125180,
        Z                   = 0,
        Y                   = 63830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 114980,
        Z                   = 0,
        Y                   = -55400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -1040,
        Z                   = 0,
        Y                   = -56350,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -56390,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2470,
        Z                   = 0,
        Y                   = 61010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = 1520,
        TriggerZ            = 0,
        TriggerY            = 64780,
        TriggerRange        = 1000,
        ActorX              = 1520,
        ActorZ              = 2000,
        ActorY              = 64780,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_41B",          # 01, 1
        "Function_2_472",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_4BA",          # 04, 4
        "Function_5_996",          # 05, 5
        "Function_6_13CC",         # 06, 6
        "Function_7_1672",         # 07, 7
        "Function_8_1934",         # 08, 8
        "Function_9_1CFF",         # 09, 9
        "Function_10_21D3",        # 0A, 10
        "Function_11_25C0",        # 0B, 11
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28B")
    SetChrPos(0x8, 59640, 0, 1740, 90)
    SetChrPos(0x9, 60760, 0, 1740, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 123980, 0, 1080, 90)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrFlags(0xA, 0x10)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jump("loc_41A")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2B7")
    SetChrPos(0x8, 59640, 0, 1740, 90)
    SetChrPos(0x9, 60760, 0, 1740, 270)
    Jump("loc_41A")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_327")
    SetChrPos(0x8, 55510, 0, 62080, 270)
    SetChrPos(0xA, 115170, 0, 60900, 90)
    SetChrPos(0xB, 116170, 0, 60910, 270)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xD, -2640, 0, 64080, 179)
    Jump("loc_41A")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_397")
    SetChrPos(0x8, 55510, 0, 62080, 270)
    SetChrPos(0xB, 114980, 0, -55400, 0)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    SetChrPos(0xD, -1600, 0, 64260, 90)
    SetChrPos(0xE, -2180, 0, 63520, 90)
    SetChrPos(0xF, -1460, 0, 64920, 180)
    Jump("loc_41A")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E9")
    SetChrPos(0x8, 55510, 0, 62080, 270)
    SetChrPos(0xB, 114980, 0, -55400, 0)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    SetChrPos(0xD, -2640, 0, 64080, 179)
    Jump("loc_41A")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_41A")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xB, 114980, 0, -55400, 0)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    Jump("loc_41A")

    label("loc_41A")

    Return()

    # Function_0_216 end

    def Function_1_41B(): pass

    label("Function_1_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_437")
    OP_B1("t4111_y")
    Jump("loc_440")

    label("loc_437")

    OP_B1("t4111_n")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_44E")
    OP_43(0xF, 0x0, 0x6, 0x2)

    label("loc_44E")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_471")
    OP_65(0x0, 0x1)

    label("loc_471")

    Return()

    # Function_1_41B end

    def Function_2_472(): pass

    label("Function_2_472")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_8D(0xFE, 113830, 62500, 117900, 58880, 2000)
    Jump("Function_2_472")

    label("loc_495")

    Return()

    # Function_2_472 end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B9")
    OP_8D(0xFE, -1150, 59690, -3770, 62520, 3000)
    Jump("Function_3_496")

    label("loc_4B9")

    Return()

    # Function_3_496 end

    def Function_4_4BA(): pass

    label("Function_4_4BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4C7")
    Jump("loc_992")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_525")

    ChrTalk(    #0
        0xFE,
        (
            "W-With things as they are, I really\x01",
            "don't think now's the time to fish, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_6BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_623")

    ChrTalk(    #1
        0xFE,
        "...How do I put this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I feel like I understand what it means\x01",
            "to be left behind now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I intend to make a new start on my life here,\x01",
            "and enjoy fishing with my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Things are bound to be a little complex, but...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6B9")

    label("loc_623")


    ChrTalk(    #5
        0xFE,
        (
            "I feel like I understand what it means\x01",
            "to be left behind now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I intend to make a new start on my life here,\x01",
            "and enjoy fishing with my wife.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9")

    Jump("loc_992")

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_700")

    ChrTalk(    #7
        0xFE,
        "I've decided.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I'm...giving up fishing, I think.\x02",
    )

    CloseMessageWindow()
    Jump("loc_992")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DC")

    ChrTalk(    #9
        0xFE,
        (
            "Can't even imagine the work that goes\x01",
            "into reaching the Master Fisher rank. Can you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "That IS the top rank in the Fisherman's Guild,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "To think my wife's gotten that far...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7F1")

    label("loc_7DC")


    ChrTalk(    #12
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    label("loc_7F1")

    Jump("loc_992")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_7FE")
    Jump("loc_992")

    label("loc_7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91F")

    ChrTalk(    #14
        0xFE,
        (
            "Even though fishing is my passion, my wife\x01",
            "beat me in joining the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "She's apparently been going to the lake pretty\x01",
            "often while I've been away at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "And, man... The gap between our abilities\x01",
            "is only just going to keep getting bigger.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_992")

    label("loc_91F")


    ChrTalk(    #17
        0xFE,
        (
            "Incidentally, I haven't even joined the\x01",
            "Fisherman's Guild myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "My humiliation is deep and profound...\x02",
    )

    CloseMessageWindow()

    label("loc_992")

    TalkEnd(0xFE)
    Return()

    # Function_4_4BA end

    def Function_5_996(): pass

    label("Function_5_996")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_9A3")
    Jump("loc_13C8")

    label("loc_9A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #19
        0xFE,
        "What are you saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "With an attitude like that, you'll\x01",
            "never be able to join the group!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "This is exactly the time to cast\x01",
            "your line and calm your mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "The mindset of a Master Fisher is that of\x01",
            "a clear, still pond!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_B2B")

    label("loc_AA3")


    ChrTalk(    #23
        0xFE,
        (
            "This is exactly the time to cast\x01",
            "your line and calm your mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "The mindset of a Master Fisher is that of\x01",
            "a clear, still pond!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2B")

    Jump("loc_13C8")

    label("loc_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(    #25
        0xFE,
        (
            "Heehee! I bought a new rod to\x01",
            "replace my old one recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I'd been using the same rod since I started\x01",
            "fishing, so I thought it was about time for an\x01",
            "upgrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Now, then, what to do with my old rod...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "My husband only uses new, top-class rods,\x01",
            "you see. So I had to keep up!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #29
        0xFE,
        "You... You fish, don't you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #30
        0x101,
        (
            "#1004FHuh? Well, some...\x02\x03",

            "#1013F(H-How did she know?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Well, then! Allow me to offer you this.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #32
        "\x07\x00Received #590i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x24E, 1)
    OP_0D()

    ChrTalk(    #33
        0x101,
        "#1008FWow! Th-Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Make sure to catch plenty of fish\x01",
            "with it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x166B)
    Jump("loc_13C8")

    label("loc_DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_EA4")

    ChrTalk(    #35
        0xFE,
        (
            "Starting with his next vacation, I'll\x01",
            "be teaching my husband to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "My husband is willing to take me\x01",
            "on a fishing trip next time he has vacation\x01",
            "days saved up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "A lot's happened, but...right now,\x01",
            "I'm actually pretty happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C8")

    label("loc_EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_FAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")

    ChrTalk(    #38
        0xFE,
        (
            "My husband has been pouting an\x01",
            "awful lot these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "And over such a little thing, too! How pathetic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "When we first met, he was a much more\x01",
            "manly fellow, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_FA8")

    label("loc_F6C")


    ChrTalk(    #41
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "Perhaps I've been pushing him a bit too hard.\x02",
    )

    CloseMessageWindow()

    label("loc_FA8")

    Jump("loc_13C8")

    label("loc_FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103E")

    ChrTalk(    #43
        0xFE,
        (
            "When I told him I received the rank of Master\x01",
            "Fisher, my husband suddenly got very quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "Ohoho! I must've struck a nerve.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C8")

    label("loc_103E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A7")

    ChrTalk(    #45
        0xFE,
        "May I have your ear for a moment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I actually just received the rank of Master\x01",
            "Fisher from the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Now I can be counted alongside people\x01",
            "like Lloyd. You know Lloyd,\x01",
            "don't you? He's a wonderful fisherman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Once my husband comes back from the\x01",
            "castle, I'm going to positively rub\x01",
            "his face in this. Oh, I will!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1266")

    label("loc_11A7")


    ChrTalk(    #49
        0xFE,
        (
            "I actually just received the rank of Master\x01",
            "Fisher from the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Once my husband comes back from the\x01",
            "castle, I'm going to positively rub\x01",
            "his face in this. Oh, I will!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1266")

    Jump("loc_13C8")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_13C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")

    ChrTalk(    #51
        0xFE,
        (
            "My husband was so busy with fishing and work,\x01",
            "he didn't pay me a moment's notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "That's why I decided to take my husband\x01",
            "down a peg by beating him at his own hobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "He ignored his sweet wife, and\x01",
            "I intend to make him pay dearly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_13C8")

    label("loc_1373")


    ChrTalk(    #54
        0xFE,
        (
            "Lately, sending my husband off to\x01",
            "work has been so terribly fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "O-hohoho!\x02",
    )

    CloseMessageWindow()

    label("loc_13C8")

    TalkEnd(0xFE)
    Return()

    # Function_5_996 end

    def Function_6_13CC(): pass

    label("Function_6_13CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_142C")

    ChrTalk(    #56
        0xFE,
        (
            "Amen! Time to begin evacuation\x01",
            "training for our house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "First, roll call!\x02",
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_142C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_14BE")

    ChrTalk(    #58
        0xFE,
        "Hahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Yep! I need to keep command of our little group.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Listen up! Time to work like crazy\x01",
            "and get some vacation money!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_14BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_155E")

    ChrTalk(    #61
        0xFE,
        "Elmo Hot Springs, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "What's your take on family vacations?\x01",
            "They're AMAZING EVENTS, let me tell you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "I could even make a rulebook!\x02",
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_155E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DD")

    ChrTalk(    #64
        0xFE,
        "A great meal certainly gives one energy to spare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Yes. I... I want to do something really\x01",
            "worth doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_15DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1608")

    ChrTalk(    #66
        0xFE,
        "Oh, I smell something good!\x02",
    )

    CloseMessageWindow()
    Jump("loc_166E")

    label("loc_1608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_166E")

    ChrTalk(    #67
        0xFE,
        "Ahhh... How peaceful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Peace is so boring. I can't even\x01",
            "muster up the will to work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166E")

    TalkEnd(0xFE)
    Return()

    # Function_6_13CC end

    def Function_7_1672(): pass

    label("Function_7_1672")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16CB")

    ChrTalk(    #69
        0xFE,
        (
            "Heehee, at times like this, it's great\x01",
            "comfort having that man around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1930")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1715")

    ChrTalk(    #70
        0xFE,
        (
            "Haha, seems like he's gotten some\x01",
            "of his energy back, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1930")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_178D")

    ChrTalk(    #71
        0xFE,
        (
            "Oh, yes. I'd LOVE for us to go to\x01",
            "the Elmo Hot Springs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "And, I want you to run the trip, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1930")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1827")

    ChrTalk(    #73
        0xFE,
        (
            "Even serving a big meal like this will only\x01",
            "give him energy for a short while, and it's\x01",
            "hard on the finances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "What can I do...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1930")

    label("loc_1827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_18C7")

    ChrTalk(    #75
        0xFE,
        (
            "I suppose the way to get him some energy\x01",
            "is to make him a really great meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I guess I've just got to try a few things\x01",
            "and see what sticks!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1930")

    label("loc_18C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1930")

    ChrTalk(    #77
        0xFE,
        "That man really is trouble sometimes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I've got to get him to cheer up and\x01",
            "go to work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1930")

    TalkEnd(0xFE)
    Return()

    # Function_7_1672 end

    def Function_8_1934(): pass

    label("Function_8_1934")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19D7")

    ChrTalk(    #79
        0xFE,
        (
            "There are all kinds of emergencies nowadays,\x01",
            "so this kinda thing is important, don't get\x01",
            "me wrong...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "But Dad's smile kinda makes me wonder.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_19D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(    #81
        0xFE,
        (
            "The number one at our house is\x01",
            "definitely Mom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Dad's just gonna keep getting wrapped around\x01",
            "her little finger his whole life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1AD5")

    ChrTalk(    #83
        0xFE,
        "Ooooooh... Nice one, Mom!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I should write that down...\x01",
            "It might be useful in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_1AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B45")

    ChrTalk(    #85
        0xFE,
        "I wonder how Mom's gonna respond to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "Well, I'm gonna sit back and watch their war.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_1B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BCC")

    ChrTalk(    #87
        0xFE,
        (
            "We're gonna have top-grade beef steak\x01",
            "today to cheer up Dad, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "Mom sure is being awfully sweet to Dad...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1CFB")

    ChrTalk(    #89
        0xFE,
        (
            "Dad gets kinda lazy without a big event like\x01",
            "the Martial Arts Competition or the Birthday\x01",
            "Celebration going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "He can't really run the family except\x01",
            "when there's something going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "But, I mean, that's how it is, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "After all, Mom's the real head honcho in our house.\x02",
    )

    CloseMessageWindow()

    label("loc_1CFB")

    TalkEnd(0xFE)
    Return()

    # Function_8_1934 end

    def Function_9_1CFF(): pass

    label("Function_9_1CFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1DA8")

    ChrTalk(    #93
        0xFE,
        (
            "To think that not being able to use orbments\x01",
            "would be this anxiety-inducing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "I wonder if he's safe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "I wish I could at least contact him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_1DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E73")

    ChrTalk(    #96
        0xFE,
        "The harbor isn't very far from here, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I need to keep Rianne safe\x01",
            "while my husband is away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "I don't want to see what happened to her\x01",
            "in the coup d'etat ever happen again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_1E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1F64")

    ChrTalk(    #99
        0xFE,
        (
            "Even with the coup d'etat over,\x01",
            "my husband seems rather busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "When he comes to Grancel, he never\x01",
            "has the time to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I wish I could at least get him to see Rianne,\x01",
            "but I suppose that's how things are for now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_1F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FD7")

    ChrTalk(    #102
        0xFE,
        (
            "To think someone like that could sneak\x01",
            "into our house...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Anyway, I'm just glad Rianne is safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_1FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_208E")

    ChrTalk(    #104
        0xFE,
        "A bit ago, Colonel Cid came to visit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "My granddaughter's quite fond\x01",
            "of Colonel Cid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "The colonel quite likes children,\x01",
            "and I'm sure the children can tell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_208E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_213D")

    ChrTalk(    #107
        0xFE,
        (
            "For all my husband's dislike of bracers, he\x01",
            "certainly speaks of them quite a lot recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Perhaps it's Cassius' influence...as shocking\x01",
            "as that would be!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_213D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_21CF")

    ChrTalk(    #109
        0xFE,
        (
            "My husband's expression when he heard that\x01",
            "General Cassius would be returning was oddly\x01",
            "positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "I wish you could have seen it!\x02",
    )

    CloseMessageWindow()

    label("loc_21CF")

    TalkEnd(0xFE)
    Return()

    # Function_9_1CFF end

    def Function_10_21D3(): pass

    label("Function_10_21D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2287")

    ChrTalk(    #111
        0xFE,
        (
            "It's kind of scary having only women around\x01",
            "the house at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "At the very least, I'll keep the missus and\x01",
            "Rianne safe in place of the good sir!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_2287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2330")

    ChrTalk(    #113
        0xFE,
        (
            "Whoaaaa! Apparently a tank went\x01",
            "on a rampage at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Rumors say the tank was headed for the castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "So was it going to go right past us?\x02",
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_2330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_23CF")

    ChrTalk(    #116
        0xFE,
        (
            "The good sir's worried about\x01",
            "madam's health, and so am I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I've at least got to get her good meals to\x01",
            "eat so she can build up some stamina.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_23CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_245F")

    ChrTalk(    #118
        0xFE,
        (
            "I'll make sure everything's closed up\x01",
            "tightly at night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Not that I'd ever let someone suspicious\x01",
            "into this mansion again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_245F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2497")

    ChrTalk(    #120
        0xFE,
        "Rianne's hungry, so I need to hurry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_2497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2520")

    ChrTalk(    #121
        0xFE,
        "The good sir's changed a bit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Maybe it's my imagination, but he seems\x01",
            "to smile more than I'm accustomed to\x01",
            "seeing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BC")

    label("loc_2520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(    #123
        0xFE,
        (
            "The good sir...uh, General Morgan...\x01",
            "can be a very scary person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "But you know what? Heehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#1SHe's totally under his wife's thumb.\x02",
    )

    CloseMessageWindow()

    label("loc_25BC")

    TalkEnd(0xFE)
    Return()

    # Function_10_21D3 end

    def Function_11_25C0(): pass

    label("Function_11_25C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_262C")

    ChrTalk(    #126
        0xFE,
        (
            "When the sun sets, it gets\x01",
            "reeeally dark in my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "If only the sun wouldn't set...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_262C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_26B1")

    ChrTalk(    #128
        0xFE,
        "They told me not to go out today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Mister Richard hasn't come to play much\x01",
            "lately either. It's sooooo boring...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_26B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_273B")

    ChrTalk(    #130
        0xFE,
        "Grandpa's gonna take me to the 'villah.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "I have scary memories of that 'villah,'\x01",
            "but I'll be fine with Grandpa along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27A4")

    ChrTalk(    #132
        0xFE,
        (
            "Hey, hey. What kind of person is\x01",
            "a 'phantom thief'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "I really wanna meet one one day.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_27A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2801")

    ChrTalk(    #134
        0xFE,
        (
            "I played lots and lots today.\x01",
            "Now I'm hungry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Is the food ready yet?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_2801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_287A")

    ChrTalk(    #136
        0xFE,
        (
            "I met a girl in a white dress\x01",
            "a little while ago, at the cathedral!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "I wish I coulda played with her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D1")

    label("loc_287A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_28D1")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #138
        0xFE,
        "Ah, it's the nice people who rescued me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Did you come to play?\x02",
    )

    CloseMessageWindow()

    label("loc_28D1")

    TalkEnd(0xFE)
    Return()

    # Function_11_25C0 end

    SaveToFile()

Try(main)
