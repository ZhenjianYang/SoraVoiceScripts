from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3160   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3160.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Yuriel',                               # 9
        'Muriel',                               # 10
        'Gary',                                 # 11
        'Ada',                                  # 12
        'Didi',                                 # 13
        'Knowles',                              # 14
        'Father Vixen',                         # 15
        'Sister Kiera',                         # 16
        'Lane',                                 # 17
        'Seagaro',                              # 18
        'Edel',                                 # 19
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
        'ED6_DT07/CH01070 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01060 ._CH',             # 05
        'ED6_DT07/CH01400 ._CH',             # 06
        'ED6_DT07/CH01410 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01130 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01070P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01060P._CP',             # 05
        'ED6_DT07/CH01400P._CP',             # 06
        'ED6_DT07/CH01410P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01130P._CP',             # 0A
    )

    DeclNpc(
        X                   = 61430,
        Z                   = 0,
        Y                   = 45130,
        Direction           = 345,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 54510,
        Z                   = 0,
        Y                   = 43560,
        Direction           = 345,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_286",          # 00, 0
        "Function_1_637",          # 01, 1
        "Function_2_6A7",          # 02, 2
        "Function_3_6BD",          # 03, 3
        "Function_4_743",          # 04, 4
        "Function_5_7F6",          # 05, 5
        "Function_6_8C4",          # 06, 6
        "Function_7_912",          # 07, 7
        "Function_8_9B6",          # 08, 8
        "Function_9_AE9",          # 09, 9
        "Function_10_CD2",         # 0A, 10
        "Function_11_DA0",         # 0B, 11
        "Function_12_E4E",         # 0C, 12
        "Function_13_E53",         # 0D, 13
        "Function_14_3154",        # 0E, 14
    )


    def Function_0_286(): pass

    label("Function_0_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2F2")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_328")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_394")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_365")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 15690, 4000, 42960, 96)
    Jump("loc_37B")

    label("loc_365")

    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 60250, 1000, 51160, 270)

    label("loc_37B")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 61930, 0, 46550, 4)
    Jump("loc_636")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3CA")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 57890, 0, 48010, 82)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 59610, 0, 47980, 274)
    Jump("loc_636")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 54110, 0, 42050, 20)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 55350, 0, 42050, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 63500, 0, 46550, 348)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 62290, 0, 46560, 338)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_529")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60350, 1000, 51110, 285)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60270, 1000, 52070, 281)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 56260, 0, 45050, 348)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 56260, 0, 45050, 348)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_636")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5D7")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 61490, 0, 45200, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 62440, 0, 45200, 3)
    Jump("loc_636")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_636")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 61490, 0, 45200, 2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 62440, 0, 45200, 3)

    label("loc_636")

    Return()

    # Function_0_286 end

    def Function_1_637(): pass

    label("Function_1_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_641")
    Jump("loc_6A6")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_64B")
    Jump("loc_6A6")

    label("loc_64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_655")
    Jump("loc_6A6")

    label("loc_655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_65F")
    Jump("loc_6A6")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_66D")
    OP_64(0x0, 0x1)
    Jump("loc_6A6")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_677")
    Jump("loc_6A6")

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_681")
    Jump("loc_6A6")

    label("loc_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_6A6")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_6A6")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_6A6")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A6")

    label("loc_6A6")

    Return()

    # Function_1_637 end

    def Function_2_6A7(): pass

    label("Function_2_6A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6A7")

    label("loc_6BC")

    Return()

    # Function_2_6A7 end

    def Function_3_6BD(): pass

    label("Function_3_6BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(    #0
        0xFE,
        (
            "So, here it is. The Zeiss branch\x01",
            "of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Only one stop left...the great\x01",
            "Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73F")

    TalkEnd(0xFE)
    Return()

    # Function_3_6BD end

    def Function_4_743(): pass

    label("Function_4_743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F2")

    ChrTalk(    #2
        0xFE,
        (
            "The church is quite simple,\x01",
            "isn't it? So different from\x01",
            "the surrounding buildings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I wonder if there's a revolving chair\x01",
            "or some other hidden gimmick?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F2")

    TalkEnd(0xFE)
    Return()

    # Function_4_743 end

    def Function_5_7F6(): pass

    label("Function_5_7F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_8C0")

    ChrTalk(    #4
        0xFE,
        (
            "I believe we should turn to the\x01",
            "Goddess Aidios for guidance\x01",
            "after today's events...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "You seem worried as well. I pray\x01",
            "Aidios protects and cares for you,\x01",
            "and washes your worries away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C0")

    TalkEnd(0xFE)
    Return()

    # Function_5_7F6 end

    def Function_6_8C4(): pass

    label("Function_6_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_911")
    TalkBegin(0x8)

    ChrTalk(    #6
        0xFE,
        (
            "It's so loud outside, I can barely\x01",
            "concentrate on my book!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_911")

    Return()

    # Function_6_8C4 end

    def Function_7_912(): pass

    label("Function_7_912")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_9B2")

    ChrTalk(    #7
        0xFE,
        (
            "I may complain a lot, but I always\x01",
            "come to Sunday School!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "...It sure is noisy outside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Don't they know some of us\x01",
            "are trying to study?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B2")

    TalkEnd(0xFE)
    Return()

    # Function_7_912 end

    def Function_8_9B6(): pass

    label("Function_8_9B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(    #10
        0xFE,
        "Sooo...where to go now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I'm a wanderin' man. Go where\x01",
            "and when I please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "My feet and my heart are my\x01",
            "guide, and I live free.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE5")

    label("loc_A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_AE5")

    ChrTalk(    #13
        0xFE,
        "Oh, good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Nothing like starting the day\x01",
            "with a morning prayer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Close your eyes and you can\x01",
            "forget all about orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE5")

    TalkEnd(0xFE)
    Return()

    # Function_8_9B6 end

    def Function_9_AE9(): pass

    label("Function_9_AE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_BAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B36")
    TurnDirection(0xFE, 0xC, 400)

    ChrTalk(    #16
        0xFE,
        (
            "Didi, sit still. We're almost\x01",
            "finished here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_B36")

    OP_A2(0x3)

    ChrTalk(    #17
        0xFE,
        (
            "We came all this way...we should\x01",
            "all say a prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Goddess Aidios...thank you for\x01",
            "your gift of medicine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAC")

    Jump("loc_CCE")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C36")

    ChrTalk(    #19
        0xFE,
        (
            "Father Vixen's medicines always\x01",
            "work so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "It's times like these when I'm\x01",
            "truly thankful for the church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCE")

    label("loc_C36")

    OP_A2(0x3)

    ChrTalk(    #21
        0xFE,
        (
            "I've come for some more medicine.\x01",
            "My neck and shoulders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Everything gets so stiff that\x01",
            "the pain goes right on up to\x01",
            "my head lately.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)

    label("loc_CCE")

    TalkEnd(0xFE)
    Return()

    # Function_9_AE9 end

    def Function_10_CD2(): pass

    label("Function_10_CD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D01")

    ChrTalk(    #23
        0xFE,
        "Knowles, that's a bad habit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D9C")

    label("loc_D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(    #24
        0xFE,
        (
            "Mommy?\x01",
            "Mommy, are we finished?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9C")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_D9C")

    ChrTalk(    #25
        0xFE,
        "Mommy? Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I think your shoulders' orbaldilly\x01",
            "energy pressure is too high,\x01",
            "Mommy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_CD2 end

    def Function_11_DA0(): pass

    label("Function_11_DA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(    #27
        0xFE,
        "*gasp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "How could people just LEAVE\x01",
            "things all messy like this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I can't just leave it...!\x01",
            "The unevenness, the clutter...\x01",
            "It HURTS my braiiiiiin!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A")

    TalkEnd(0xFE)
    Return()

    # Function_11_DA0 end

    def Function_12_E4E(): pass

    label("Function_12_E4E")

    Call(0, 13)
    Return()

    # Function_12_E4E end

    def Function_13_E53(): pass

    label("Function_13_E53")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154E")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x107, 57370, 1000, 52020, 90)
    SetChrPos(0x102, 56420, 1000, 52490, 90)
    SetChrPos(0x101, 56210, 1000, 51250, 90)
    SetChrPos(0x108, 57250, 1000, 50620, 45)
    TurnDirection(0xE, 0x107, 0)
    OP_6D(58050, 1000, 52120, 1000)

    ChrTalk(    #30
        0x101,
        (
            "#006FFather!\x01",
            "We got the Zemuria Moss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        "You have it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "I'm impressed you were able to\x01",
            "get it so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        (
            "#560FCan you use this to make\x01",
            "that medicine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xE,
        "Yes, yes. Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "I need to mix it in the back.\x01",
            "Come with me, if you'd please.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(16290, 4000, 43670, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(3090, 0)
    OP_6C(41000, 0)
    OP_6E(262, 0)
    SetChrPos(0xE, 15590, 4000, 43000, 90)
    SetChrPos(0xF, 15690, 4000, 41980, 45)
    OP_4A(0xF, 255)

    def lambda_103B():

        label("loc_103B")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_103B")

    QueueWorkItem2(0x0, 1, lambda_103B)

    def lambda_104C():

        label("loc_104C")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_104C")

    QueueWorkItem2(0x1, 1, lambda_104C)

    def lambda_105D():

        label("loc_105D")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_105D")

    QueueWorkItem2(0x2, 1, lambda_105D)

    def lambda_106E():

        label("loc_106E")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_106E")

    QueueWorkItem2(0x3, 1, lambda_106E)
    SetChrPos(0x101, 14110, 4000, 44580, 150)
    SetChrPos(0x102, 14410, 4000, 45600, 176)
    SetChrPos(0x107, 14890, 4000, 44370, 153)
    SetChrPos(0x108, 15390, 4000, 45540, 176)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #36
        0xE,
        (
            "#6PThe blue and gold consecrated\x01",
            "by septium, the source of all\x01",
            "things, abides here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "#6POh, Great Goddess, we call on your\x01",
            "will to shape and purify the power\x01",
            "distilled within.\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "magic\\\\mg110_0.eff")
    PlayEffect(0x0, 0x0, 0xFF, 16260, 4100, 42980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #38
        0xE,
        "#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        "#6PIt is ready.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x107, 400)

    def lambda_1202():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1202)

    def lambda_1210():
        OP_6D(16290, 4000, 44670, 1000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1210)
    OP_8E(0xE, 0x3A48, 0xFA0, 0xAA32, 0x3E8, 0x0)
    TurnDirection(0xE, 0x107, 400)

    ChrTalk(    #40
        0xE,
        "Here. Take this.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x365, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #41
        "\x07\x00Received \x07\x02Arve Sovereign Serum\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x366, 1)
    OP_8F(0xE, 0x3A5C, 0xFA0, 0xA910, 0x3E8, 0x0)

    ChrTalk(    #42
        0x107,
        "#560FWhat a pretty color!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#501FDo you...drink this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xE,
        "Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xE,
        (
            "#6PMind you, this will not destroy the poison. It \x01",
            "will only boost the patient's immune system\x01",
            "so that it may deal with the toxic agents itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x108,
        "#070FHow very...Eastern.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xE,
        (
            "Yes, it does share some of its\x01",
            "origin with the more esoteric\x01",
            "cures of the East.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        "Go. Take it to your friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#001FThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x107,
        "#061FThank you so much, Father!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrPos(0x101, 11980, 2000, 47970, 270)
    SetChrPos(0x102, 11980, 2000, 47970, 270)
    SetChrPos(0x107, 11980, 2000, 47970, 270)
    SetChrPos(0x108, 11980, 2000, 47970, 270)
    SetChrPos(0xE, 59070, 1000, 52160, 180)
    SetChrPos(0xF, 15690, 4000, 42960, 90)
    OP_4B(0xF, 255)
    OP_6D(11980, 2000, 47970, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x557)
    OP_28(0x42, 0x1, 0x100)
    EventEnd(0x0)
    Jump("loc_3150")

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE0")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x107, 57370, 1000, 52020, 90)
    SetChrPos(0x102, 56420, 1000, 52490, 90)
    SetChrPos(0x101, 56210, 1000, 51250, 90)
    TurnDirection(0xE, 0x107, 0)
    OP_4A(0xF, 255)
    OP_6D(58050, 1000, 52120, 1000)

    ChrTalk(    #51
        0xE,
        "Tita...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xE,
        (
            "What brings you here at this\x01",
            "time of night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x107,
        (
            "#068FOh, Father!\x02\x03",

            "Please help us save Agate!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0xE,
        "What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#004FTita, calm down a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        "#012FFather, you see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #57
        "\x07\x05Joshua explained Agate's poisoning and the details of the poison itself.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #58
        0xF,
        "I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        "Hmm. This is troubling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#002FIs there anything you can do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xE,
        (
            "Thankfully, we do have a treatment\x01",
            "here at the church for virulent nerve\x01",
            "toxins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xE,
        (
            "It doesn't nullify the poison, but it does boost\x01",
            "the patient's immune system so that he can\x01",
            "better fight off the effects on his own.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)

    ChrTalk(    #63
        0xE,
        (
            "#3PSister Kiera, you're familiar with the\x01",
            "medicine I refer to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xF,
        "I am. But the ingredients...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        "#069FYou're out of the ingredients?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#012FWhat do you need,\x01",
            "and where can we get it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x107, 400)

    ChrTalk(    #67
        0xE,
        (
            "Zemuria Moss is what we've\x01",
            "called it. It's a species of\x01",
            "bioluminescent plant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xE,
        (
            "It should grow deep in the Limestone\x01",
            "Cave inside the Kaldia Tunnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xE,
        (
            "We've sent bracers to collect it\x01",
            "in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#505FThe Kaldia Tunnel... We went\x01",
            "through there when we came\x01",
            "here to Zeiss!\x02\x03",

            "#006FThis should be a snap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#010FThen let's go find some of this\x01",
            "Zemuria Moss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xE,
        "What? You two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x107,
        (
            "#560FYes, Father. My two friends here\x01",
            "are bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "I see.\x01",
            "That makes things much easier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "At any rate, go back to the guild\x01",
            "and talk to the staff before going\x01",
            "to Limestone Cave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "There might be some record\x01",
            "from earlier collection trips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#006FGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        "#010FLet's go.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x551)
    OP_28(0x42, 0x1, 0x4)
    OP_28(0x42, 0x1, 0x8)
    OP_28(0x42, 0x1, 0x10)
    OP_4B(0xF, 255)
    EventEnd(0x0)
    Jump("loc_3150")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C61")

    ChrTalk(    #79
        0xE,
        (
            "If you ever have a need,\x01",
            "please feel welcome to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "The Septian Church is for everyone,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBC")

    label("loc_1C61")

    OP_A2(0x6)

    ChrTalk(    #81
        0xE,
        "Oh, it's you. Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xE,
        "Thank you so much for before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#000FThank you, too, Father.\x02\x03",

            "Thanks to you, Agate made\x01",
            "a total recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        "#010FWe very much appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xE,
        (
            "No need to thank me. I'm only\x01",
            "doing what I must.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        (
            "If you ever have a need,\x01",
            "please feel welcome to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xE,
        (
            "The Septian Church is for everyone,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBC")

    Jump("loc_3150")

    label("loc_1DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 1)), scpexpr(EXPR_END)), "loc_1E35")

    ChrTalk(    #88
        0xE,
        (
            "Even if he's recovered from\x01",
            "the poison, his body is still\x01",
            "recuperating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        "We need only wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2182")

    label("loc_1E35")

    OP_A2(0x579)

    ChrTalk(    #90
        0x107,
        (
            "#060FFather Vixen!\x02\x03",

            "Thank you for that medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        "Hello, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "Where are you headed after your\x01",
            "current job is done...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x106,
        "#050FMedicine...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x107,
        (
            "#060FThat's correct.\x02\x03",

            "Father Vixen here made the medicine\x01",
            "we gave you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x106,
        (
            "#050FIs that right...?\x02\x03",

            "...Sorry for the trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#000FYou suck at showing gratitude,\x01",
            "you know that, Agate?\x02\x03",

            "Why can't you just say\x01",
            "'thank you'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#010FPots and kettles, Estelle.\x01",
            "Be careful what you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        (
            "Still...you bracers are something else if\x01",
            "you're able to be up and about so soon\x01",
            "after getting so high a dosage of poison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        "Still, don't overdo things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#050FYeah, yeah. That's good advice\x01",
            "for your body. Me, I'm fine.\x02\x03",

            "...\x02\x03",

            "Umm...yes. Anyway, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#000FOh, yeah. We should go.\x02\x03",

            "See you, Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xE,
        "Yes, goodbye.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xE,
        "Tita...stay strong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x107,
        (
            "#060F...\x02\x03",

            "...Yes, Father!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2182")

    Jump("loc_3150")

    label("loc_2185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 0)), scpexpr(EXPR_END)), "loc_2206")

    ChrTalk(    #105
        0xE,
        (
            "I'll be praying for Agate's full\x01",
            "and speedy recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "You're welcome here whenever\x01",
            "you wish to visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2543")

    label("loc_2206")

    OP_A2(0x578)

    ChrTalk(    #107
        0xE,
        "Oh, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xE,
        "Did the medicine work out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#010FYes, for the most part.\x02\x03",

            "According to Dr. Miriam at the\x01",
            "central factory, Agate is past\x01",
            "the worst of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xE,
        "I see. That is a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#000FYes, he ought to be fine.\x02\x03",

            "This is Agate we're talking about,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FIndeed.\x02\x03",

            "He's tough enough to give even\x01",
            "Zin a run for his money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#000FBut Father, we're real sorry for\x01",
            "bothering you so late.\x02\x03",

            "Making you stay up like that\x01",
            "putting the serum together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "My dear, anyone who saw little\x01",
            "Tita's face would have done\x01",
            "exactly the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xE,
        (
            "Seeing that shy little girl with\x01",
            "such a wild look about her\x01",
            "would spur anyone to action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xE,
        (
            "I'll be praying for Agate's full\x01",
            "and speedy recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#000FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        "#010FWe deeply appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xE,
        (
            "You're welcome here whenever\x01",
            "you wish to visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2543")

    Jump("loc_3150")

    label("loc_2546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_262D")

    ChrTalk(    #120
        0xE,
        (
            "The medicine will not destroy the\x01",
            "poison, but only boost his immune\x01",
            "system so that he may recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xE,
        (
            "It should have some positive\x01",
            "effect, even on such a rare\x01",
            "specimen of poison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xE,
        "Hurry. Take it to him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_262D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2694")

    ChrTalk(    #123
        0xE,
        "We will be ready and waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xE,
        (
            "The Limestone Cave is a dangerous\x01",
            "place. Be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2730")

    label("loc_2694")


    ChrTalk(    #125
        0xE,
        (
            "At any rate, go back to the guild\x01",
            "and talk to the staff before going\x01",
            "to Limestone Cave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xE,
        (
            "There might be some record\x01",
            "from earlier collection trips.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2730")

    Jump("loc_3150")

    label("loc_2733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_281B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_27A1")

    ChrTalk(    #127
        0xE,
        "This is quite serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xE,
        (
            "We're going to all have to do\x01",
            "our best to get through this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2818")

    label("loc_27A1")

    OP_A2(0x6)

    ChrTalk(    #129
        0xE,
        "This is quite serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        (
            "There haven't been any reports\x01",
            "of injuries, but I should prepare\x01",
            "something anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2818")

    Jump("loc_3150")

    label("loc_281B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_28DA")

    ChrTalk(    #131
        0xE,
        (
            "And so it was that Zeiss, the\x01",
            "'Clock Maker's Town,' realized\x01",
            "its greater purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xE,
        (
            "The orbments they built spread\x01",
            "across the land, spurring the\x01",
            "Orbal Revolution of Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3150")

    label("loc_28DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_292E")

    ChrTalk(    #133
        0xE,
        "O Aidios, Goddess of the Sky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        "Guide and protect your flock...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3150")

    label("loc_292E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2B28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_29F0")

    ChrTalk(    #135
        0xE,
        (
            "I understand Sister Kiera's desire\x01",
            "to preserve the church as a place\x01",
            "of prayer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "But I believe the church must\x01",
            "first be a place where the\x01",
            "troubled can come for help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B25")

    label("loc_29F0")

    OP_A2(0x6)

    ChrTalk(    #137
        0xE,
        (
            "Prescribing medical aid is one of\x01",
            "the church's equally important\x01",
            "functions as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        (
            "And we're not limited to medicine, but also\x01",
            "personal guidance or domestic advice. The\x01",
            "role we play in the community is a large one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xE,
        (
            "I feel these community services\x01",
            "are the very future of the Septian\x01",
            "Church.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B25")

    Jump("loc_3150")

    label("loc_2B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2DD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2BBD")

    ChrTalk(    #140
        0xE,
        (
            "I am always willing to listen if\x01",
            "you need someone to talk to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xE,
        (
            "If you have any problems, I welcome\x01",
            "you to bring them here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD2")

    label("loc_2BBD")

    OP_A2(0x6)

    ChrTalk(    #142
        0xE,
        "Good morning, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xE,
        "There, there...no need to speak.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xE,
        (
            "Last night was quite hard for\x01",
            "you, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x107,
        "#060F*sob* I'm so sorry... *sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xE,
        (
            "There is nothing you need to\x01",
            "apologize for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        (
            "Experiments are vital to progress.\x01",
            "And sometimes experiments must\x01",
            "fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xE,
        "We all understand this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xE,
        (
            "Tita, make sure you are there\x01",
            "to support your grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        "#060FYes, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "I am always willing to listen if\x01",
            "you need someone to talk to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xE,
        (
            "If you have any problems, I welcome\x01",
            "you to bring them here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD2")

    Jump("loc_3150")

    label("loc_2DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_309E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2E5F")

    ChrTalk(    #153
        0xE,
        (
            "If you need to talk, I am always\x01",
            "here, ready to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xE,
        (
            "The church is not solely a house\x01",
            "of prayers, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_2E5F")

    OP_A2(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9A")

    ChrTalk(    #155
        0xE,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xE,
        "Is that young Tita I see?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EEB")

    label("loc_2E9A")


    ChrTalk(    #157
        0xE,
        "Hello, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xE,
        (
            "It feels like such a long time\x01",
            "since I've seen your face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEB")


    ChrTalk(    #159
        0x107,
        "#060FHello, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xE,
        (
            "It appears your grandfather is\x01",
            "as busy as he ever was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xE,
        (
            "When your work has slowed down\x01",
            "we'll be eagerly waiting for you\x01",
            "here at Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xE,
        (
            "You're still a child, Tita. I think it's\x01",
            "important for you to spend time\x01",
            "with other children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x107,
        "#060FYes, Father. I'll try.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xE,
        (
            "If you need to talk, I am always\x01",
            "here, ready to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xE,
        (
            "The church is not solely a house\x01",
            "of prayers, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309B")

    Jump("loc_3150")

    label("loc_309E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_30E8")

    ChrTalk(    #166
        0xE,
        (
            "Of course you're welcome to\x01",
            "come and pray any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3150")

    label("loc_30E8")

    OP_A2(0x6)

    ChrTalk(    #167
        0xE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xE,
        (
            "I am here to help you, with anything,\x01",
            "spiritual or mundane.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3150")

    TalkEnd(0xE)
    Return()

    # Function_13_E53 end

    def Function_14_3154(): pass

    label("Function_14_3154")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_31F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_31AC")

    ChrTalk(    #169
        0xFE,
        "Please come back any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "Any time you're ready to pray.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31F4")

    label("loc_31AC")

    OP_A2(0x7)

    ChrTalk(    #171
        0xFE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "I am always here to listen.\x02",
    )

    CloseMessageWindow()

    label("loc_31F4")

    Jump("loc_3AF6")

    label("loc_31F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_32D5")

    ChrTalk(    #173
        0xFE,
        (
            "It appears the medicine worked.\x01",
            "Father Vixen is quite a wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Sometimes it seems as though\x01",
            "he is able to save anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "I think maybe it's important for\x01",
            "the church to expand its wisdom\x01",
            "like that. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF6")

    label("loc_32D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3494")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3397")

    ChrTalk(    #176
        0xFE,
        (
            "At times like last night, I do feel\x01",
            "that Father Vixen's opinion is\x01",
            "perfectly valid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "But treating the church as an\x01",
            "apothecary is surely not a\x01",
            "proper show of respect?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3491")

    label("loc_3397")

    OP_A2(0x7)

    ChrTalk(    #178
        0xFE,
        (
            "At times like last night, I feel\x01",
            "that Father Vixen's opinion is\x01",
            "perfectly valid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "If we show generosity to others,\x01",
            "they will surely show generosity\x01",
            "in return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "But treating the church as an\x01",
            "apothecary is not a proper\x01",
            "show of respect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3491")

    Jump("loc_3AF6")

    label("loc_3494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_361C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_END)), "loc_3501")

    ChrTalk(    #181
        0xFE,
        (
            "You must hurry and take this\x01",
            "medicine to your friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "We will be praying for him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3619")

    label("loc_3501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_358A")

    ChrTalk(    #183
        0xFE,
        "Did you find the ingredients?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "The one who can actually mix\x01",
            "the ingredients is Father Vixen.\x01",
            "Please give them to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3619")

    label("loc_358A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_35D0")

    ChrTalk(    #185
        0xFE,
        "I await your return.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "Please be careful, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3619")

    label("loc_35D0")


    ChrTalk(    #187
        0xFE,
        "Why, hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "What brings you here this\x01",
            "late at night?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3619")

    Jump("loc_3AF6")

    label("loc_361C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_36A8")

    ChrTalk(    #189
        0xFE,
        (
            "It certainly seems something\x01",
            "serious has happened at the\x01",
            "central factory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "But I do not know all of the\x01",
            "circumstances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF6")

    label("loc_36A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3721")

    ChrTalk(    #191
        0xFE,
        (
            "The streets are especially\x01",
            "lively today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "The children can hardly keep\x01",
            "their attention inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D7")

    label("loc_3721")

    OP_A2(0x7)

    ChrTalk(    #193
        0xFE,
        (
            "Today's class will deal with the\x01",
            "history of our town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "But first...what is all this racket\x01",
            "coming from outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "The children can hardly keep\x01",
            "their attention inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D7")

    Jump("loc_3AF6")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3862")

    ChrTalk(    #196
        0xFE,
        (
            "I thought someone had come,\x01",
            "but they only needed medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "Father Vixen is too lax on the\x01",
            "lack of proper prayers...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF6")

    label("loc_3862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_39EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3902")

    ChrTalk(    #198
        0xFE,
        (
            "I believe a church is a house\x01",
            "of prayers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Currently though, the church is\x01",
            "more like a tourist attraction\x01",
            "or better yet, a drugstore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39EC")

    label("loc_3902")

    OP_A2(0x7)

    ChrTalk(    #200
        0xFE,
        (
            "The people of Zeiss are too busy\x01",
            "with their daily lives to come to\x01",
            "the church and pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "Father Vixen has been trying to\x01",
            "attract people by offering more\x01",
            "community services...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "I believe a church is a house\x01",
            "of prayers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39EC")

    Jump("loc_3AF6")

    label("loc_39EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3AA8")

    ChrTalk(    #203
        0xFE,
        (
            "Last night was quite a\x01",
            "dangerous affair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "The central factory looked like\x01",
            "it was in total uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "Such times of anxiety are best\x01",
            "remedied by a calming prayer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF6")

    label("loc_3AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AF6")

    ChrTalk(    #206
        0xFE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "Please approach and pray.\x02",
    )

    CloseMessageWindow()

    label("loc_3AF6")

    TalkEnd(0xFE)
    Return()

    # Function_14_3154 end

    SaveToFile()

Try(main)
