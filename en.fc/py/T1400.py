from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1400   ._SN',
        MapName             = 'Bose',
        Location            = 'T1400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Sentry',                               # 9
        'Sentry',                               # 10
        'Carlos',                               # 11
        'Carlos',                               # 12
        'Blond-Haired Man',                     # 13
        'General Morgan',                       # 14
        'Anelace',                              # 15
        'Royal Army Soldier',                   # 16
        'Royal Army Soldier',                   # 17
        'Target Camera',                        # 18
        'Eisen Road',                           # 19
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH00030 ._CH',             # 02
        'ED6_DT07/CH02080 ._CH',             # 03
        'ED6_DT07/CH01630 ._CH',             # 04
        'ED6_DT07/CH01650 ._CH',             # 05
        'ED6_DT06/CH20045 ._CH',             # 06
        'ED6_DT06/CH20039 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH00030P._CP',             # 02
        'ED6_DT07/CH02080P._CP',             # 03
        'ED6_DT07/CH01630P._CP',             # 04
        'ED6_DT07/CH01650P._CP',             # 05
        'ED6_DT06/CH20045P._CP',             # 06
        'ED6_DT06/CH20039P._CP',             # 07
    )

    DeclNpc(
        X                   = 8250,
        Z                   = 0,
        Y                   = -12000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2400,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2100,
        Z                   = 0,
        Y                   = -20100,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = -7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 19250,
        Z                   = 0,
        Y                   = 14430,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 209710,
        Z                   = 0,
        Y                   = 11740,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10600,
        Z                   = 0,
        Y                   = -29900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 9000,
        Z                   = 11750,
        Y                   = 3000,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 11890,
        Z                   = 40,
        Y                   = -60460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 8810,
        Y                   = -1000,
        Z                   = -12035,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 3830,
        Y                   = -1000,
        Z                   = -43570,
        Range               = 10270,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF5880,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_34F",          # 01, 1
        "Function_2_393",          # 02, 2
        "Function_3_3A9",          # 03, 3
        "Function_4_3CD",          # 04, 4
        "Function_5_3F1",          # 05, 5
        "Function_6_72E",          # 06, 6
        "Function_7_106B",         # 07, 7
        "Function_8_14A4",         # 08, 8
        "Function_9_1BF0",         # 09, 9
        "Function_10_1E24",        # 0A, 10
        "Function_11_2393",        # 0B, 11
        "Function_12_2711",        # 0C, 12
        "Function_13_2C6E",        # 0D, 13
        "Function_14_32E3",        # 0E, 14
        "Function_15_3746",        # 0F, 15
        "Function_16_3776",        # 10, 16
        "Function_17_37AB",        # 11, 17
        "Function_18_37E0",        # 12, 18
        "Function_19_380E",        # 13, 19
        "Function_20_39F5",        # 14, 20
        "Function_21_5142",        # 15, 21
        "Function_22_5197",        # 16, 22
        "Function_23_51EC",        # 17, 23
        "Function_24_523C",        # 18, 24
        "Function_25_5262",        # 19, 25
        "Function_26_527E",        # 1A, 26
        "Function_27_529F",        # 1B, 27
        "Function_28_52EC",        # 1C, 28
        "Function_29_5367",        # 1D, 29
        "Function_30_5388",        # 1E, 30
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2B4")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrPos(0x8, 8230, 0, -10540, 270)
    Jump("loc_30A")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2CF")
    SetChrPos(0x8, 8230, 0, -10540, 270)
    Jump("loc_30A")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2D9")
    Jump("loc_30A")

    label("loc_2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_END)), "loc_2E8")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_30A")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2F2")
    Jump("loc_30A")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_END)), "loc_30A")
    SetChrPos(0x8, 8300, 0, -10500, 180)

    label("loc_30A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_31D")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 14)

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_330")
    SetMapFlags(0x10000000)
    OP_A3(0x3FB)
    Event(0, 20)

    label("loc_330")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_33C"),
        (SWITCH_DEFAULT, "loc_34E"),
    )


    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B")
    OP_A2(0x30D)
    Event(0, 13)

    label("loc_34B")

    Jump("loc_34E")

    label("loc_34E")

    Return()

    # Function_0_28A end

    def Function_1_34F(): pass

    label("Function_1_34F")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFE0430, 0x30045)
    OP_6F(0x3, 0)
    OP_72(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_377")
    Jump("loc_392")

    label("loc_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_386")
    Jump("loc_392")

    label("loc_386")

    OP_6F(0x1, 0)
    OP_72(0x1, 0x10)

    label("loc_392")

    Return()

    # Function_1_34F end

    def Function_2_393(): pass

    label("Function_2_393")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_393")

    label("loc_3A8")

    Return()

    # Function_2_393 end

    def Function_3_3A9(): pass

    label("Function_3_3A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CC")
    OP_8D(0xFE, -7000, -13000, 3500, -25300, 2000)
    Jump("Function_3_3A9")

    label("loc_3CC")

    Return()

    # Function_3_3A9 end

    def Function_4_3CD(): pass

    label("Function_4_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F0")
    OP_8D(0xFE, -15100, -32400, -9800, -27500, 2000)
    Jump("Function_4_3CD")

    label("loc_3F0")

    Return()

    # Function_4_3CD end

    def Function_5_3F1(): pass

    label("Function_5_3F1")

    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "④Arrived at Haken Gate.\x01",                    # 0
            "③Met Maybelle.\x01",                             # 1
            "⑥Met with General Morgan.\x01",                  # 2
            "⑧Decided to head to Ravennue Village.\x01",      # 3
            "⑬Released from Royal Army custody.\x01",         # 4
            "⑭Decided to head to inn by lakeside.\x01",       # 5
            "Exposed.\x01",                                    # 6
            "Do nothing.\x01",                                 # 7
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_503"),
        (1, "loc_556"),
        (2, "loc_57C"),
        (3, "loc_5B9"),
        (4, "loc_60B"),
        (5, "loc_669"),
        (6, "loc_6CC"),
        (SWITCH_DEFAULT, "loc_712"),
    )


    label("loc_503")

    OP_A2(0x219)
    OP_A2(0x202)
    OP_A2(0x203)
    OP_A2(0x205)
    OP_A2(0x207)
    OP_A2(0x217)
    OP_A2(0x206)
    OP_A2(0x212)
    OP_A2(0x213)
    OP_A2(0x239)
    OP_A2(0x24F)
    OP_A2(0x259)
    OP_A2(0x261)
    OP_A2(0x301)
    OP_A2(0x30C)

    ChrTalk(    #0
        0x101,
        "#000F④Arrived at Haken Gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_556")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)

    ChrTalk(    #1
        0x101,
        "#000F③Met Maybelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_57C")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x313)

    ChrTalk(    #2
        0x101,
        "#000F⑥Met with General Morgan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_5B9")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x314)
    OP_A2(0x317)
    OP_A2(0x318)
    OP_A2(0x313)

    ChrTalk(    #3
        0x101,
        "#000F⑧Decided to head to Ravennue Village.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_60B")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x314)
    OP_A2(0x317)
    OP_A2(0x318)
    OP_A2(0x31B)
    OP_A2(0x31C)
    OP_A2(0x31D)
    OP_A2(0x31E)
    OP_A2(0x32B)
    OP_A2(0x313)

    ChrTalk(    #4
        0x101,
        "#000F⑬Released from Royal Army custody.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_669")

    OP_A2(0x301)
    OP_A2(0x30A)
    OP_A2(0x30B)
    OP_A2(0x30C)
    OP_A2(0x310)
    OP_A2(0x312)
    OP_A2(0x314)
    OP_A2(0x317)
    OP_A2(0x318)
    OP_A2(0x31B)
    OP_A2(0x31C)
    OP_A2(0x31D)
    OP_A2(0x31E)
    OP_A2(0x32B)
    OP_A2(0x33A)
    OP_A2(0x313)

    ChrTalk(    #5
        0x101,
        "#000F⑭Decided to head to inn by lakeside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_6CC")

    OP_A3(0x301)
    OP_A3(0x30A)
    OP_A3(0x30B)
    OP_A3(0x30C)
    OP_A3(0x310)
    OP_A3(0x312)
    OP_A3(0x314)
    OP_A3(0x317)
    OP_A3(0x318)
    OP_A3(0x31B)
    OP_A3(0x31C)
    OP_A3(0x31D)
    OP_A3(0x31E)
    OP_A3(0x32B)
    OP_A3(0x33A)
    OP_A3(0x313)

    ChrTalk(    #6
        0x101,
        "#000FExposed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_728")

    label("loc_712")


    ChrTalk(    #7
        0x101,
        "#000FDo nothing.\x02",
    )

    CloseMessageWindow()

    label("loc_728")

    OP_5F(0x0)
    EventEnd(0x0)
    Return()

    # Function_5_3F1 end

    def Function_6_72E(): pass

    label("Function_6_72E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(    #8
        0xFE,
        "Huh? Aren't you those bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Do you have some business\x01",
            "with the general?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_7EF")

    ChrTalk(    #10
        0xFE,
        (
            "Do you have some business\x01",
            "with the general?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "He's indisposed at the moment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_7EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_843")

    ChrTalk(    #12
        0xFE,
        "Hi there, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Do you have some business\x01",
            "with the general?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(    #14
        0xFE,
        "Huh? Aren't you those bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Please don't hold it against me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "But after getting my ear yelled\x01",
            "off by the general I can't let\x01",
            "you through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_96D")

    ChrTalk(    #17
        0xFE,
        "Please don't hold it against me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "But after getting my ear yelled\x01",
            "off by the general I can't let\x01",
            "you through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_A14")

    ChrTalk(    #19
        0xFE,
        (
            "The general's office is at the\x01",
            "end of the hallway on the left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Make sure you don't go wandering\x01",
            "around in other places where\x01",
            "you're not permitted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1067")

    label("loc_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE7")
    EventBegin(0x0)
    OP_A2(0x30E)
    OP_69(0x8, 0x3E8)

    ChrTalk(    #21
        0x8,
        (
            "How in the world did you guys get\x01",
            "through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "The barricade hasn't been lifted\x01",
            "on the Eisen Road yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#010FWe came here on an errand for\x01",
            "Mayor Maybelle from Bose.\x02\x03",

            "Do you think you could get us\x01",
            "in to see General Morgan?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05Joshua explained what the mayor requested without disclosing his identity.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #25
        0x8,
        "#6PWell, that's understandable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "In that case, I could definitely get you\x01",
            "in to see the general, but unfortunately\x01",
            "he's out at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#6PHe's actually spearheading a number\x01",
            "of searches right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#020FIt looks like our timing was bad...\x02\x03",

            "You don't happen to have an idea\x01",
            "when he might return, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#6PI think he'll be back sometime\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "There's a bar in that rest stop\x01",
            "over there, so why don't you\x01",
            "wait there for him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#6PI'll let you know when he gets\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCF")

    ChrTalk(    #32
        0x101,
        (
            "#004FA bar in a rest stop...? Why is\x01",
            "there a bar in a place like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_DCF")


    ChrTalk(    #33
        0x101,
        (
            "#000FThe bar? You mean the place we\x01",
            "were just at? Why is there a bar\x01",
            "in a place like this, anyway?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E37")


    ChrTalk(    #34
        0x8,
        (
            "#6PObviously because this is the\x01",
            "border with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "The screening process for those entering and\x01",
            "leaving the country is really strict, so there are\x01",
            "a lot of travelers who have to wait quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010FThat makes a lot of sense. In that case,\x01",
            "it's understandable that you would need\x01",
            "facilities like an inn and a bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#020FWell then, we'll take you up on your\x01",
            "suggestion and wait over at the bar.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x100)
    EventEnd(0x1)
    Jump("loc_1067")

    label("loc_FE7")


    ChrTalk(    #38
        0x8,
        (
            "There's a bar in that rest stop\x01",
            "over there, so why don't you\x01",
            "wait there for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        "I'll let you know when he gets back.\x02",
    )

    CloseMessageWindow()

    label("loc_1067")

    TalkEnd(0x8)
    Return()

    # Function_6_72E end

    def Function_7_106B(): pass

    label("Function_7_106B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_10E4")

    ChrTalk(    #40
        0xFE,
        "Welcome to the Haken Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "With the sky bandits in custody,\x01",
            "our red alert status will be changed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A0")

    label("loc_10E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1184")

    ChrTalk(    #42
        0xFE,
        (
            "With the sky bandits in custody,\x01",
            "our red alert status will be changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "The border garrison is conducting\x01",
            "a full-scale search at the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A0")

    label("loc_1184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_12B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1290")
    OP_A2(0x0)

    ChrTalk(    #44
        0xFE,
        "Welcome to the Haken Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Huh? Weren't you the bracers\x01",
            "who were tossed into prison\x01",
            "not that long ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#509FWhy do you gotta make me\x01",
            "remember all the bad things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Ha ha. Well, at least you were\x01",
            "cleared of any wrongdoing, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B0")

    label("loc_1290")


    ChrTalk(    #48
        0xFE,
        "Welcome to the Haken Gate!\x02",
    )

    CloseMessageWindow()

    label("loc_12B0")

    Jump("loc_14A0")

    label("loc_12B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1306")

    ChrTalk(    #49
        0xFE,
        (
            "Welcome to the Haken Gate!\x01",
            "Are you heading to the\x01",
            "Erebonian Empire?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A0")

    label("loc_1306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1390")

    ChrTalk(    #50
        0xFE,
        (
            "I could hear the general yelling\x01",
            "all the way out here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "What in the world did you guys\x01",
            "do to piss him off like that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A0")

    label("loc_1390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1434")

    ChrTalk(    #52
        0xFE,
        (
            "The fort is on heightened alert\x01",
            "for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Therefore, I must ask you NOT to\x01",
            "walk around like you own the place.\x01",
            "It looks...suspicious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A0")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_14A0")

    ChrTalk(    #54
        0xFE,
        "Welcome to the Haken Gate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Hey, wait a minute! Did you come\x01",
            "here by way of the Eisen Road?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A0")

    TalkEnd(0x9)
    Return()

    # Function_7_106B end

    def Function_8_14A4(): pass

    label("Function_8_14A4")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1596")
    OP_A2(0x1)

    ChrTalk(    #56
        0xFE,
        (
            "I was finally able to get all the\x01",
            "paperwork done to leave this\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "But during my layover here I used all\x01",
            "my travel money eating and drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Ha ha. Then again, I've always\x01",
            "lived my life on a whim.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1642")

    label("loc_1596")


    ChrTalk(    #59
        0xFE,
        (
            "I was finally able to get all the\x01",
            "paperwork done to leave this\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Whether someone is happy in\x01",
            "life or not, it's all based on how\x01",
            "satisfied they are, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1642")

    Jump("loc_1BEC")

    label("loc_1645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_185C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C2")
    OP_A2(0x1)

    ChrTalk(    #61
        0xFE,
        (
            "Whether someone is happy in\x01",
            "life or not, it's all based on how\x01",
            "satisfied they are, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "As long as a person is satisfied that\x01",
            "it doesn't really matter what anybody\x01",
            "else says, that person is happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I want to live a life that changes\x01",
            "on a whim, so that's what I'm\x01",
            "going to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "And I'm not going to let anybody\x01",
            "give me crap about it either!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_17C2")


    ChrTalk(    #65
        0xFE,
        (
            "I want to live a life that changes\x01",
            "on a whim, so that's what I'm\x01",
            "going to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "And I'm not going to let anybody\x01",
            "give me crap about it either!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1859")

    Jump("loc_1BEC")

    label("loc_185C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1914")

    ChrTalk(    #67
        0xFE,
        (
            "Even if you try to live a serious\x01",
            "life, you're still going to have\x01",
            "your ups and downs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "That's why living a life on a whim\x01",
            "and taking it easy is the best way\x01",
            "to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEC")

    label("loc_1914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_19D6")

    ChrTalk(    #69
        0xFE,
        (
            "After the Hundred Days War ended,\x01",
            "not a lot of people have wanted\x01",
            "to travel to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I'm sure there are still a lot of\x01",
            "complex feelings for many\x01",
            "people here in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEC")

    label("loc_19D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3A")
    OP_A2(0x1)

    ChrTalk(    #71
        0xFE,
        (
            "I'm thinking about visiting the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Doesn't look like anyone's here to\x01",
            "fill out the necessary paperwork\x01",
            "for leaving the country, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Well, it doesn't really matter to\x01",
            "me, since I just live my life on\x01",
            "a whim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "In fact, the only reason I decided\x01",
            "to travel to the Empire is...well...\x01",
            "because it occurred to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEC")

    label("loc_1B3A")


    ChrTalk(    #75
        0xFE,
        (
            "Doesn't look like anyone's here to\x01",
            "fill out the necessary paperwork\x01",
            "for leaving the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Well, it doesn't really matter to\x01",
            "me, since I just live my life on\x01",
            "a whim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEC")

    TalkEnd(0xA)
    Return()

    # Function_8_14A4 end

    def Function_9_1BF0(): pass

    label("Function_9_1BF0")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1CAF")

    ChrTalk(    #77
        0xFE,
        (
            "Whew! I can't believe my first mission\x01",
            "was to storm the sky bandits' hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "But when you live your life as\x01",
            "spontaneously as I do, you can\x01",
            "experience a lot of things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E20")

    label("loc_1CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA9")
    OP_A2(0x1)

    ChrTalk(    #79
        0xFE,
        (
            "I had been thinking about traveling\x01",
            "to the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "But I ran out of money so I joined\x01",
            "the border garrison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "And why did I do that? Obviously\x01",
            "because I live my life on a whim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "I don't regret my choice either.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E20")

    label("loc_1DA9")


    ChrTalk(    #83
        0xFE,
        (
            "I had been thinking about traveling\x01",
            "to the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "But I ran out of money so I joined\x01",
            "the border garrison.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E20")

    TalkEnd(0xB)
    Return()

    # Function_9_1BF0 end

    def Function_10_1E24(): pass

    label("Function_10_1E24")

    TalkBegin(0xE)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217B")
    OP_A2(0x360)
    OP_A2(0x2)

    ChrTalk(    #85
        0xFE,
        (
            "#814FIsn't that you, Scherazard?\x02\x03",

            "#850FIt's nice to see you again. I haven't\x01",
            "seen you since the last time you\x01",
            "were here during your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x103,
        (
            "#020FIf it isn't Anelace. What are you\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "#810FWell, we had a request to\x01",
            "exterminate a monster in\x01",
            "this area.\x02\x03",

            "And with the barricade lifted on\x01",
            "the road, I was finally able to\x01",
            "complete my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        (
            "#020FOh really...?\x02\x03",

            "So how has your swordsmanship been\x01",
            "coming along? Have you started\x01",
            "mastering the use of that weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "#819FOh, please don't even ask.\x01",
            "I'm still working on that.\x02\x03",

            "#810FBy the way, Scherazard, are you\x01",
            "here on a job with the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#020FYeah, something like that. Although\x01",
            "the job is a little different from the\x01",
            "one you're handling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "#810FIs that so...\x02\x03",

            "Well, this region has become\x01",
            "more dangerous recently.\x02\x03",

            "Make sure to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238F")

    label("loc_217B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2307")
    OP_A2(0x2)

    ChrTalk(    #92
        0xFE,
        (
            "#810FOh, Scherazard...\x02\x03",

            "Are you really investigating the\x01",
            "whereabouts of the missing\x01",
            "airliner?\x02\x03",

            "#856FI'm sorry that you had to come\x01",
            "all the way out here since we\x01",
            "weren't up to the task.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        (
            "#020FWhy are you even apologizing?\x02\x03",

            "The only reason we're here is because the\x01",
            "incident has something to do with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "#814FI didn't know that.\x02\x03",

            "#810FAt any rate, be careful out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238F")

    label("loc_2307")


    ChrTalk(    #95
        0xFE,
        (
            "#856FThe bracers at the Bose branch\x01",
            "have been so busy recently.\x02\x03",

            "That's why we never got around\x01",
            "to the incident with the airliner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238F")

    TalkEnd(0xE)
    Return()

    # Function_10_1E24 end

    def Function_11_2393(): pass

    label("Function_11_2393")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2452")
    OP_A2(0x3)

    ChrTalk(    #96
        0xFE,
        (
            "We haven't seen a border garrison\x01",
            "force this size since the Hundred\x01",
            "Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I just hope the Empire doesn't\x01",
            "mistake it for an extensive\x01",
            "military operation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A5")

    label("loc_2452")


    ChrTalk(    #98
        0xFE,
        (
            "We haven't seen a border garrison\x01",
            "force this size since the Hundred\x01",
            "Days War.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A5")

    Jump("loc_270D")

    label("loc_24A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2560")

    ChrTalk(    #99
        0xFE,
        (
            "General Morgan said he plans\x01",
            "to change the way the search\x01",
            "is being conducted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "It seems as though he's going\x01",
            "to rely on the newly established\x01",
            "intelligence division.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_2560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2630")

    ChrTalk(    #101
        0xFE,
        (
            "It looks like we've hit a brick\x01",
            "wall in our search for the\x01",
            "sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "We've been using patrol ships to search\x01",
            "the northern mountainous regions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "But we still come up empty handed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_270D")

    label("loc_2630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_270D")

    ChrTalk(    #104
        0xFE,
        (
            "The border is always confronted\x01",
            "with threats from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Therefore we must be extremely\x01",
            "prudent in our actions, whatever\x01",
            "we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Otherwise, it could possibly give\x01",
            "them a pretext to invade again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270D")

    TalkEnd(0xF)
    Return()

    # Function_11_2393 end

    def Function_12_2711(): pass

    label("Function_12_2711")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2785")

    ChrTalk(    #107
        0xFE,
        (
            "It's beautiful weather today,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "There's a very clear view of\x01",
            "the Empire's territory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6A")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_293F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2884")
    OP_A2(0x4)

    ChrTalk(    #109
        0xFE,
        (
            "Thankfully it doesn't look like there\x01",
            "are any military movements\x01",
            "building on the Empire's side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I guess it's to be expected\x01",
            "since we've signed a mutual\x01",
            "nonaggression treaty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Even so, it's difficult to\x01",
            "relieve tensions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_293C")

    label("loc_2884")


    ChrTalk(    #112
        0xFE,
        (
            "Thankfully it doesn't look like there\x01",
            "are any military movements\x01",
            "building on the Empire's side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "I guess it's to be expected\x01",
            "since we've signed a mutual\x01",
            "nonaggression treaty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293C")

    Jump("loc_2C6A")

    label("loc_293F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AB2")
    OP_A2(0x4)

    ChrTalk(    #114
        0xFE,
        (
            "10 years ago, there used to\x01",
            "be a village called Hamel that\x01",
            "sat just beyond the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I've heard that it could even\x01",
            "be seen from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "It seems as though the village\x01",
            "completely vanished during\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "However, since the Liberl Army never invaded\x01",
            "the Empire's borders, I don't understand how\x01",
            "that could've happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B63")

    label("loc_2AB2")


    ChrTalk(    #118
        0xFE,
        (
            "10 years ago, there used to\x01",
            "be a village called Hamel that\x01",
            "sat just beyond the border.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "It seems as though the village\x01",
            "completely vanished during\x01",
            "the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B63")

    Jump("loc_2C6A")

    label("loc_2B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2C6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1C")
    OP_A2(0x4)

    ChrTalk(    #120
        0xFE,
        (
            "Because of what happened 10\x01",
            "years ago, all of the guards\x01",
            "here are very tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I hope we never have another\x01",
            "breach of this gate by the\x01",
            "Imperial Army...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6A")

    label("loc_2C1C")


    ChrTalk(    #122
        0xFE,
        (
            "I hope we never have another\x01",
            "breach of this gate by the\x01",
            "Imperial Army...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6A")

    TalkEnd(0x10)
    Return()

    # Function_12_2711 end

    def Function_13_2C6E(): pass

    label("Function_13_2C6E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 7940, 30, -38220, 0)
    SetChrPos(0x102, 6200, 0, -38720, 0)
    SetChrPos(0x103, 7430, 0, -40110, 0)
    OP_6D(14550, 11750, 700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5560, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x3D090, 0x0)
    FadeToBright(2000, 0)
    OP_6D(-8310, 11750, 800, 5000)
    Fade(1000)
    OP_6D(-440, 11200, -19210, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(6560, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_2D54():
        OP_6B(3250, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2D54)

    def lambda_2D64():
        OP_67(0, 8000, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D64)
    Sleep(3000)

    def lambda_2D81():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2D81)

    def lambda_2D91():
        OP_6D(7190, 50, -38190, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2D91)
    StopSound(0x9470, 0x186A0, 0x1B58)
    Sleep(6000)

    ChrTalk(    #123
        0x101,
        (
            "#004FTh-This is the Haken Gate...?\x02\x03",

            "It's freaking huge!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#020FOf course it's huge. It acts as the sole\x01",
            "entrance to the Empire and is the rampart\x01",
            "that protects Liberl from foreign threats.\x02\x03",

            "After it was destroyed in the war 10 years ago,\x01",
            "a much more robust wall was built in its place.\x01",
            "Standard military reaction: Bigger equals better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#000FWhich means that beyond this\x01",
            "point is no longer Liberl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#012FYeah...\x02\x03",

            "It's the territory of the Erebonian Empire\x01",
            "which stands beneath the emblem of\x01",
            "the golden stallion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#002FThe Erebonian Empire...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #129
        0x102,
        (
            "#010FWell, enough staring for one day.\x01",
            "Let's go meet with General Morgan.\x02\x03",

            "There are some barracks right\x01",
            "there to the side of the gate...\x01",
            "Maybe we'll find him in there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #130
        0x101,
        "#006FOkay, let's go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        (
            "#020FBefore that...\x02\x03",

            "I want you to remove those Bracer\x01",
            "Emblems you've got pinned on\x01",
            "your chests.\x02\x03",

            "Things won't be pretty if General\x01",
            "Morgan sees those.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #132
        0x101,
        "#6P#000FOh, I forgot all about that...\x02",
    )

    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #133
        "\x07\x05Estelle and Joshua reluctantly removed their bracer emblems.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #134
        0x101,
        "#6P#008FSomehow I feel all weird doing this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#010FYeah, there's something that just\x01",
            "doesn't feel right about this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x103,
        (
            "#021FDon't worry. That's proof that you've\x01",
            "started adjusting to being a bracer.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_13_2C6E end

    def Function_14_32E3(): pass

    label("Function_14_32E3")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-15040, 500, -25820, 0)
    OP_A2(0x310)
    SetChrPos(0x101, -14860, 500, -23500, 180)
    SetChrPos(0x103, -14860, 500, -23500, 180)
    SetChrPos(0x102, -14860, 500, -23500, 180)
    SetChrPos(0xC, -14860, 500, -23500, 180)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    Sleep(500)
    OP_70(0x0, 0x14)
    OP_73(0x0)
    SetChrPos(0x11, -15050, 500, -29150, 0)
    OP_43(0x103, 0x0, 0x0, 0xF)
    OP_43(0x102, 0x0, 0x0, 0x10)
    OP_43(0x101, 0x0, 0x0, 0x11)
    OP_43(0xC, 0x0, 0x0, 0x12)
    Sleep(2000)
    OP_6D(-10900, 0, -27570, 1500)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #137
        0x101,
        (
            "#509F#4PWhat are you following us\x01",
            "around for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        (
            "#025FYour timing is excellent. You didn't\x01",
            "miss a beat in exiting behind us. It\x01",
            "seemed almost natural. Scarily so...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #139
        0xC,
        "Blond-Haired Man",
        (
            "#035FHa! You noticed!\x02\x03",

            "Everything about you all just seemed\x01",
            "so interesting, I thought I'd take a\x01",
            "gander.\x02\x03",

            "#030FPlease, don't mind me. Carry on,\x01",
            "my good gent and mademoiselles!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #140
        0x101,
        "#005F#3S#4POf course we're going to mind!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8F(0x101, 0xFFFFD44A, 0x0, 0xFFFF92A0, 0xBB8, 0x0)

    ChrTalk(    #141
        0x101,
        "#009F#4PNow get, you! Shoo! Shoo!!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #142
        0xC,
        "Blond-Haired Man",
        "#034FScrooge.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 270, 400)
    OP_8E(0xC, 0xFFFFC568, 0x0, 0xFFFF93A4, 0x7D0, 0x0)
    OP_8E(0xC, 0xFFFFC5F4, 0x1F4, 0xFFFFA330, 0xBB8, 0x0)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 20)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    SetChrFlags(0xC, 0x80)
    Sleep(1000)

    ChrTalk(    #143
        0x102,
        (
            "#017FWho WAS that guy...?\x01",
            "Seriously, what was his deal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x103,
        "#020FHe's not normal, that's for sure.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #145
        0x101,
        (
            "#509FGetting rid of that weirdo was probably\x01",
            "better not only for ourselves, but a\x01",
            "service for the world at large, too!\x02\x03",

            "Now, let's hurry and meet with the\x01",
            "general!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_14_32E3 end

    def Function_15_3746(): pass

    label("Function_15_3746")

    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0xFFFF91EC, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_3746 end

    def Function_16_3776(): pass

    label("Function_16_3776")

    Sleep(1000)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD878, 0x0, 0xFFFF8F80, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_3776 end

    def Function_17_37AB(): pass

    label("Function_17_37AB")

    Sleep(1800)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD7C4, 0x0, 0xFFFF9444, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_17_37AB end

    def Function_18_37E0(): pass

    label("Function_18_37E0")

    Sleep(3000)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF93A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFCE1E, 0x0, 0xFFFF9156, 0xBB8, 0x0)
    Return()

    # Function_18_37E0 end

    def Function_19_380E(): pass

    label("Function_19_380E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39F4")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0x8, 255)

    def lambda_382B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_382B)

    def lambda_3839():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3839)

    def lambda_3847():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3847)

    def lambda_3855():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3855)
    OP_69(0x8, 0x3E8)
    OP_A2(0x311)

    ChrTalk(    #146
        0x8,
        (
            "I could hear some arguing. Was\x01",
            "there some kind of problem with\x01",
            "another traveler?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        (
            "#008FN-No, nothing big like that.\x02\x03",

            "That aside...could you let us\x01",
            "meet with the general?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        "#6PYeah, he's inside.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x206C, 0x0, 0xFFFFD6FC, 0xBB8, 0x0)
    TurnDirection(0x8, 0x0, 400)
    ClearChrFlags(0x8, 0x4)

    ChrTalk(    #149
        0x8,
        (
            "His office is the last \x01",
            "door on the left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "Make sure you don't go wandering\x01",
            "around in other places where you're\x01",
            "not permitted.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 255)
    OP_71(0x1, 0x10)
    EventEnd(0x1)

    label("loc_39F4")

    Return()

    # Function_19_380E end

    def Function_20_39F5(): pass

    label("Function_20_39F5")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(6980, 0, -10700, 0)
    SetChrPos(0x101, 11000, 500, -11970, 0)
    SetChrPos(0x103, 11000, 500, -11970, 0)
    SetChrPos(0x102, 11000, 500, -11970, 0)
    SetChrPos(0xD, 11000, 500, -11970, 0)
    SetChrPos(0x8, 11000, 500, -11970, 0)
    SetChrPos(0x9, 11000, 500, -11970, 0)
    OP_4A(0xD, 255)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    Sleep(500)
    OP_70(0x1, 0x14)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x0, 0x0, 0x15)
    OP_43(0x103, 0x0, 0x0, 0x17)
    OP_43(0x102, 0x0, 0x0, 0x16)
    Sleep(1500)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    Sleep(300)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3B10():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3B10)
    OP_8E(0x8, 0x1F4A, 0x0, 0xFFFFD06C, 0xFA0, 0x0)
    OP_8E(0x8, 0x1BB2, 0x0, 0xFFFFD4A4, 0xFA0, 0x0)
    OP_8C(0x8, 270, 0)

    ChrTalk(    #151
        0x101,
        (
            "#009FJust what is your problem, old man?!\x01",
            "Trying to brush us off like bugs!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x80)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3BB2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_3BB2)
    OP_8E(0xD, 0x1F4A, 0x0, 0xFFFFD06C, 0xBB8, 0x0)

    ChrTalk(    #152
        0xD,
        (
            "#160F#4PHmph, you're no different.\x02\x03",

            "Hiding your identities so you could\x01",
            "try and finagle some information\x01",
            "out of me...\x02\x03",

            "It's because you pull underhanded\x01",
            "actions like that that bracers can't\x01",
            "be trusted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#005FJust where do you get off calling\x01",
            "it 'finagling'?!\x02\x03",

            "It's your own fault since you didn't\x01",
            "share information with the guild to\x01",
            "begin with!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xD,
        (
            "#162F#4PNonsense! Who in their right mind\x01",
            "would leave an incident this big in\x01",
            "the hands of a mere civilian group?!\x02\x03",

            "#163FI swear...of all the stupid things\x01",
            "Maybelle could have tried to pull...\x02\x03",

            "Hiring a bunch of kids like this\x01",
            "and getting in the way of our\x01",
            "search party...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #155
        0x103,
        (
            "#022FHow about you cut with the\x01",
            "crap, General?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3EA0():
        OP_6D(7800, 0, -10140, 1200)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3EA0)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 0)

    def lambda_3EC2():

        label("loc_3EC2")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3EC2")

    QueueWorkItem2(0x8, 2, lambda_3EC2)

    def lambda_3ED3():

        label("loc_3ED3")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3ED3")

    QueueWorkItem2(0x9, 2, lambda_3ED3)
    OP_8E(0x103, 0x1838, 0x0, 0xFFFFD01C, 0xBB8, 0x0)
    OP_44(0x8, 0x2)
    OP_44(0x9, 0x2)
    Sleep(400)

    ChrTalk(    #156
        0x103,
        (
            "#025F#1PWhy do you think we've had to\x01",
            "come all the way from Rolent\x01",
            "to begin with?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #157
        0x103,
        (
            "#024F#1P#3SIt's because when it comes down to it,\x01",
            "you military morons can't do your job!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #158
        0xD,
        "#161F#2PWhat did you just say?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#007F(Holy cow...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#017F(Schera's really pissed, all right...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x103,
        (
            "#022F#1PFor the past few months, you've known\x01",
            "about the string of burglaries which seem\x01",
            "to be the work of the sky bandits, right?\x02\x03",

            "And who, knowing full well it was them, dumped\x01",
            "the workload onto the guild instead of looking\x01",
            "into it themselves like they should have, huh?\x02\x03",

            "#026FAnd now, the second this incident happens,\x01",
            "you get on your high horse with an attitude...\x02\x03",

            "Yet you've got nothing to show for it!\x01",
            "No hostages or even the location of the\x01",
            "missing airliner.\x02\x03",

            "#027FDon't you think that's an embarrassment to\x01",
            "the entire kingdom?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0xD,
        "#162F#2P#3SSilence, girl!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #163
        0xD,
        (
            "#162F#2PThe military is an organization\x01",
            "that runs on discipline and does\x01",
            "not take action on a whim!\x02\x03",

            "Unlike a group I know of who didn't think\x01",
            "ahead and let the sky bandits escape,\x01",
            "so enough with your insolence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        (
            "#022F#1PSo you're really looking for a\x01",
            "fight, aren't you...?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 6)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, 0, 0, -5000, 135)
    OP_1F(0x46, 0x190)
    Sleep(400)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #165
        0xC,
        "Man's Voice",
        "How sad it is to see such discord.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)
    OP_1F(0x64, 0x190)
    OP_4A(0xC, 255)
    SetChrChipByIndex(0xC, 6)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    SetChrPos(0xC, 0, 0, -7024, 135)

    def lambda_44FA():
        OP_6D(3580, 0, -8410, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_44FA)

    def lambda_4512():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4512)

    def lambda_4522():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4522)

    def lambda_4530():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4530)

    def lambda_453E():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_453E)
    Sleep(500)

    def lambda_4551():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4551)

    def lambda_455F():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_455F)

    def lambda_456D():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_456D)
    Sleep(2000)

    ChrTalk(    #166
        0xC,
        (
            "#035FStrife brings nothing to be borne...but\x01",
            "only extends the barren wilderness\x01",
            "within our hearts.\x02\x03",

            "#030FLet me sing a requiem for you all,\x01",
            "one to soothe your parched souls.\x02\x03",

            "A gentle, yet wistful tune, to bathe\x01",
            "your brittle spirits and cause the\x01",
            "deserts of your hearts to bloom...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x103)
    OP_63(0x102)
    OP_63(0xD)
    OP_63(0x8)
    OP_63(0x9)
    Sleep(500)
    OP_1D(0x0)

    ChrTalk(    #999 op#A op#5
        0xC,
        "#035F#10A#0W...\x05\x02",
    )

    Sleep(1500)
    OP_4B(0xC, 255)
    CloseMessageWindow()
    Sleep(6270)

    ChrTalk(    #167 op#A op#5
        0xC,
        (
            "#100A#0WBrightly shooting stars,\x01",
            "leaving trails in the skies...\x05\x02",
        )
    )

    Sleep(6600)

    ChrTalk(    #168 op#A op#5
        0xC,
        (
            "#100A#0WLike a guiding light, they show\x01",
            "me the way to your eyes...\x05\x02",
        )
    )

    Sleep(6200)

    ChrTalk(    #169 op#A op#5
        0xC,
        (
            "#100A#0WThis yearning passion,\x01",
            "tears my heart in twain...\x05\x02",
        )
    )

    Sleep(5600)

    ChrTalk(    #170 op#A op#5
        0xC,
        (
            "#100A#0WAnd the cruel moon mocks\x01",
            "my pain...\x05\x02",
        )
    )

    Sleep(7000)

    ChrTalk(    #171 op#A op#5
        0xC,
        (
            "#100A#0WIf this fleeting dream shall\x01",
            "never be...\x05\x02",
        )
    )

    Sleep(7000)

    ChrTalk(    #172 op#A op#5
        0xC,
        (
            "#100A#0WA single wound will remain in\x01",
            "my heart for all to see...\x05\x02",
        )
    )

    Sleep(9500)

    ChrTalk(    #173 op#A op#5
        0xC,
        (
            "#100A#0WOur passionate first and final\x01",
            "kiss...\x05\x02",
        )
    )

    Sleep(8500)

    ChrTalk(    #174 op#A op#5
        0xC,
        (
            "#100A#0WYour tears to me are an\x01",
            "amber bliss...\x05\x02",
        )
    )

    Sleep(8800)

    ChrTalk(    #175 op#A op#5
        0xC,
        "#100A#0WLet us immure this eternal love...\x05\x02",
    )

    Sleep(10800)
    CloseMessageWindow()
    OP_21()
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    OP_4A(0xC, 255)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 7)
    SetChrSubChip(0xC, 0)
    OP_0D()
    OP_99(0xC, 0x0, 0x3, 0x5DC)
    Sleep(300)
    OP_99(0xC, 0x3, 0xA, 0x3E8)
    Sleep(500)

    ChrTalk(    #176
        0xC,
        (
            "#035FHa ha...it looks like you all understood\x01",
            "what I was trying to get across.\x02\x03",

            "What is it that is most precious\x01",
            "above all?\x02\x03",

            "#030FThat's love and peace, baby.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0xC, 0x12C, 1900, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    Sleep(500)

    ChrTalk(    #177
        0xD,
        "#163F#2P*cough*...\x02",
    )

    CloseMessageWindow()

    def lambda_4B21():
        OP_6D(6980, 0, -10700, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4B21)

    def lambda_4B39():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4B39)
    Sleep(1500)
    OP_1D(0x10)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 2)
    TurnDirection(0xD, 0x9, 400)
    OP_63(0xC)

    ChrTalk(    #178
        0xD,
        (
            "#160F#4PI-I think it's about time for the\x01",
            "search party to be returning\x01",
            "with their reports.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BC4():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BC4)

    def lambda_4BD2():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BD2)

    def lambda_4BE0():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BE0)

    def lambda_4BEE():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BEE)

    def lambda_4BFC():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BFC)

    ChrTalk(    #179
        0x9,
        "Th-That's right, General!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xD,
        (
            "#160F#4PI should get back to my duties.\x01",
            "And make sure you don't let\x01",
            "those kids in again.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    OP_8E(0xD, 0x2544, 0x1F4, 0xFFFFD148, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #181
        0xD,
        (
            "#163F#6POh...and cancel any further checks on\x01",
            "the travelers along the Eisen Road.\x02\x03",

            "Having these kids around any longer\x01",
            "will just be an eyesore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        "#5PRight away, sir!\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x1C)
    OP_43(0x8, 0x1, 0x0, 0x1D)

    def lambda_4D63():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_4D63)
    OP_8E(0xD, 0x2AF8, 0x1F4, 0xFFFFD13E, 0x7D0, 0x0)
    SetChrFlags(0xD, 0x80)
    Sleep(1000)

    ChrTalk(    #183
        0x101,
        "#509F(He ran away...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x102,
        (
            "#017F(I wish WE could escape...\x01",
            "He's still right behind us, isn't he?)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DFA():
        OP_6D(4140, 0, -10880, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4DFA)

    def lambda_4E12():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_4E12)
    OP_8E(0xC, 0x960, 0x0, 0xFFFFD940, 0x7D0, 0x0)
    OP_8C(0xC, 135, 400)
    Sleep(500)

    ChrTalk(    #185
        0xC,
        (
            "#031FHa ha ha ha! No matter which\x01",
            "country you visit, military men\x01",
            "lack romanticism.\x02\x03",

            "But you lot, on the other hand,\x01",
            "appear to appreciate my aesthetic\x01",
            "sense.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #186
        0x101,
        (
            "#506F#6PY-You know, maybe we should\x01",
            "get going ourselves?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 45, 400)
    Sleep(300)

    ChrTalk(    #187
        0x102,
        (
            "#019F#5PY-Yeah, good idea.\x02\x03",

            "We had a bit of trouble, but we did\x01",
            "manage to get some information...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #188
        0x103,
        (
            "#021FAfter we head back to Bose,\x01",
            "how about we think about our\x01",
            "future plan of attack?\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x0, 0x18)
    OP_43(0x103, 0x0, 0x0, 0x1A)
    OP_43(0x102, 0x0, 0x0, 0x19)
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xC, 180, 400)

    ChrTalk(    #189
        0xC,
        (
            "#033FHmm...?\x02\x03",

            "Wh-Where are you going?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_90(0xC, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)

    ChrTalk(    #190
        0xC,
        (
            "#036F#5PW-Wait for me! I-I mean,\x01",
            "please wait for me!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5110():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5110)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x400000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_39F5 end

    def Function_21_5142(): pass

    label("Function_21_5142")

    Sleep(600)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_516F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_516F)
    OP_8E(0xFE, 0x1464, 0x0, 0xFFFFD314, 0x1770, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_21_5142 end

    def Function_22_5197(): pass

    label("Function_22_5197")

    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_51C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_51C4)
    OP_8E(0xFE, 0x125C, 0x0, 0xFFFFCD9C, 0x1770, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_22_5197 end

    def Function_23_51EC(): pass

    label("Function_23_51EC")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5214():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5214)
    OP_8E(0xFE, 0xEE2, 0x0, 0xFFFFD04E, 0x1770, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_23_51EC end

    def Function_24_523C(): pass

    label("Function_24_523C")

    Sleep(500)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xBB8, 0x0)
    Return()

    # Function_24_523C end

    def Function_25_5262(): pass

    label("Function_25_5262")

    OP_8C(0xFE, 180, 400)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xBB8, 0x0)
    Return()

    # Function_25_5262 end

    def Function_26_527E(): pass

    label("Function_26_527E")

    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0xBB8, 0x0)
    Return()

    # Function_26_527E end

    def Function_27_529F(): pass

    label("Function_27_529F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_52B0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_52B0)
    OP_8E(0xFE, 0x1F4A, 0x0, 0xFFFFD06C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C0C, 0x0, 0xFFFFCBD0, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_27_529F end

    def Function_28_52EC(): pass

    label("Function_28_52EC")

    Sleep(500)
    OP_8E(0xFE, 0x1F4A, 0x0, 0xFFFFD06C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x244A, 0x1F4, 0xFFFFD0EE, 0xFA0, 0x0)

    def lambda_531F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_531F)
    OP_8E(0xFE, 0x2AF8, 0x1F4, 0xFFFFD13E, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Sleep(500)
    OP_72(0x1, 0x800)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0x1, 20)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x800)
    Return()

    # Function_28_52EC end

    def Function_29_5367(): pass

    label("Function_29_5367")

    Sleep(3000)
    OP_8E(0xFE, 0x203A, 0x0, 0xFFFFD120, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_5367 end

    def Function_30_5388(): pass

    label("Function_30_5388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54E7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5450")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B4")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_53BB")

    label("loc_53B4")

    TurnDirection(0x103, 0x0, 400)

    label("loc_53BB")


    def lambda_53C1():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53C1)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #191
        0x103,
        (
            "#020FWe shouldn't go anywhere else\x01",
            "until the general returns.\x02\x03",

            "And while we're waiting, let's\x01",
            "make good use of the bar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54CC")

    label("loc_5450")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5466")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_546D")

    label("loc_5466")

    TurnDirection(0x103, 0x0, 400)

    label("loc_546D")


    def lambda_5473():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5473)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #192
        0x103,
        (
            "#020FWe shouldn't wander off. Let's\x01",
            "hurry and meet with the general.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54CC")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_54E7")

    Return()

    # Function_30_5388 end

    SaveToFile()

Try(main)
