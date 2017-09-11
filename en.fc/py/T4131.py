from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4131   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Archbishop Currant',                   # 9
        'Bishop Reval',                         # 10
        'Sister Noah',                          # 11
        'Sister Ellen',                         # 12
        'Cisna',                                # 13
        'Seagaro',                              # 14
        '1st Lieutenant Schwarz',               # 15
        'Lila',                                 # 16
        'Mayor Maybelle',                       # 17
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01670 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH02090 ._CH',             # 05
        'ED6_DT07/CH02370 ._CH',             # 06
        'ED6_DT07/CH02360 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01670P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH02090P._CP',             # 05
        'ED6_DT07/CH02370P._CP',             # 06
        'ED6_DT07/CH02360P._CP',             # 07
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -131900,
        Z                   = 0,
        Y                   = 6270,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2140,
        Z                   = 0,
        Y                   = 15980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3470,
        Z                   = 0,
        Y                   = 510,
        Direction           = 110,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3160,
        Z                   = 0,
        Y                   = 13260,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4180,
        Z                   = 0,
        Y                   = 9260,
        Direction           = 2,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 200,
        Z                   = 0,
        Y                   = 14310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_437",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_51D",          # 03, 3
        "Function_4_629",          # 04, 4
        "Function_5_68B",          # 05, 5
        "Function_6_A0E",          # 06, 6
        "Function_7_B5F",          # 07, 7
        "Function_8_136D",         # 08, 8
        "Function_9_184D",         # 09, 9
        "Function_10_21D5",        # 0A, 10
        "Function_11_2E2A",        # 0B, 11
        "Function_12_2E2F",        # 0C, 12
        "Function_13_4591",        # 0D, 13
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    SetChrPos(0x8, 72000, 4000, 6060, 0)

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_2A5")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3020, 0, 13250, 340)
    SetChrPos(0xF, 4040, 0, 13250, 1)
    Jump("loc_2EF")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2CA")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 71980, 4000, 6250, 0)
    Jump("loc_2EF")

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_2D4")
    Jump("loc_2EF")

    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2DE")
    Jump("loc_2EF")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2E8")
    Jump("loc_2EF")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2EF")

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2FE")
    SetChrFlags(0xB, 0x80)
    Jump("loc_436")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_30D")
    SetChrFlags(0xB, 0x80)
    Jump("loc_436")

    label("loc_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_32D")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x8, 72000, 4000, 6060, 0)
    Jump("loc_436")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_341")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_436")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_36D")
    SetChrPos(0xB, -2130, 0, 15890, 180)
    SetChrPos(0x9, 2440, 1000, 18600, 180)
    Jump("loc_436")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3AA")
    SetChrPos(0xB, -133770, 0, 64950, 15)
    SetChrPos(0x9, 72000, 4000, 5780, 0)
    SetChrPos(0xA, -71370, 0, 3320, 90)
    Jump("loc_436")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3DB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, -2130, 0, 15890, 180)
    SetChrPos(0x9, 2440, 1000, 18600, 180)
    Jump("loc_436")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EA")
    SetChrFlags(0xB, 0x80)
    Jump("loc_436")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_416")
    SetChrPos(0xB, -2130, 0, 15890, 180)
    SetChrPos(0x9, 2440, 1000, 18600, 180)
    Jump("loc_436")

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_42A")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_436")

    label("loc_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_436")
    SetChrFlags(0xB, 0x80)

    label("loc_436")

    Return()

    # Function_0_252 end

    def Function_1_437(): pass

    label("Function_1_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A")
    OP_B1("t4131_y")
    Jump("loc_473")

    label("loc_46A")

    OP_B1("t4131_n")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_END)), "loc_483")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_493")
    OP_64(0x0, 0x1)

    label("loc_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_4A1")
    OP_64(0x0, 0x1)
    Jump("loc_506")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_4AB")
    Jump("loc_506")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_4B9")
    OP_64(0x0, 0x1)
    Jump("loc_506")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_4C3")
    Jump("loc_506")

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_4CD")
    Jump("loc_506")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_506")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4E1")
    Jump("loc_506")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EB")
    Jump("loc_506")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_506")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_506")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_506")

    label("loc_506")

    Return()

    # Function_1_437 end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_507")

    label("loc_51C")

    Return()

    # Function_2_507 end

    def Function_3_51D(): pass

    label("Function_3_51D")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x10,
        (
            "#610FDuring busy times like this, I always plan out my\x01",
            "prayer sessions well in advance. Can't neglect my\x01",
            "civic duties after all, right?\x02\x03",

            "But I'm certainly not a pure soul, so\x01",
            "I feel like prayer is a must for me. No\x01",
            "matter what, I have to make time for it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_51D end

    def Function_4_629(): pass

    label("Function_4_629")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xF,
        (
            "#620FHer Highness requested a visit\x01",
            "to the church today--much to\x01",
            "everyone's surprise!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_629 end

    def Function_5_68B(): pass

    label("Function_5_68B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(    #2
        0xE,
        (
            "#170FAre you here to consult the\x01",
            "archbishop?\x02\x03",

            "He should be in the sacramental\x01",
            "chamber right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0A")

    label("loc_6FE")

    OP_A2(0x6)

    ChrTalk(    #3
        0xE,
        "#170FEstelle! Joshua! How goes it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#001FHey, Julia. Fancy meeting you\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "#170FThe archbishop was very kind to me\x01",
            "when I took asylum here.\x02\x03",

            "I wanted to thank him, and keep \x01",
            "him up-to-date on the current\x01",
            "situation as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#501FAh, okay. That makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xE,
        (
            "#170F...And I wanted to thank the\x01",
            "both of you, too.\x02\x03",

            "You're the reason we were able\x01",
            "to save Her Majesty and the\x01",
            "princess.\x02\x03",

            "If you hadn't been there...\x01",
            "Well, at any rate, you have\x01",
            "our sincerest gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#000FDon't thank us! It was a group\x01",
            "effort. Give a little, get a\x01",
            "little, you know?\x02\x03",

            "Besides, we wanted to rescue\x01",
            "Her Majesty just as much as\x01",
            "you did!\x02\x03",

            "#001FSo it's win-win! Her Majesty's\x01",
            "safe, and everybody's happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xE,
        (
            "#173F...I suppose that's true.\x02\x03",

            "#171FBut thank you, nonetheless!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0A")

    TalkEnd(0xFE)
    Return()

    # Function_5_68B end

    def Function_6_A0E(): pass

    label("Function_6_A0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_A1B")
    Jump("loc_B5B")

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_A25")
    Jump("loc_B5B")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_A2F")
    Jump("loc_B5B")

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_A9C")

    ChrTalk(    #10
        0xFE,
        (
            "The archbishop's sermons always\x01",
            "ring true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I wish more people would come\x01",
            "listen to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5B")

    label("loc_A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_AA6")
    Jump("loc_B5B")

    label("loc_AA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_AB0")
    Jump("loc_B5B")

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_B36")

    ChrTalk(    #12
        0xFE,
        (
            "The cathedral's chapel has such\x01",
            "a pure, clean feel to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "May the blessings of Aidios be\x01",
            "with my wife this day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5B")

    label("loc_B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B40")
    Jump("loc_B5B")

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_B4A")
    Jump("loc_B5B")

    label("loc_B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_B54")
    Jump("loc_B5B")

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B5B")

    label("loc_B5B")

    TalkEnd(0xFE)
    Return()

    # Function_6_A0E end

    def Function_7_B5F(): pass

    label("Function_7_B5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_BE8")

    ChrTalk(    #14
        0xFE,
        (
            "After all that's happened, I'm\x01",
            "so glad the town has gone back\x01",
            "to its former peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "The will of Aidios be praised!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_C9A")

    ChrTalk(    #16
        0xFE,
        (
            "Seemed there was quite a commotion\x01",
            "outside earlier... I'm curious as\x01",
            "to what it may have been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "...No, I mustn't allow myself to\x01",
            "be distracted. I must pray!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D16")

    ChrTalk(    #18
        0xFE,
        (
            "There's a newly-cloistered nun,\x01",
            "but I haven't seen her around\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I pray that she has not taken\x01",
            "ill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D5C")

    ChrTalk(    #20
        0xFE,
        (
            "Time passes so quickly when I'm\x01",
            "lost in prayer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBC")

    label("loc_D5C")

    OP_A2(0x4)

    ChrTalk(    #21
        0xFE,
        "Oh, my... Is it this late already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Time passes so quickly when I'm\x01",
            "lost in prayer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBC")

    Jump("loc_1369")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_E2A")

    ChrTalk(    #23
        0xFE,
        (
            "My prayers today have been with\x01",
            "Her Majesty--that she may recover\x01",
            "quickly from her ailment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EBE")

    ChrTalk(    #24
        0xFE,
        (
            "It was the church that brought us back from\x01",
            "the brink of extinction following the Great\x01",
            "Collapse. Have people forgotten this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEC")

    label("loc_EBE")

    OP_A2(0x4)

    ChrTalk(    #25
        0xFE,
        (
            "After the development of orbal\x01",
            "technology, the world has become\x01",
            "very convenient indeed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "...but as a result, people seem\x01",
            "to have lost their faith in Aidios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "It was the church that brought us back from\x01",
            "the brink of extinction following the Great\x01",
            "Collapse. Have people forgotten this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEC")

    Jump("loc_1369")

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_11E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10D8")

    ChrTalk(    #28
        0xFE,
        (
            "As the days progress, fewer and fewer\x01",
            "faithful come to the church for prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "There are many who cease attendance immediately\x01",
            "upon graduating Sunday School, perhaps feeling\x01",
            "their obligations have been met.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E6")

    label("loc_10D8")

    OP_A2(0x4)

    ChrTalk(    #30
        0xFE,
        (
            "As the days progress, fewer and fewer\x01",
            "faithful come to the church for prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "There are many who cease attendance immediately\x01",
            "upon graduating Sunday School, perhaps feeling\x01",
            "their obligations have been met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "It is a sorry state of affairs,\x01",
            "in my mind...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E6")

    Jump("loc_1369")

    label("loc_11E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1262")

    ChrTalk(    #33
        0xFE,
        (
            "Both the bishop and archbishop\x01",
            "hold such lovely sermons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Perhaps you should stay and\x01",
            "listen as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_12BC")

    ChrTalk(    #35
        0xFE,
        (
            "I have never neglected my prayers.\x01",
            "Not for a single day in my entire\x01",
            "life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_12FF")

    ChrTalk(    #36
        0xFE,
        (
            "I thank the Goddess for her\x01",
            "protection every day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1369")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1369")

    ChrTalk(    #37
        0xFE,
        "Aidios watches over us, always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "We must treasure every day of\x01",
            "the life She has given us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1369")

    TalkEnd(0xFE)
    Return()

    # Function_7_B5F end

    def Function_8_136D(): pass

    label("Function_8_136D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_137A")
    Jump("loc_1849")

    label("loc_137A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1384")
    Jump("loc_1849")

    label("loc_1384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_138E")
    Jump("loc_1849")

    label("loc_138E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1398")
    Jump("loc_1849")

    label("loc_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_14B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13CB")

    ChrTalk(    #39
        0xFE,
        "Good luck at the tournament!\x02",
    )

    CloseMessageWindow()
    Jump("loc_14AD")

    label("loc_13CB")

    OP_A2(0x3)

    ChrTalk(    #40
        0xFE,
        "Estelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Did you get home all right\x01",
            "yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#008FUh, y-yeah, we sure did!\x02\x03",

            "#007F(How am I supposed to talk\x01",
            "to her, knowing she's really\x01",
            "Lieutenant Schwarz?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        "#010F(Try 'like you always have.')\x02",
    )

    CloseMessageWindow()

    label("loc_14AD")

    Jump("loc_1849")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1512")

    ChrTalk(    #44
        0xFE,
        (
            "I'm on break at the moment, so\x01",
            "I'm passing the time watching\x01",
            "the clouds roll by...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1849")

    label("loc_1512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1577")

    ChrTalk(    #45
        0xFE,
        "Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I must prepare myself, as morning\x01",
            "mass will be starting very soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1849")

    label("loc_1577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1581")
    Jump("loc_1849")

    label("loc_1581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 5)), scpexpr(EXPR_END)), "loc_15C2")

    ChrTalk(    #47
        0xFE,
        (
            "Thank you so much for your help\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1835")

    label("loc_15C2")

    OP_A2(0x67D)

    ChrTalk(    #48
        0xFE,
        "Y-You two are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Thank you so much for your help\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#004FOh, hey, you're that nun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "A thousand pardons...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "You two got into a fine mess\x01",
            "on my account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#505FMess? What mess?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#010FDo you mean...the scuffle with\x01",
            "the guards?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#001FOh, that? Pfft, that was nothing!\x02\x03",

            "#009FIt was their own fault, anyway.\x01",
            "They got me mad. And people don't\x01",
            "like me when I'm mad!\x02\x03",

            "#000FSo did they get you home okay?\x01",
            "They didn't rough you up or\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "Oh! Yes, yes. No problems at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#000FGreat. Just be careful when\x01",
            "you're walking alone from now\x01",
            "on, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "I will. Thank you again.\x02",
    )

    CloseMessageWindow()

    label("loc_1835")

    Jump("loc_1849")

    label("loc_1838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_1842")
    Jump("loc_1849")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1849")

    label("loc_1849")

    TalkEnd(0xFE)
    Return()

    # Function_8_136D end

    def Function_9_184D(): pass

    label("Function_9_184D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_18AD")

    ChrTalk(    #59
        0xFE,
        (
            "It's such a joy to see so many\x01",
            "smiling faces!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "May they all be blessed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_194E")

    ChrTalk(    #61
        0xFE,
        (
            "Soldiers are still scouring\x01",
            "the city to find the Royal\x01",
            "Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "The Royal Guard is highly trained,\x01",
            "so locating them is not an easy\x01",
            "task...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_194E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_END)), "loc_1A3E")

    ChrTalk(    #63
        0xFE,
        (
            "Sister Ellen has no sense of direction,\x01",
            "it seems, but she's extremely courteous\x01",
            "and very, very devout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "No one is perfect, though, of course,\x01",
            "and we must always remember that it's\x01",
            "our imperfections which make us special.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_1A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1B02")

    ChrTalk(    #65
        0xFE,
        (
            "Are you looking for Sister Ellen,\x01",
            "perchance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I believe the archbishop should\x01",
            "know her whereabouts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "He should be in the sacramental\x01",
            "chamber, to the southeast of this\x01",
            "room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_1B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1B6F")

    ChrTalk(    #68
        0xFE,
        "Oh, Goddess Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I have been blessed with another\x01",
            "day under your divine protection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1C29")

    ChrTalk(    #70
        0xFE,
        (
            "I've been thinking of hosting a\x01",
            "bazaar at the cathedral after the\x01",
            "Queen's Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If it's to happen, however, we'll\x01",
            "need to begin the preparations now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_1C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CAA")

    ChrTalk(    #72
        0xFE,
        (
            "I mustn't forget to ready the \x01",
            "hymnals today, before our next\x01",
            "service!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Now, where is Sister Ellen...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DDE")

    label("loc_1CAA")

    OP_A2(0x2)

    ChrTalk(    #74
        0xFE,
        (
            "I mustn't forget to ready the \x01",
            "hymnals today, before our next\x01",
            "service!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "There are over 200 books to comb through. We must\x01",
            "ensure no one wrote any dirty limericks in the\x01",
            "margins. It's quite a monumental task!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "Now, where is Sister Ellen...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I hope she hasn't gotten herself\x01",
            "lost again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    Jump("loc_21D1")

    label("loc_1DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1E2C")

    ChrTalk(    #78
        0xFE,
        (
            "Goddess Aidios, we humbly ask\x01",
            "for your protection this day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E9F")

    ChrTalk(    #79
        0xFE,
        (
            "I've been meaning to send Sister\x01",
            "Ellen on an errand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "...but I can't seem to find her!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F17")

    label("loc_1E9F")

    OP_A2(0x2)

    ChrTalk(    #81
        0xFE,
        (
            "I've been meaning to send Sister\x01",
            "Ellen on an errand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "...but I can't seem to find her!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Oh, bother...\x02",
    )

    CloseMessageWindow()

    label("loc_1F17")

    Jump("loc_21D1")

    label("loc_1F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1F96")

    ChrTalk(    #84
        0xFE,
        "And so, another day begins.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Today, too, we must bring enlightenment\x01",
            "to the masses...one mass at a time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_1F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_201F")

    ChrTalk(    #86
        0xFE,
        (
            "What could Sister Ellen possibly\x01",
            "be doing all this time?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "She left for the Erbe Scenic Route,\x01",
            "and has yet to return!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_201F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_21D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2098")

    ChrTalk(    #88
        0xFE,
        (
            "A new sister just joined us here. She\x01",
            "is currently out gathering grasses and\x01",
            "herbs for us, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D1")

    label("loc_2098")

    OP_A2(0x2)

    ChrTalk(    #89
        0xFE,
        (
            "I hope Sister May is doing well\x01",
            "in Rolent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Although I practice religious duties the same\x01",
            "as anyone else in my position, I am also in\x01",
            "charge of instructing the newly-cloistered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "And our ranks HAVE been bolstered recently, but\x01",
            "the new sister is currently out gathering grasses\x01",
            "and herbs for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D1")

    TalkEnd(0xFE)
    Return()

    # Function_9_184D end

    def Function_10_21D5(): pass

    label("Function_10_21D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2258")

    ChrTalk(    #92
        0xFE,
        (
            "I'm so grateful that the Birthday\x01",
            "Celebration is a success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Praise be to Aidios and her\x01",
            "protective embrace!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_2258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_22C8")

    ChrTalk(    #94
        0xFE,
        (
            "The soldiers seem to have gotten\x01",
            "themselves in a frenzy about\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "What's happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_22C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_25C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23DA")

    ChrTalk(    #96
        0xFE,
        (
            "Each goodbye is a new hello in waiting,\x01",
            "and this rule shall remain steadfast\x01",
            "throughout each of our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Life moves ever forward, pulled by threads we\x01",
            "call destiny. There is no beginning, no middle\x01",
            "and no end; there is only the human condition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C2")

    label("loc_23DA")

    OP_A2(0x1)

    ChrTalk(    #98
        0xFE,
        (
            "For every meeting, there\x01",
            "must also be a parting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Each goodbye is a new hello in waiting,\x01",
            "and this rule shall remain steadfast\x01",
            "throughout each of our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Life moves ever forward, pulled by threads we\x01",
            "call destiny. There is no beginning, no middle\x01",
            "and no end; there is only the human condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "There is no way we, as men and women,\x01",
            "can fully conceive of this universe\x01",
            "within which we dwell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "That is something only the Goddess,\x01",
            "Aidios, can properly envision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C2")

    Jump("loc_2E26")

    label("loc_25C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_267A")

    ChrTalk(    #103
        0xFE,
        (
            "This year, we celebrate the \x01",
            "1120th year of the Grancel\x01",
            "Cathedral's history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "This place of worship was founded \x01",
            "alongside the royal bloodline of\x01",
            "Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_267A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_271D")

    ChrTalk(    #105
        0xFE,
        (
            "Like your Bracer Guild, the Septian Church\x01",
            "has smaller branches all across this land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Naturally, this cathedral is\x01",
            "only one of those branches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_271D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_298B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_282E")

    ChrTalk(    #107
        0xFE,
        (
            "It is said the survivors of the Great Collapse\x01",
            "struggled with such intensity that the energy\x01",
            "of their lives shone from within their bodies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Perhaps the Great Collapse was but a\x01",
            "trial from Aidios, sent down from on\x01",
            "high to alter our perspectives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2988")

    label("loc_282E")

    OP_A2(0x1)

    ChrTalk(    #109
        0xFE,
        (
            "After the Great Collapse, mankind\x01",
            "lived on and persevered through a\x01",
            "period known as the Dark Age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Life was difficult, but it's said the light\x01",
            "of their struggles shone from within the \x01",
            "bodies of every man, woman and child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Perhaps the Great Collapse was but a\x01",
            "trial from Aidios, sent down from on\x01",
            "high to alter our perspectives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2988")

    Jump("loc_2E26")

    label("loc_298B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2AEB")

    ChrTalk(    #112
        0xFE,
        (
            "For every summer, a winter.\x01",
            "For every noon, a midnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "The cycle from seed to harvest\x01",
            "is a wheel, turning without\x01",
            "beginning or end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "After the Great Collapse, all men\x01",
            "and women struggled to survive,\x01",
            "balancing themselves on this wheel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I believe that with each turn,\x01",
            "the world as a whole becomes a\x01",
            "better place for us all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_2AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2B9C")

    ChrTalk(    #116
        0xFE,
        (
            "In the beginning, the world was\x01",
            "a formless, shapeless void. There\x01",
            "was only darkness and bitter wind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "And unto this void, the Goddess,\x01",
            "Aidios, brought light.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_2B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_2D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C42")

    ChrTalk(    #118
        0xFE,
        (
            "I understand you lent aid to our\x01",
            "Sister Ellen yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Many thanks to thee. May your\x01",
            "road always be alight with the\x01",
            "blessings of Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D8D")

    label("loc_2C42")

    OP_A2(0x1)

    ChrTalk(    #120
        0xFE,
        "Ah, greetings. I see you're bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I understand you lent aid to our\x01",
            "Sister Ellen yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "She went out to gather herbs, and we hadn't\x01",
            "heard from her for an inordinately long time.\x01",
            "I was beginning to get quite concerned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Many thanks to thee. May your\x01",
            "road always be alight with the\x01",
            "blessings of Aidios.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8D")

    Jump("loc_2E26")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_2DD3")

    ChrTalk(    #124
        0xFE,
        (
            "The city's become quite a lively\x01",
            "place, has it not?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E26")

    label("loc_2DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2E26")

    ChrTalk(    #125
        0xFE,
        (
            "Welcome to our local cathedral,\x01",
            "where the Septian faith is kept\x01",
            "alive.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E26")

    TalkEnd(0xFE)
    Return()

    # Function_10_21D5 end

    def Function_11_2E2A(): pass

    label("Function_11_2E2A")

    Call(0, 12)
    Return()

    # Function_11_2E2A end

    def Function_12_2E2F(): pass

    label("Function_12_2E2F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3581")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 71280, 4000, 4900, 0)
    SetChrPos(0x102, 72450, 4000, 4890, 0)
    SetChrPos(0x108, 71610, 4000, 4030, 0)
    TurnDirection(0x8, 0x108, 0)
    OP_A2(0x64F)
    OP_28(0x4B, 0x1, 0x400)
    OP_6D(71530, 4000, 5910, 0)
    OP_0D()

    ChrTalk(    #126
        0x8,
        "And who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#000FWe're, um...members, uh...of\x01",
            "the bracers. The Bracer Guild,\x01",
            "I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        (
            "#010FWe were looking for a Sister\x01",
            "Ellen...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        "Were you, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "Might I guess that you share\x01",
            "complicity with her, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #131
        0x101,
        "#004FWith a nun? Ew! No!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        (
            "#015FHe's asking if we know her\x01",
            "real identity, Estelle.\x02\x03",

            "#012FWe're here with information\x01",
            "she asked us to find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "I'm sorry to say she's no\x01",
            "longer at the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "She came to say goodbye to \x01",
            "me this morning, and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#580FWhere to? I mean, do you know\x01",
            "where she might have gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        "If only I did!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "I've been close with the royal family\x01",
            "for many years, and she's always regarded\x01",
            "me as a friend and confidant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "...but this time, she refused\x01",
            "to give me any details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "She no doubt wished to keep the church\x01",
            "from getting too deeply involved in...\x01",
            "whatever is occurring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        "#013FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        "I wouldn't worry, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "She had the light of hope in her\x01",
            "eyes as she departed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "I'm confident she was not running\x01",
            "away to wallow in despair, but for\x01",
            "a more noble cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#007FWell, that's good, at least.\x02\x03",

            "#505FBut the thing is, we kind of \x01",
            "need her to stay in touch with\x01",
            "the Royal Guardsmen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x108,
        (
            "#072FWell, begging for rain in the\x01",
            "desert only gets you sand. We\x01",
            "should probably go.\x02\x03",

            "#074FThe best thing we can do is\x01",
            "covertly keep an eye out for\x01",
            "other Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#012FNot the most efficient plan, but\x01",
            "that seems to be all we've got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "You seem to be...between a rock\x01",
            "and a hard place, as they say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "Always remember that Aidios helps those who\x01",
            "help themselves. Do all that you can, and\x01",
            "Aidios will surely take care of the rest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x8,
        (
            "Hard and honest work will always\x01",
            "lead you down the right path.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3574():
        OP_8C(0x8, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3574)
    EventEnd(0x0)
    Jump("loc_458D")

    label("loc_3581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_37D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3646")

    ChrTalk(    #150
        0x8,
        (
            "A common saying in our modern post-\x01",
            "revolutionary orbal society, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "How fascinating that the wisdom of\x01",
            "Zemuria has taken on such a form,\x01",
            "and survived all these years...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D5")

    label("loc_3646")

    OP_A2(0x0)

    ChrTalk(    #152
        0x8,
        (
            "Hard and honest work will always lead you down\x01",
            "the right path. A common saying in our modern\x01",
            "post-revolutionary orbal society, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "How fascinating that the wisdom of\x01",
            "Zemuria has taken on such a form,\x01",
            "and survived all these years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "All we can do is watch over you, and\x01",
            "pray. We cannot involve ourselves in\x01",
            "your struggle beyond that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#505F...Uhh... What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D5")

    Jump("loc_458D")

    label("loc_37D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_387F")

    ChrTalk(    #156
        0x8,
        (
            "You have a certain fire in your\x01",
            "eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "If there is a place you must\x01",
            "go, then I suggest you go\x01",
            "there immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        "Aidios will guide your way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_387F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_3952")

    ChrTalk(    #159
        0x8,
        (
            "Always remember that Aidios helps those who\x01",
            "help themselves. Do all that you can, and\x01",
            "Aidios will surely take care of the rest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "Hard and honest work will always\x01",
            "lead you down the right path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_3952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_3A0B")

    ChrTalk(    #161
        0x8,
        "So, the tournament is over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "I don't know what will happen with the Birthday\x01",
            "Celebration, but we'd best prepare for an influx\x01",
            "of people, if only as a precaution...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_3A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3AA3")

    ChrTalk(    #163
        0x8,
        (
            "I have yet to see Princess Klaudia\x01",
            "even a single time this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "I imagine Her Majesty's illness\x01",
            "must be keeping her busy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BB2")

    label("loc_3AA3")

    OP_A2(0x0)

    ChrTalk(    #165
        0x8,
        (
            "Actually, the princess does typically\x01",
            "come for a visit around this time of\x01",
            "year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "...to say a prayer for Her Majesty's\x01",
            "birthday, as you might imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        "But this year, I've yet to see her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "I imagine Her Majesty's illness\x01",
            "must be keeping her busy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB2")

    Jump("loc_458D")

    label("loc_3BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3C50")

    ChrTalk(    #169
        0x8,
        (
            "It seems the Royal Army plans\x01",
            "to patrol all major establish-\x01",
            "ments in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "The Royal Army came by earlier,\x01",
            "with a message.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D1C")

    label("loc_3C50")

    OP_A2(0x0)

    ChrTalk(    #171
        0x8,
        (
            "They announced they would be\x01",
            "'enforcing stricter security\x01",
            "measures.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x8,
        (
            "It seems they intend to patrol\x01",
            "all major establishments in the\x01",
            "city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "The Royal Army came by earlier,\x01",
            "with a message.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D1C")

    Jump("loc_458D")

    label("loc_3D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D91")

    ChrTalk(    #174
        0x8,
        (
            "We've formed a rather nice relationship\x01",
            "with the Liberl royal family over these\x01",
            "many years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2D")

    label("loc_3D91")

    OP_A2(0x0)

    ChrTalk(    #175
        0x8,
        (
            "After the Hundred Days War it\x01",
            "was the church and the bracers\x01",
            "who mediated and restored peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "I firmly believe in the mutual\x01",
            "separation of church and state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "That being said, however, I also believe that\x01",
            "singular instances of...tacit cooperation...can\x01",
            "help bring about a favorable outcome for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "We've formed a rather nice relationship\x01",
            "with the Liberl royal family over these\x01",
            "many years.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2D")

    Jump("loc_458D")

    label("loc_3F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4005")

    ChrTalk(    #179
        0x8,
        (
            "The Septian Church and the Liberl royal\x01",
            "family are very much in league with one\x01",
            "another to maintain peace and order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        (
            "We've cooperated with one another's\x01",
            "efforts for over 1000 years now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4123")

    label("loc_4005")

    OP_A2(0x0)

    ChrTalk(    #181
        0x8,
        (
            "The Septian Church and the Liberl royal\x01",
            "family are very much in league with one\x01",
            "another to maintain peace and order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "We've cooperated with one another's\x01",
            "efforts for over 1000 years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "Of course, it is a friendship\x01",
            "I seek with Queen Alicia, not\x01",
            "a political alliance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4123")

    Jump("loc_458D")

    label("loc_4126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_42D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_41BB")

    ChrTalk(    #184
        0x8,
        (
            "This cathedral has been active\x01",
            "ever since the Dark Age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        (
            "I daresay it is the oldest church\x01",
            "building in the entire kingdom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D1")

    label("loc_41BB")

    OP_A2(0x0)

    ChrTalk(    #186
        0x8,
        (
            "Since the Dark Age following the Great Collapse,\x01",
            "it's fallen upon the Septian Church to help\x01",
            "illuminate the road to peace and prosperity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "This cathedral has been active\x01",
            "ever since the Dark Age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "I daresay it is the oldest church\x01",
            "building in the entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42D1")

    Jump("loc_458D")

    label("loc_42D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_438C")

    ChrTalk(    #189
        0x8,
        (
            "Duke Dunan feels that the Martial Arts\x01",
            "Competition serves to bring passion to\x01",
            "the people as a whole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x8,
        (
            "And indeed, on one level, it\x01",
            "certainly does achieve that\x01",
            "goal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_438C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_458D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_444F")

    ChrTalk(    #191
        0x8,
        (
            "No one in the castle seems to\x01",
            "know any specifics about Her\x01",
            "Majesty's illness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "The head maid, Hilda, requested\x01",
            "an audience, but was turned away\x01",
            "by a man in black armor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_458D")

    label("loc_444F")

    OP_A2(0x0)

    ChrTalk(    #193
        0x8,
        (
            "I thought perhaps I could take the\x01",
            "initiative and fund the mixing of a\x01",
            "medicine for Her Majesty's ailment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x8,
        (
            "...but not a soul seems to know her\x01",
            "symptoms. No one has been told, and\x01",
            "no one is allowed audience. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        (
            "The head maid, Hilda, requested\x01",
            "an audience, but was turned away\x01",
            "by a man in black armor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_458D")

    TalkEnd(0x8)
    Return()

    # Function_12_2E2F end

    def Function_13_4591(): pass

    label("Function_13_4591")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #196
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_4591 end

    SaveToFile()

Try(main)
