from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4221   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Factory Chief Murdock',                # 9
        'Colonel Richard',                      # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Scherazard',                           # 13
        'Revol',                                # 14
        'Nage',                                 # 15
        'Tita',                                 # 16
        'Russell',                              # 17
        'Olivier',                              # 18
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02030 ._CH',             # 01
        'ED6_DT07/CH02460 ._CH',             # 02
        'ED6_DT07/CH02230 ._CH',             # 03
        'ED6_DT07/CH02240 ._CH',             # 04
        'ED6_DT07/CH02140 ._CH',             # 05
        'ED6_DT07/CH02470 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH01350 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH00060 ._CH',             # 0B
        'ED6_DT07/CH02020 ._CH',             # 0C
        'ED6_DT07/CH00030 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02030P._CP',             # 01
        'ED6_DT07/CH02460P._CP',             # 02
        'ED6_DT07/CH02230P._CP',             # 03
        'ED6_DT07/CH02240P._CP',             # 04
        'ED6_DT07/CH02140P._CP',             # 05
        'ED6_DT07/CH02470P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH01350P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH00060P._CP',             # 0B
        'ED6_DT07/CH02020P._CP',             # 0C
        'ED6_DT07/CH00030P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 141250,
        Z                   = 0,
        Y                   = 7610,
        Direction           = 278,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 78740,
        Z                   = 0,
        Y                   = -1880,
        Direction           = 194,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 83500,
        Z                   = 0,
        Y                   = -53540,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 86170,
        Z                   = 0,
        Y                   = -52670,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 139300,
        Z                   = 0,
        Y                   = 5970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 139320,
        TriggerZ            = 0,
        TriggerY            = 7540,
        TriggerRange        = 400,
        ActorX              = 141250,
        ActorZ              = 1500,
        ActorY              = 7610,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_454",          # 02, 2
        "Function_3_5D1",          # 03, 3
        "Function_4_11F5",         # 04, 4
        "Function_5_13EB",         # 05, 5
        "Function_6_14FC",         # 06, 6
        "Function_7_15ED",         # 07, 7
        "Function_8_1664",         # 08, 8
        "Function_9_1669",         # 09, 9
        "Function_10_18BA",        # 0A, 10
        "Function_11_223E",        # 0B, 11
        "Function_12_361B",        # 0C, 12
        "Function_13_366C",        # 0D, 13
        "Function_14_4B6F",        # 0E, 14
        "Function_15_5767",        # 0F, 15
        "Function_16_58C3",        # 10, 16
        "Function_17_592E",        # 11, 17
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_28C")
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_29A")
    OP_A3(0x3FB)
    Event(0, 14)

    label("loc_29A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_2AA"),
        (108, "loc_2C0"),
        (SWITCH_DEFAULT, "loc_2D6"),
    )


    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BD")
    OP_A2(0x646)
    Event(0, 13)

    label("loc_2BD")

    Jump("loc_2D6")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D3")
    OP_A2(0x670)
    Event(0, 15)

    label("loc_2D3")

    Jump("loc_2D6")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 38180, 0, -59720, 90)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    SetChrChipByIndex(0x0, 2)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_34C")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 37930, 0, 59370, 97)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_3F2")

    label("loc_34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_36B")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x55, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    ClearChrFlags(0x11, 0x80)

    label("loc_368")

    Jump("loc_3F2")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_390")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_3F2")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_3F2")

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_3D5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_3F2")

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_3F2")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)

    label("loc_3F2")

    Return()

    # Function_0_27E end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    OP_1B(0x0, 0x0, 0x10)
    OP_1B(0x6, 0x0, 0x11)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_413")
    Jump("loc_44A")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_41D")
    Jump("loc_44A")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_42B")
    OP_64(0x0, 0x1)
    Jump("loc_44A")

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_439")
    OP_64(0x0, 0x1)
    Jump("loc_44A")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_443")
    Jump("loc_44A")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_44A")

    label("loc_44A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3F3 end

    def Function_2_454(): pass

    label("Function_2_454")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_479")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5BB")

    label("loc_479")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5BB")

    label("loc_492")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5BB")

    label("loc_4AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5BB")

    label("loc_4C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5BB")

    label("loc_4DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5BB")

    label("loc_4F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5BB")

    label("loc_50F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_528")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5BB")

    label("loc_528")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5BB")

    label("loc_541")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5BB")

    label("loc_55A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5BB")

    label("loc_573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5BB")

    label("loc_58C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5BB")

    label("loc_5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5BB")

    label("loc_5D0")

    Return()

    # Function_2_454 end

    def Function_3_5D1(): pass

    label("Function_3_5D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x55, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_994")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 137920, 0, 6450, 90)
    SetChrPos(0x102, 137940, 0, 5220, 90)
    OP_8C(0x11, 270, 0)
    SetChrSubChip(0x11, 0)
    OP_6D(138940, 0, 6080, 1000)

    ChrTalk(    #0
        0x11,
        (
            "#4P#030FEstelle! Joshua!\x02\x03",

            "It is the Birthday Celebration!\x01",
            "What a waste it would be if we\x01",
            "were not to enjoy it, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#505F(Hey, Joshua... I think he's the guy!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#6P#015F(Without question.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#4P#033FI have it!\x02\x03",

            "Why don't you join me in a\x01",
            "little afternoon delight?\x02\x03",

            "#032FJust you...and you...and I.\x01",
            "Doesn't that sound...divine?\x02\x03",

            "#031FCome now. Do say yes.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(    #4
        0x101,
        (
            "#001FHeh, heh. Funny you asked.\x02\x03",

            "We were JUST talking to this guy, who asked us the\x01",
            "same thing, and we said, we have this friend whom\x01",
            "you would probably just LOVE to talk to...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x11,
        "#4P#033F#5SDid you really, now?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        "#4P#032FHonest to goodness?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#6P#019FAbsolutely. Would you like us\x01",
            "to introduce him to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#4P#030FI would most love that!\x02\x03",

            "#031FPlease, lead the way!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_11F1")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECB")
    OP_A2(0x6ED)

    ChrTalk(    #9
        0x101,
        "#004FOlivier...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#030FEstelle! Joshua!\x02\x03",

            "I heard from Cassius that you've\x01",
            "become full-class bracers. Well\x01",
            "done, well done!\x02\x03",

            "#031FCongratulations, my dear little\x01",
            "pussycats!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#007FCould you just...ugh. We'll just\x01",
            "go with 'thanks.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FOlivier, what brings you here?\x02\x03",

            "I'd heard you were invited to tonight's\x01",
            "celebratory banquet, but...well, I didn't\x01",
            "think you'd be here already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#580FYeah, seriously!\x02\x03",

            "What's a guy who loves parties\x01",
            "doing drinking alone in a quiet\x01",
            "place like this?!\x02\x03",

            "#005FBetter be careful, or some\x01",
            "people might start thinking\x01",
            "you're an imposter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#035FThe news of you two becoming\x01",
            "full-fledged bracers filled my \x01",
            "heart almost to bursting.\x02\x03",

            "...So much so that I saw no recourse\x01",
            "but to hold an impromptu concert in\x01",
            "front of the Grand Arena.\x02\x03",

            "Ah, if only you had witnessed\x01",
            "the unbridled excitement I\x01",
            "inspired in my legion of fans!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#509FUh...riiiight...  \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#018FMakes me think of the performance\x01",
            "at Haken Gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#030FIndeed! And such a public explosion of passion\x01",
            "left me drained, so I wandered here for a quiet\x01",
            "place to drink and brood.\x02\x03",

            "#035FAh, me... In restless dreams walking alone,\x01",
            "sharing the drink they call loneliness...\x02\x03",

            "Before you sits the beauty and\x01",
            "the beast that is...man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#017FI can't make those words fit together\x01",
            "into anything resembling sense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F1")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110F")
    OP_A2(0x6F6)

    ChrTalk(    #19
        0x101,
        (
            "#501FUh, so yeah. About your reunion\x01",
            "with my dad...\x02\x03",

            "You apparently have something you need\x01",
            "to talk about with him, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        "#033F...I do?...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#014FYou do.\x02\x03",

            "As a matter of fact, it seemed\x01",
            "to me as though Dad already\x01",
            "knew who you were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#036F...\x02\x03",

            "#031FInconceivable, my pretty kitty!\x01",
            "Hah, hah, haah!\x02\x03",

            "Surely a man like him and a man\x01",
            "such as I would have little need\x01",
            "to...spread our wings and...fly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#509F(Yeah, he DEFINITELY knows something.\x01",
            "He's acting weird, even for him!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#015F(Definitely. There's more to this\x01",
            "story, for sure.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F1")

    label("loc_110F")


    ChrTalk(    #25
        0x11,
        (
            "#035FPups! Forget about the worries on\x01",
            "your mind! Come! Dance! To the beat\x01",
            "of the rhythm of the night!\x02\x03",

            "Let the sounds of our feet and our laughter\x01",
            "chase away those lurking twin trolls,\x01",
            "Forgotten Past and Unknown Future!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F1")

    TalkEnd(0xFE)
    Return()

    # Function_3_5D1 end

    def Function_4_11F5(): pass

    label("Function_4_11F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(    #26
        0x10B,
        (
            "#100FAureole, huh... One of the\x01",
            "legendary Sept-Terrions...\x02\x03",

            "Someone had to have known its \x01",
            "location and told the colonel\x01",
            "without Her Majesty's knowledge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E7")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1305")

    ChrTalk(    #27
        0x10B,
        (
            "#100FThe colonel's coup d'etat may\x01",
            "be over, but there are still\x01",
            "too many loose ends.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E7")

    label("loc_1305")

    OP_A2(0x5)

    ChrTalk(    #28
        0x10B,
        (
            "#100FThe colonel's coup d'etat may\x01",
            "be over, but there are still\x01",
            "too many loose ends.\x02\x03",

            "...Like those ruins of an ancient\x01",
            "orbal civilization beneath the royal\x01",
            "castle...\x02\x03",

            "We must delve a bit deeper. We\x01",
            "must find answers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E7")

    TalkEnd(0xFE)
    Return()

    # Function_4_11F5 end

    def Function_5_13EB(): pass

    label("Function_5_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_1475")

    ChrTalk(    #29
        0x107,
        (
            "#060FGrandpa's had something important\x01",
            "on his mind for a little while now.\x02\x03",

            "I wonder when we'll be going home\x01",
            "to Zeiss...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FB")

    label("loc_1475")


    ChrTalk(    #30
        0x107,
        (
            "#060FThe food at the castle was amazing!\x02\x03",

            "I wasn't expecting that, for\x01",
            "some reason. I figured it'd be\x01",
            "bland, stuffy old cuisine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FB")

    Return()

    # Function_5_13EB end

    def Function_6_14FC(): pass

    label("Function_6_14FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_159A")

    ChrTalk(    #31
        0xC,
        (
            "#020FJoshua wasn't in his room?\x02\x03",

            "He's got to be somewhere in the\x01",
            "castle. If you look around, I'm\x01",
            "sure you'll find him!\x02\x03",

            "Good luck, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E9")

    label("loc_159A")


    ChrTalk(    #32
        0xC,
        (
            "#020FJoshua's room was next to your\x01",
            "dad's, I think.\x02\x03",

            "I hope you find him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E9")

    TalkEnd(0xFE)
    Return()

    # Function_6_14FC end

    def Function_7_15ED(): pass

    label("Function_7_15ED")

    TalkBegin(0xFE)

    ChrTalk(    #33
        0xFE,
        (
            "This is Professor Russell and\x01",
            "Miss Tita's room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Regrettably, though, they appear\x01",
            "to have stepped out.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_15ED end

    def Function_8_1664(): pass

    label("Function_8_1664")

    Call(0, 9)
    Return()

    # Function_8_1664 end

    def Function_9_1669(): pass

    label("Function_9_1669")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_168E")

    ChrTalk(    #35
        0xD,
        "By yourself today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16F2")

    ChrTalk(    #36
        0xD,
        "Colonel Richard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xD,
        (
            "I still can't believe he'd rebel\x01",
            "against Her Majesty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179D")

    label("loc_16F2")

    OP_A2(0x0)

    ChrTalk(    #38
        0xD,
        (
            "Colonel Richard visited me every evening...\x01",
            "and we would talk for hours, about anything\x01",
            "and everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "I still can't believe he'd rebel\x01",
            "against Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179D")

    Jump("loc_18B6")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_17AA")
    Jump("loc_18B6")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_17B4")
    Jump("loc_18B6")

    label("loc_17B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1824")

    ChrTalk(    #40
        0xD,
        (
            "Would you like an after-dinner\x01",
            "drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xD,
        (
            "We can make anything you'd \x01",
            "like, on or off the menu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(    #42
        0xD,
        (
            "This is a place to talk. Please,\x01",
            "come right in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "For drinks, we have anything you\x01",
            "can think of, be it alcoholic or\x01",
            "non-alcoholic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B6")

    TalkEnd(0xD)
    Return()

    # Function_9_1669 end

    def Function_10_18BA(): pass

    label("Function_10_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E12")
    OP_A2(0x63C)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38180, 0, -57660, 171)
    SetChrPos(0x102, 36300, 0, -58410, 135)
    OP_6D(37860, 0, -58600, 1000)

    ChrTalk(    #44
        0x8,
        "#800FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#000FMr. Murdock! I thought you might\x01",
            "be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#010FWith mayoral-class individuals on\x01",
            "the guest list, we had a feeling\x01",
            "you might also be in attendance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#800FI must say I never expected you two to\x01",
            "win a tournament championship and end\x01",
            "up hobnobbing in Grancel Castle.\x02\x03",

            "Cassius' kids to the bone, you are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#000FHeh. It took more than our up-\x01",
            "bringing to get here. Lots of\x01",
            "people helped along the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#010FSo it's been a few days... Have\x01",
            "there been any developments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#800FWell...right after you left for the \x01",
            "capital, Captain Amalthea from the\x01",
            "Intelligence Division came knocking.\x02\x03",

            "She forced me to come to this \x01",
            "banquet, but I kept my mouth\x01",
            "shut about Leiston Fortress.\x02\x03",

            "Professor Russell and company are\x01",
            "still on the run, too. Army hasn't\x01",
            "found 'em yet.\x02\x03",

            "But the longer we keep this up,\x01",
            "the less chance they have. It's\x01",
            "really only a matter of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#000FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#800FI asked Captain Amalthea if I could\x01",
            "see Her Majesty and wish her well,\x01",
            "but no luck--I was flat-out refused.\x02\x03",

            "So in other words, we definitely\x01",
            "aren't gonna be able to do this\x01",
            "the easy way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#000FWe sure aren't...but don't you\x01",
            "worry, because we've totally\x01",
            "got that covered!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#010FWe WILL get the professor's message\x01",
            "to Her Majesty, one way or another.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_223D")

    label("loc_1E12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_1E90")

    ChrTalk(    #55
        0x8,
        (
            "#800FStill seems busy out there.\x02\x03",

            "Since I'm here, I think I'll\x01",
            "go tie one on before I take\x01",
            "my leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F30")

    label("loc_1E90")


    ChrTalk(    #56
        0x8,
        (
            "#800FNeither Professor Russell nor myself\x01",
            "can go for long without spending some\x01",
            "time at the factory.\x02\x03",

            "I'm going to catch the Linde\x01",
            "back to Zeiss tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F30")

    Jump("loc_223A")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F3D")
    Jump("loc_223A")

    label("loc_1F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1F47")
    Jump("loc_223A")

    label("loc_1F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FBC")

    ChrTalk(    #57
        0x8,
        (
            "#800FI'm glad to hear Her Majesty is\x01",
            "on the mend.\x02\x03",

            "That alone makes the whole trip\x01",
            "worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217E")

    label("loc_1FBC")

    OP_A2(0x2)

    ChrTalk(    #58
        0x8,
        "#800FMadam Hilda. You look well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x138,
        (
            "#710FAs do you, Mr. Murdock.\x02\x03",

            "Though busy as ever, it seems!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#800FYes, but it's hardly work at all when\x01",
            "the central factory is so full of\x01",
            "bright minds.\x02\x03",

            "I'm glad to hear Her Majesty is\x01",
            "on the mend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x138,
        (
            "#710FIndeed. I'm sure we'll all be\x01",
            "able to see her again soon.\x02\x03",

            "If there is anything you need\x01",
            "in your room, please feel free\x01",
            "to let me know.\x02\x03",

            "I'll bring it right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "#800FThank you, Hilda.\x02",
    )

    CloseMessageWindow()

    label("loc_217E")

    Jump("loc_223A")

    label("loc_2181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_21CA")

    ChrTalk(    #63
        0x8,
        (
            "#800FEstelle! Joshua!\x02\x03",

            "So, have you met with Her Majesty?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_21CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_223A")

    ChrTalk(    #64
        0x8,
        (
            "#800FThe Intelligence Division has\x01",
            "eyes everywhere.\x02\x03",

            "We'll have to be more subtle\x01",
            "in our movements.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223A")

    TalkEnd(0xFE)

    label("loc_223D")

    Return()

    # Function_10_18BA end

    def Function_11_223E(): pass

    label("Function_11_223E")

    EventBegin(0x0)
    OP_6D(142500, 4850, 7580, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(343, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 143590, 4000, 7800, 270)
    SetChrPos(0x101, 141480, 4000, 7160, 90)
    SetChrPos(0x102, 141270, 4000, 8340, 90)

    ChrTalk(    #65
        0x9,
        (
            "#110F...I met Cassius shortly after I graduated\x01",
            "from the military academy.\x02\x03",

            "I was assigned to a mobile unit that was under\x01",
            "his command.\x02\x03",

            "And since that time, I have found myself in his\x01",
            "debt again and again, both personally and\x01",
            "professionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#000FUh...he did...?\x02\x03",

            "And, uh...what did you think\x01",
            "of him at the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#110FTo put it simply, he was a hero.\x02\x03",

            "A master swordsman, known simply as the 'Divine Blade.'\x02\x03",

            "No matter the scenario, he could find\x01",
            "a way to handle any number of battle-\x01",
            "fronts in every direction...\x02\x03",

            "It wasn't just a matter of sheer\x01",
            "tactics... He understood and could\x01",
            "direct high-level strategy, as well.\x02\x03",

            "Quite simply, he was a\x01",
            "man without peer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#000FIf I didn't know better, I'd\x01",
            "say we were talking about two\x01",
            "different people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#010FSo you were with our father\x01",
            "during the Hundred Days War?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#110FYes...\x01",
            "He was my C.O.\x02\x03",

            "Even now, I can still vividly remember the\x01",
            "excitement that filled me as we executed his plan\x01",
            "that turned the war's tide...\x02\x03",

            "Any time I get to talking about\x01",
            "those days, time just runs away\x01",
            "with me...\x02\x03",

            "But this much I can tell you:\x02\x03",

            "If Cassius Bright had not been part\x01",
            "of the Royal Army, Liberl would now\x01",
            "be part of the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#000FN-No way!\x02\x03",

            "That's kinda hard to believe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "#110FHa ha... Well, as a hero, he had\x01",
            "a knack for doing unbelievable\x01",
            "things.\x02\x03",

            "He left the army immediately after the war,\x01",
            "declining even a medal from the queen, so few\x01",
            "know of his achievements...\x02\x03",

            "But inside the army, many soldiers still hold\x01",
            "him up as the prime example of what a hero\x01",
            "should be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#000FUhh...\x02\x03",

            "He never said one word\x01",
            "about any of this to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#010FWell, it's not really the kind of\x01",
            "thing you tell your daughter about.\x02\x03",

            "It's not fair to criticize him for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#000FHey, whose side are you on?!\x02\x03",

            "And besides, why doesn't any of\x01",
            "this shock you like it shocks me?\x02\x03",

            "Did you already know about all\x01",
            "of this or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        (
            "#010FWell, I didn't know that he was\x01",
            "Colonel Richard's superior officer...\x02\x03",

            "The rest I knew about...vaguely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#000F'Vaguely'?!\x02\x03",

            "You're an accomplice?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#010FH-Hey, calm down...\x02\x03",

            "It's not like he TOLD me any\x01",
            "of it. I just...figured a lot\x01",
            "of it out.\x02\x03",

            "He told me he didn't feel it was something\x01",
            "worth going out of his way to tell others about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#000FGrrr... I just don't get it.\x02\x03",

            "When he comes back,\x01",
            "he is SO in trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        "#110FHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#000FErr... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#010FPlease excuse us.\x01",
            "We didn't mean to interrupt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#110FNo, no. Seeing you like this\x01",
            "is actually a bit of a relief.\x02\x03",

            "When I found out that your father was intending\x01",
            "to leave the military, I desperately tried to\x01",
            "stop him...\x02\x03",

            "But it seems that by leaving, he did what was\x01",
            "best for himself after all.\x02\x03",

            "After losing his dear wife, maybe\x01",
            "being with you was all that could\x01",
            "help him recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#000FColonel Richard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()

    def lambda_2DBE():

        label("loc_2DBE")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2DBE")

    QueueWorkItem2(0x101, 1, lambda_2DBE)

    def lambda_2DCF():

        label("loc_2DCF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2DCF")

    QueueWorkItem2(0x102, 1, lambda_2DCF)
    OP_8F(0x9, 0x231B8, 0xFA0, 0x1824, 0x7D0, 0x0)

    ChrTalk(    #86
        0x9,
        (
            "#110FNow, then... I thank you for\x01",
            "taking the time to come here.\x02\x03",

            "I really can't keep the duke\x01",
            "waiting, so I'm afraid you'll\x01",
            "have to excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#000FOh...all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#010FOur apologies for making\x01",
            "you so late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "#110FNot at all. You both have told\x01",
            "me the one thing I wanted most\x01",
            "to know.\x02\x03",

            "And thus, I have no regrets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#010FHow's that again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "#110FHa ha... I'm sure we'll have a\x01",
            "chance to speak again soon.\x02\x03",

            "Cassius might even be with us\x01",
            "then, to share in the stories.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_43(0x9, 0x1, 0x0, 0xC)

    def lambda_301D():
        OP_6D(143890, 2750, 1780, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_301D)

    def lambda_3035():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3035)
    Sleep(5000)
    OP_63(0x101)
    OP_63(0x102)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(142230, 4850, 7220, 2000)

    ChrTalk(    #93
        0x101,
        (
            "#000FUmm...\x02\x03",

            "Okay, who was that man, and what\x01",
            "has he done with Colonel Richard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        "#010FWhat are you babbling about now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#000FIt's just that it's weird to hear\x01",
            "him talking about Dad that way.\x02\x03",

            "I wasn't expecting him to be\x01",
            "so...well, nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#010FTrue. He doesn't seem all that\x01",
            "villainous, anyway.\x02\x03",

            "Even so, it's pretty much a\x01",
            "foregone conclusion that he's\x01",
            "got something up his sleeve.\x02\x03",

            "For now, we should probably put the issue of Dad\x01",
            "aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#000FYeah, I guess you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        (
            "#010FAnd I hate to say it...\x02\x03",

            "...but I think that he might've been\x01",
            "playing nice, just because he could\x01",
            "get something out of it.\x02\x03",

            "He's an intelligence officer, so he\x01",
            "probably thinks that fooling a couple\x01",
            "of kids is as easy as could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#000FD-Don't you think that's going\x01",
            "a little too far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#010FYou might be right.\x02\x03",

            "Let me be the one who's mistrustful of others.\x02\x03",

            "You should just follow your instincts and\x01",
            "believe whatever you think is right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#010FBut just make sure you're prepared for anything.\x01",
            "Don't let your guard down.\x02\x03",

            "I'd say a bracer's job...is pretty\x01",
            "much that, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#000FJoshua...?\x02\x03",

            "Okay, I got it.\x02\x03",

            "I'll keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        "#010FThank you, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#000F'Thank you'? What the heck\x01",
            "are you thanking me for?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#000FAnyway, we need to go\x01",
            "back and see Hilda.\x02\x03",

            "She's probably sick of waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#010FYeah. She should be in the\x01",
            "maid quarters.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    SetChrPos(0x101, 142340, 4000, 5440, 169)
    SetChrPos(0x102, 142340, 4000, 5440, 169)
    SetChrFlags(0x9, 0x80)
    EventEnd(0x0)
    Return()

    # Function_11_223E end

    def Function_12_361B(): pass

    label("Function_12_361B")

    OP_8E(0xFE, 0x24298, 0xFA0, 0x146E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x241D0, 0x7D0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x22632, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20666, 0x0, 0x320, 0xBB8, 0x0)
    Return()

    # Function_12_361B end

    def Function_13_366C(): pass

    label("Function_13_366C")

    EventBegin(0x0)
    OP_6D(88610, 0, 6390, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x138, 2)
    SetChrPos(0x138, 87950, 0, 4590, 0)
    SetChrPos(0x101, 87640, 0, 6230, 90)
    SetChrPos(0x102, 89210, 0, 6370, 270)
    Sleep(1000)

    ChrTalk(    #108
        0x101,
        (
            "#000Fはあ……\x01",
            "ヨシュアってばモテモテね。\x02\x03",

            "あの連中、ヨシュアの挨拶で\x01",
            "目の色変わってたもんね～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#010Fそ、そんなこと無いってば。\x02\x03",

            "エステルとだって結構、\x01",
            "話が弾んでたじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#000Fあたしの時は、あの連中、\x01",
            "別に緊張してなかったもん。\x02\x03",

            "あーあ、何だかちょっと\x01",
            "自信無くなっちゃったなあ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        "#010Fあのねぇ……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 93780, 0, 850, 90)
    SetChrPos(0xB, 93780, 0, 850, 90)

    ChrTalk(    #112
        0xA,
        (
            "ヒック……\x01",
            "何を騒いでおるのだ……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)

    def lambda_3862():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3862)

    def lambda_3870():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3870)

    def lambda_387E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_387E)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x138, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(90380, 0, 5100, 1000)

    def lambda_38E2():

        label("loc_38E2")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_38E2")

    QueueWorkItem2(0x101, 1, lambda_38E2)

    def lambda_38F3():

        label("loc_38F3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_38F3")

    QueueWorkItem2(0x102, 1, lambda_38F3)

    def lambda_3904():

        label("loc_3904")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3904")

    QueueWorkItem2(0x138, 1, lambda_3904)

    def lambda_3915():
        OP_6D(89070, 0, 5570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3915)

    def lambda_392D():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_392D)
    WaitChrThread(0xA, 0x1)
    ClearChrFlags(0xB, 0x80)

    def lambda_3952():
        OP_8E(0xFE, 0x15D06, 0x0, 0x1158, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3952)

    def lambda_396D():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_396D)
    WaitChrThread(0xB, 0x1)

    def lambda_398D():
        OP_8E(0xFE, 0x15EA0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_398D)
    WaitChrThread(0xA, 0x1)

    def lambda_39AD():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_39AD)

    ChrTalk(    #113
        0x138,
        "#710Fこれは公爵閣下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        "#220F何だ、女官長ではないか……\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #115
        0xA,
        (
            "#220Fおや……\x01",
            "なんだ、その侍女たちは……\x02\x03",

            "ヒック……\x01",
            "見たことのない顔だが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_3AE1")

    ChrTalk(    #116
        0x138,
        (
            "#710F新しく入った見習いの\x01",
            "レナとカリンと申します。\x02\x03",

            "まだ城内に不慣れなもので\x01",
            "色々案内しているところです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD6")

    label("loc_3AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_3B5C")

    ChrTalk(    #117
        0x138,
        (
            "#710F新しく入った見習いの\x01",
            "シェラとカリンと申します。\x02\x03",

            "まだ城内に不慣れなもので\x01",
            "色々案内しているところです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD6")

    label("loc_3B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_3BD6")

    ChrTalk(    #118
        0x138,
        (
            "#710F新しく入った見習いの\x01",
            "ドロシーとカリンと申します。\x02\x03",

            "まだ城内に不慣れなもので\x01",
            "色々案内しているところです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD6")


    ChrTalk(    #119
        0xB,
        "#720Fおや……？\x02",
    )

    CloseMessageWindow()
    OP_8E(0xB, 0x16044, 0x0, 0x10AE, 0x7D0, 0x0)
    OP_8E(0xB, 0x15F40, 0x0, 0x14BE, 0x7D0, 0x0)
    TurnDirection(0xB, 0x102, 400)
    Sleep(500)
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #120
        0xB,
        "#720F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#000F（あっ……気付かれた？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x102,
        (
            "#010F（……まずいな。）\x02\x03",

            "（この人とは何度か会ってるから\x01",
            "  気付かれてもおかしくない……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        (
            "#220Fなんだ、フィリップ。\x01",
            "まじまじと顔を見つめて……\x02\x03",

            "わはは、堅物のお前にしては\x01",
            "ずいぶんと珍しいではないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "#720Fこれは失礼しました……\x02\x03",

            "わたくしの姪に似ていたので\x01",
            "一瞬、目を疑ってしまいまして。\x02\x03",

            "お嬢さん方。\x01",
            "申し訳ございませんでしたな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#000Fあ、いえいえ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#010Fどうかお気になさらずに……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xA,
        (
            "#220Fふむ、見ればどちらも\x01",
            "中々の上玉ではないか……\x02\x03",

            "特に栗色の髪の方は\x01",
            "健康的ですこぶるいいのう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#000Fぞわわっ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        (
            "#220F黒髪の方は、もう少々、\x01",
            "腰に張りが欲しい所だな……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x102,
        "#010F……きょ、恐縮です。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xA,
        "#220Fふむ、そうだな……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_3F39")

    ChrTalk(    #132
        0xA,
        (
            "#220Fレナとやら！\x01",
            "今夜の伽を申しつけるぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_3F75")

    ChrTalk(    #133
        0xA,
        (
            "#220Fシェラとやら！\x01",
            "今夜の伽を申しつけるぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_3FB0")

    ChrTalk(    #134
        0xA,
        (
            "#220Fドロシーとやら！\x01",
            "今夜の伽を申しつけるぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB0")


    ChrTalk(    #135
        0x101,
        "#000Fへ……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #136
        0xB,
        "#720Fこ、公爵閣下！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#000F（ねえ、伽（トギ）ってなに？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x102,
        "#010F（知らない方がいいと思うよ……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x138,
        (
            "#710F閣下、いくらなんでも\x01",
            "お戯れが過ぎますわよ……\x02\x03",

            "城勤めの侍女は全て\x01",
            "女王陛下に仕える身です。\x02\x03",

            "そのことをお忘れですか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xA,
        (
            "#220Fわかった、わかった……\x01",
            "まったく冗談の通じないヤツだ。\x02\x03",

            "ヒック、どうせ１週間後には\x01",
            "この城は私のものになるのだ。\x02\x03",

            "その時までのお楽しみに\x01",
            "とっておくとしようかのう……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x138,
        "#710F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xB,
        (
            "#720Fか、閣下！\x01",
            "いい加減になさいませ！\x02\x03",

            "暴飲暴食ならともかく、\x01",
            "色に走るなど言語道断！\x02\x03",

            "このフィリップ、一命を賭して\x01",
            "お諫めさせていただきま……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #143
        0xA,
        (
            "#220Fだから冗談だと\x01",
            "言っているであろうが！\x02\x03",

            "もういい！\x01",
            "今夜はとっとと休むぞ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        (
            "#720Fさ、さすがは\x01",
            "閣下でいらっしゃいます。\x02\x03",

            "そちらが閣下の部屋です。\x01",
            "足元にお気を付けください。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42E0():
        OP_6D(87270, 0, 5910, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_42E0)

    def lambda_42F8():
        OP_8E(0xFE, 0x15996, 0x0, 0x1482, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_42F8)
    Sleep(600)

    def lambda_4318():
        OP_8E(0xFE, 0x151EE, 0x0, 0x15C2, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4318)
    WaitChrThread(0xA, 0x1)

    def lambda_4338():
        OP_8E(0xFE, 0x14E38, 0x0, 0x15B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4338)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)

    def lambda_435D():

        label("loc_435D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_435D")

    QueueWorkItem2(0xB, 2, lambda_435D)

    def lambda_436E():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_436E)
    OP_8F(0xA, 0x14E92, 0x0, 0x18EC, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_43BE")

    ChrTalk(    #145
        0xA,
        (
            "#220Fうい～……\x01",
            "そうだ、レナとやら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4429")

    label("loc_43BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_43F4")

    ChrTalk(    #146
        0xA,
        (
            "#220Fうい～……\x01",
            "そうだ、シェラとやら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4429")

    label("loc_43F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_4429")

    ChrTalk(    #147
        0xA,
        (
            "#220Fうい～……\x01",
            "そうだ、ドロシーとやら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4429")


    ChrTalk(    #148
        0xA,
        (
            "#220F困ったことがあったら\x01",
            "遠慮なく私に相談するがいい。\x02\x03",

            "次期国王みずから\x01",
            "親身に相談に乗ってやろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#000Fあは……はは……\x01",
            "どうもありがとうございマス。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        (
            "#220Fわはは、愛いやつじゃ。\x02\x03",

            "うむ……愉快愉快！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4505():
        OP_6D(83810, 0, 6600, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4505)
    OP_8E(0xA, 0x13416, 0x0, 0x1B4E, 0x5DC, 0x0)
    OP_8E(0xA, 0x13416, 0x0, 0x2576, 0x5DC, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    def lambda_4559():

        label("loc_4559")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_4559")

    QueueWorkItem2(0x101, 1, lambda_4559)

    def lambda_456A():

        label("loc_456A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_456A")

    QueueWorkItem2(0x102, 1, lambda_456A)

    def lambda_457B():

        label("loc_457B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_457B")

    QueueWorkItem2(0x138, 1, lambda_457B)

    def lambda_458C():
        OP_6D(88010, 0, 6080, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_458C)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #151
        0xB,
        (
            "#720Fどうもお騒がせしました。\x02\x03",

            "多分、閣下は明日の朝になれば\x01",
            "何も覚えてらっしゃらないでしょう。\x02\x03",

            "どうかご安心くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x138,
        "#710F……そう願いたいものですわね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        (
            "#720F本当に申しわけありません。\x02\x03",

            "夫人、お嬢様がた。\x01",
            "それでは失礼いたします。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xB, 0x149CE, 0x0, 0xE38, 0xBB8, 0x0)
    OP_8E(0xB, 0x13DE4, 0x0, 0xF5A, 0xBB8, 0x0)
    OP_8E(0xB, 0x134B6, 0x0, 0x1888, 0xBB8, 0x0)
    OP_8E(0xB, 0x134B6, 0x0, 0x268E, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(    #154
        0x138,
        (
            "#710Fふう、あの男ときたら……\x02\x03",

            "相変わらず余計な苦労を\x01",
            "背負い込んでいるようですね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #155
        0x101,
        (
            "#000Fあれ、ヒルダさんって\x01",
            "フィリップさんと知り合い？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x138, 0x101, 400)

    ChrTalk(    #156
        0x138,
        (
            "#710F幼い頃からの知り合いです。\x02\x03",

            "もっとも今では、仕える方も\x01",
            "立場も隔たっていますが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x138, 400)

    ChrTalk(    #157
        0x102,
        "#010Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#000F確かにフィリップさんって\x01",
            "見るからに苦労性な感じよね。\x02\x03",

            "公爵が大佐に唆されてる状況に\x01",
            "ハラハラしてるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #159
        0x102,
        (
            "#010Fその可能性は高そうだね……\x02\x03",

            "そういえば、エステル。\x01",
            "君だってモテてるじゃないか。\x02\x03",

            "公爵は君の方が好みだってさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #160
        0x101,
        (
            "#000Fぞわわっ、何だかちっとも\x01",
            "嬉しくないんですけど……\x02\x03",

            "あ、ところで結局、\x01",
            "『トギ』って何だったの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x102,
        "#010Fそ、それは……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x138,
        (
            "#710Fエステル殿。\x02\x03",

            "そのようなことを殿方に聞いて\x01",
            "困らせるものではありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A10():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A10)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #163
        0x101,
        "#000Fへっ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x138,
        "#710F……お耳を拝借。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    OP_8E(0x138, 0x15626, 0x0, 0x1644, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #165
        (
            "\x07\x05ヒルダ夫人は\x01",
            "エステルにそっと耳打ちした。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x138, 0x1578E, 0x0, 0x11EE, 0x3E8, 0x0)

    ChrTalk(    #166
        0x101,
        "#000F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x138,
        "#710F……理解できましたか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #168
        0x101,
        (
            "#000Fあ、あう……\x02\x03",

            "…………ハイ………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x102,
        "#010F（何を聞かされたんだろう……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4214   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_366C end

    def Function_14_4B6F(): pass

    label("Function_14_4B6F")

    EventBegin(0x0)
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 33230, 0, 57840, 90)
    SetChrPos(0x101, 36130, 0, 59420, 0)
    OP_6D(36050, 0, 58110, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_4BDE():

        label("loc_4BDE")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4BDE")

    QueueWorkItem2(0xC, 1, lambda_4BDE)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x101, 0x8C8C, 0x0, 0xDD68, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8E(0x101, 0x8D22, 0x0, 0xE81C, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    OP_8E(0x101, 0x8C8C, 0x0, 0xDD68, 0x7D0, 0x0)
    Sleep(500)
    OP_63(0x101)

    ChrTalk(    #170
        0x101,
        "#000FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xC,
        (
            "#020FWhat's wrong, Estelle? You've\x01",
            "been completely on edge for a\x01",
            "while now.\x02\x03",

            "Something on your mind?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #172
        0x101,
        (
            "#000FY-Yeah...\x02\x03",

            "Did you think Joshua was acting\x01",
            "weird at dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xC,
        (
            "#020F???\x02\x03",

            "If anyone was acting weird,\x01",
            "I'd say it was you.\x02\x03",

            "He was as calm as he ever is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#000FWell, yeah, but...\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #175
        0xC,
        (
            "#020FAh-ha...\x02\x03",

            "I see. I get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#000FUh...get what?\x02",
    )

    CloseMessageWindow()

    def lambda_4DFB():
        OP_6D(35600, 0, 56920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DFB)
    OP_8E(0xC, 0x899E, 0x0, 0xDF0C, 0x7D0, 0x0)

    ChrTalk(    #177
        0xC,
        (
            "#020FYou can't keep secrets from me.♪\x02\x03",

            "I had a feeling about it, but\x01",
            "I was wondering if you'd ever\x01",
            "admit it to yourself.\x02\x03",

            "You're kinda falling for Joshua,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#000F...\x02\x03",

            "Y-You can tell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xC,
        (
            "#020FIt's pretty obvious. Sorry, hon.\x02\x03",

            "But I'm guessing you haven't\x01",
            "told him anything about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#000FN-No...\x02\x03",

            "Joshua's always picking on me,\x01",
            "telling me what a dope I am...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xC,
        (
            "#020F*sigh*\x01",
            "You're so naive.\x02\x03",

            "It's a wonder how you've lasted\x01",
            "this long. You need to learn to\x01",
            "look a little deeper.\x02\x03",

            "Big sister is ready to begin your\x01",
            "education in love, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#000FI'm never asking you for\x01",
            "advice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xC,
        (
            "#020FI'm just kidding. I'm sorry;\x01",
            "I don't mean to tease.\x02\x03",

            "But...\x02\x03",

            "You guys set out just when\x01",
            "puberty was about to hit.\x02\x03",

            "It's only logical that you'd\x01",
            "start picking up on feelings\x01",
            "for each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#000FO-Oh... You think so...?\x02\x03",

            "Traveling together just seems\x01",
            "like such a petty reason for\x01",
            "that kind of thing...\x02\x03",

            "I-I guess I've gotten a little\x01",
            "more self-aware since we started\x01",
            "all this...\x02\x03",

            "Argh! This isn't like me at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xC,
        (
            "#020FHa ha... You're the proverbial\x01",
            "flower that refuses to blossom.\x02\x03",

            "Every girl feels that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        "#000FSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xC,
        (
            "#020FI don't want to lecture you, or\x01",
            "talk about this with you if you're\x01",
            "not ready...\x02\x03",

            "...but if you are, then what say\x01",
            "we have ourselves some girl talk,\x01",
            "hmm?\x02\x03",

            "If you aren't, then nothing's\x01",
            "ever going to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#000FUmm...\x01",
            "Yeah, I think I'm ready.\x02\x03",

            "I promise I'll listen to whatever\x01",
            "you have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xC,
        (
            "#020FOkay...\x02\x03",

            "All right! Time for your\x01",
            "lesson, my protege!\x02\x03",

            "Oh, Estelle, big sister is\x01",
            "moved to tears!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#000FOn second thought...never mind.\x02\x03",

            "But thank you...\x01",
            "I do feel a little better.\x02\x03",

            "I'm gonna go see Joshua\x01",
            "for a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        (
            "#020FOh...?!\x02\x03",

            "You're going to tell him?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#000FNot about that.\x02\x03",

            "There really does seem to be\x01",
            "something weird going on with\x01",
            "him.\x02\x03",

            "I want to see what that's\x01",
            "about first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xC,
        (
            "#020FAwww...\x02\x03",

            "Well, you do seem to know him\x01",
            "better than anyone else.\x02\x03",

            "I'm sure that everything will turn\x01",
            "out just fine between you two.\x02\x03",

            "Maybe you can even just have a nice,\x01",
            "calm discussion with him and be open\x01",
            "about what's on your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#000FI... I don't think I'm quite\x01",
            "THAT ready yet.\x02\x03",

            "Okay, I'll see you later!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56D7():
        OP_6D(34760, 0, 54010, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56D7)
    OP_8E(0x101, 0x884A, 0x0, 0xC4C2, 0x1388, 0x0)

    def lambda_5703():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5703)
    OP_8E(0x101, 0x88CC, 0x0, 0xBF54, 0x1388, 0x0)

    ChrTalk(    #195
        0xC,
        (
            "#020FYoung love...\x02\x03",

            "Ahh, they'll probably be fine...\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T4221   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4B6F end

    def Function_15_5767(): pass

    label("Function_15_5767")

    EventBegin(0x0)
    OP_6D(78150, 0, 55830, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 79820, 0, 50600, 0)
    OP_6D(89010, 0, 56310, 3000)
    SetChrPos(0x101, 79700, 0, 55220, 90)
    OP_6D(79690, 0, 55490, 2000)

    ChrTalk(    #196
        0x101,
        (
            "#000FHuh... They're not here.\x02\x03",

            "Oh, yeah... Dad's still in\x01",
            "some meeting, I think.\x02\x03",

            "But where's Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)
    Sleep(1000)

    ChrTalk(    #197
        0x101,
        (
            "#000FJoshua...?\x02\x03",

            "Ah... He's out playing\x01",
            "somewhere, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_1B(0x6, 0x0, 0xFFFF)
    EventEnd(0x0)
    Return()

    # Function_15_5767 end

    def Function_16_58C3(): pass

    label("Function_16_58C3")

    EventBegin(0x1)

    ChrTalk(    #198
        0x101,
        (
            "#007FUgh... What is wrong with me?\x02\x03",

            "#000FI need to go to Joshua's room.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_58C3 end

    def Function_17_592E(): pass

    label("Function_17_592E")

    EventBegin(0x1)

    ChrTalk(    #199
        0x101,
        (
            "#007FUgh... What is wrong with me?\x02\x03",

            "#000FI need to go to Joshua's room.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_592E end

    SaveToFile()

Try(main)
