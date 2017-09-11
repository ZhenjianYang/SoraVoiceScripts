from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3130   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
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
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
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
        "Function_1_63E",          # 01, 1
        "Function_2_6CF",          # 02, 2
        "Function_3_6E5",          # 03, 3
        "Function_4_74E",          # 04, 4
        "Function_5_801",          # 05, 5
        "Function_6_8CF",          # 06, 6
        "Function_7_8FE",          # 07, 7
        "Function_8_9A2",          # 08, 8
        "Function_9_AD5",          # 09, 9
        "Function_10_CBE",         # 0A, 10
        "Function_11_D8C",         # 0B, 11
        "Function_12_E3A",         # 0C, 12
        "Function_13_E3F",         # 0D, 13
        "Function_14_2293",        # 0E, 14
    )


    def Function_0_286(): pass

    label("Function_0_286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_63D")

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2F2")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_63D")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_328")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_63D")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_374")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 61930, 0, 46550, 4)
    Jump("loc_63D")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 57890, 0, 48010, 82)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 59610, 0, 47980, 274)
    Jump("loc_63D")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_442")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 61010, 0, 48400, 306)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 60100, 0, 46860, 7)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 57910, 0, 47170, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 56780, 0, 47520, 45)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_63D")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4AE")
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
    Jump("loc_63D")

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_530")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60350, 1000, 51110, 285)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60270, 1000, 52070, 281)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 56260, 0, 45050, 348)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_63D")

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_57C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 56260, 0, 45050, 348)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    Jump("loc_63D")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5DE")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 58420, 0, 47750, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59620, 0, 47750, 0)
    Jump("loc_63D")

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_63D")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 63690, 0, 48900, 231)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 59070, 1000, 52160, 164)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 58420, 0, 47750, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59620, 0, 47750, 0)

    label("loc_63D")

    Return()

    # Function_0_286 end

    def Function_1_63E(): pass

    label("Function_1_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_656")
    OP_B1("t3130_y")
    Jump("loc_65F")

    label("loc_656")

    OP_B1("t3130_n")

    label("loc_65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_669")
    Jump("loc_6CE")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_673")
    Jump("loc_6CE")

    label("loc_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_67D")
    Jump("loc_6CE")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_687")
    Jump("loc_6CE")

    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_695")
    OP_64(0x0, 0x1)
    Jump("loc_6CE")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_6CE")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_6CE")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_6B3")
    Jump("loc_6CE")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_6BD")
    Jump("loc_6CE")

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6C7")
    Jump("loc_6CE")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6CE")

    label("loc_6CE")

    Return()

    # Function_1_63E end

    def Function_2_6CF(): pass

    label("Function_2_6CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6CF")

    label("loc_6E4")

    Return()

    # Function_2_6CF end

    def Function_3_6E5(): pass

    label("Function_3_6E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_74A")

    ChrTalk(    #0
        0xFE,
        (
            "This is the last stop on my\x01",
            "Liberl pilgrimage. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Quite a...strange...feeling.\x02",
    )

    CloseMessageWindow()

    label("loc_74A")

    TalkEnd(0xFE)
    Return()

    # Function_3_6E5 end

    def Function_4_74E(): pass

    label("Function_4_74E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FD")

    ChrTalk(    #2
        0xFE,
        (
            "The church is quite simple, isn't it?\x01",
            "So different from the surrounding\x01",
            "buildings.\x02",
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

    label("loc_7FD")

    TalkEnd(0xFE)
    Return()

    # Function_4_74E end

    def Function_5_801(): pass

    label("Function_5_801")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_8CB")

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

    label("loc_8CB")

    TalkEnd(0xFE)
    Return()

    # Function_5_801 end

    def Function_6_8CF(): pass

    label("Function_6_8CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_8FD")
    TalkBegin(0x8)

    ChrTalk(    #6
        0xFE,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Where'd Vince go?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_8FD")

    Return()

    # Function_6_8CF end

    def Function_7_8FE(): pass

    label("Function_7_8FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_99E")

    ChrTalk(    #8
        0xFE,
        (
            "I may complain a lot, but I always\x01",
            "come to Sunday School!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "...It sure is noisy outside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Don't they know some of us\x01",
            "are trying to study?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99E")

    TalkEnd(0xFE)
    Return()

    # Function_7_8FE end

    def Function_8_9A2(): pass

    label("Function_8_9A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_A3D")

    ChrTalk(    #11
        0xFE,
        "Sooo...where to go now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'm a wanderin' man. Go where\x01",
            "and when I please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "My feet and my heart are my\x01",
            "guide, and I live free.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD1")

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_AD1")

    ChrTalk(    #14
        0xFE,
        "Oh, good morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Nothing like starting the day\x01",
            "with a morning prayer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Close your eyes and you can\x01",
            "forget all about orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD1")

    TalkEnd(0xFE)
    Return()

    # Function_8_9A2 end

    def Function_9_AD5(): pass

    label("Function_9_AD5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_B9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B22")
    TurnDirection(0xFE, 0xC, 400)

    ChrTalk(    #17
        0xFE,
        (
            "Didi, sit still. We're almost\x01",
            "finished here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B98")

    label("loc_B22")

    OP_A2(0x3)

    ChrTalk(    #18
        0xFE,
        (
            "We came all this way...we should\x01",
            "all say a prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Goddess Aidios...thank you for\x01",
            "your gift of medicine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B98")

    Jump("loc_CBA")

    label("loc_B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C22")

    ChrTalk(    #20
        0xFE,
        (
            "Father Vixen's medicines always\x01",
            "work so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "It's times like these when I'm\x01",
            "truly thankful for the church.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C22")

    OP_A2(0x3)

    ChrTalk(    #22
        0xFE,
        (
            "I've come for some more medicine.\x01",
            "My neck and shoulders...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Everything gets so stiff that\x01",
            "the pain goes right on up to\x01",
            "my head lately.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)

    label("loc_CBA")

    TalkEnd(0xFE)
    Return()

    # Function_9_AD5 end

    def Function_10_CBE(): pass

    label("Function_10_CBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_CED")

    ChrTalk(    #24
        0xFE,
        "Knowles, that's a bad habit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D1B")

    ChrTalk(    #25
        0xFE,
        (
            "Mommy?\x01",
            "Mommy, are we finished?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_D88")

    ChrTalk(    #26
        0xFE,
        "Mommy? Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I think your shoulders' orbaldilly\x01",
            "energy pressure is too high,\x01",
            "Mommy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D88")

    TalkEnd(0xFE)
    Return()

    # Function_10_CBE end

    def Function_11_D8C(): pass

    label("Function_11_D8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E36")

    ChrTalk(    #28
        0xFE,
        "*gasp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "How could people just LEAVE\x01",
            "things all messy like this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I can't just leave it...!\x01",
            "The unevenness, the clutter...\x01",
            "It HURTS my braiiiiiin!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E36")

    TalkEnd(0xFE)
    Return()

    # Function_11_D8C end

    def Function_12_E3A(): pass

    label("Function_12_E3A")

    Call(0, 13)
    Return()

    # Function_12_E3A end

    def Function_13_E3F(): pass

    label("Function_13_E3F")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_EC3")

    ChrTalk(    #31
        0xE,
        (
            "If you ever have a need,\x01",
            "please feel welcome to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "The Septian Church is for everyone,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1023")

    label("loc_EC3")

    OP_A2(0x6)

    ChrTalk(    #33
        0xE,
        "Oh, it's you. Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xE,
        "Thank you so much for before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#001FThank you, too, Father.\x02\x03",

            "#006FThanks to you, Agate made\x01",
            "a total recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#010FWe very much appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "No need to thank me. I'm only\x01",
            "doing what I must.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        (
            "If you ever have a need,\x01",
            "please feel welcome to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        (
            "The Septian Church is for everyone,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1023")

    Jump("loc_228F")

    label("loc_1026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_13FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 1)), scpexpr(EXPR_END)), "loc_109C")

    ChrTalk(    #40
        0xE,
        (
            "Even if he's recovered from\x01",
            "the poison, his body is still\x01",
            "recuperating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xE,
        "We need only wait.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13FA")

    label("loc_109C")

    OP_A2(0x579)
    TurnDirection(0xE, 0x107, 0)

    ChrTalk(    #42
        0x107,
        (
            "#060FFather Vixen!\x02\x03",

            "Thank you for that medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        "Hello, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xE,
        (
            "Where are you headed after your\x01",
            "current job is done...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#052FMedicine...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x107,
        (
            "#061FThat's correct.\x02\x03",

            "Father Vixen here made the medicine\x01",
            "we gave you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x106,
        (
            "#053FIs that right...?\x02\x03",

            "...Sorry for the trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#509FYou suck at showing gratitude,\x01",
            "you know that, Agate?\x02\x03",

            "Why can't you just say\x01",
            "'thank you'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#015FPots and kettles, Estelle.\x01",
            "Be careful what you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xE,
        (
            "Still...you bracers are something else if\x01",
            "you're able to be up and about so soon\x01",
            "after getting so high a dosage of poison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xE,
        "Still, don't overdo things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x106,
        (
            "#050FYeah, yeah. That's good advice\x01",
            "for your body. Me, I'm fine.\x02\x03",

            "#053F...\x02\x03",

            "Umm...yes. Anyway, let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#000FOh, yeah. We should go.\x02\x03",

            "See you, Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xE,
        "Yes, goodbye.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        "Tita...stay strong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x107,
        (
            "#064F...\x02\x03",

            "#061F...Yes, Father!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_228F")

    label("loc_13FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_17BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 0)), scpexpr(EXPR_END)), "loc_147E")

    ChrTalk(    #57
        0xE,
        (
            "I'll be praying for Agate's full\x01",
            "and speedy recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        (
            "You're welcome here whenever\x01",
            "you wish to visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BB")

    label("loc_147E")

    OP_A2(0x578)

    ChrTalk(    #59
        0xE,
        "Oh, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xE,
        "Did the medicine work out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#010FYes, for the most part.\x02\x03",

            "According to Dr. Miriam at the\x01",
            "central factory, Agate is past\x01",
            "the worst of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xE,
        "I see. That is a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#000FYes, he ought to be fine.\x02\x03",

            "This is Agate we're talking about,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#019FIndeed.\x02\x03",

            "He's tough enough to give even\x01",
            "Zin a run for his money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#506FBut Father, we're real sorry for\x01",
            "bothering you so late.\x02\x03",

            "Making you stay up like that\x01",
            "putting the serum together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "My dear, anyone who saw little\x01",
            "Tita's face would have done\x01",
            "exactly the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xE,
        (
            "Seeing that shy little girl with\x01",
            "such a wild look about her\x01",
            "would spur anyone to action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xE,
        (
            "I'll be praying for Agate's full\x01",
            "and speedy recovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#001FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#010FWe deeply appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xE,
        (
            "You're welcome here whenever\x01",
            "you wish to visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BB")

    Jump("loc_228F")

    label("loc_17BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1864")

    ChrTalk(    #72
        0xE,
        (
            "At any rate, go back to the guild\x01",
            "and talk to the staff before going\x01",
            "to Limestone Cave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xE,
        (
            "There might be some record\x01",
            "from earlier collection trips.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228F")

    label("loc_1864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_194C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_18D2")

    ChrTalk(    #74
        0xE,
        "This is quite serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "We're going to all have to do\x01",
            "our best to get through this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1949")

    label("loc_18D2")

    OP_A2(0x6)

    ChrTalk(    #76
        0xE,
        "This is quite serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xE,
        (
            "There haven't been any reports\x01",
            "of injuries, but I should prepare\x01",
            "something anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1949")

    Jump("loc_228F")

    label("loc_194C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1A0B")

    ChrTalk(    #78
        0xE,
        (
            "And so it was that Zeiss, the\x01",
            "'Clock Maker's Town,' realized\x01",
            "its greater purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        (
            "The orbments they built spread\x01",
            "across the land, spurring the\x01",
            "Orbal Revolution of Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228F")

    label("loc_1A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1A5F")

    ChrTalk(    #80
        0xE,
        "O Aidios, Goddess of the Sky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        "Guide and protect your flock...\x02",
    )

    CloseMessageWindow()
    Jump("loc_228F")

    label("loc_1A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1B21")

    ChrTalk(    #82
        0xE,
        (
            "I understand Sister Kiera's desire\x01",
            "to preserve the church as a place\x01",
            "of prayer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xE,
        (
            "But I believe the church must\x01",
            "first be a place where the\x01",
            "troubled can come for help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C56")

    label("loc_1B21")

    OP_A2(0x6)

    ChrTalk(    #84
        0xE,
        (
            "Prescribing medical aid is one of\x01",
            "the church's equally important\x01",
            "functions as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xE,
        (
            "And we're not limited to medicine, but also\x01",
            "personal guidance or domestic advice. The\x01",
            "role we play in the community is a large one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        (
            "I feel these community services\x01",
            "are the very future of the Septian\x01",
            "Church.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C56")

    Jump("loc_228F")

    label("loc_1C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1F0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1CEE")

    ChrTalk(    #87
        0xE,
        (
            "I am always willing to listen if\x01",
            "you need someone to talk to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xE,
        (
            "If you have any problems, I welcome\x01",
            "you to bring them here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0A")

    label("loc_1CEE")

    OP_A2(0x6)
    TurnDirection(0xE, 0x107, 0)

    ChrTalk(    #89
        0xE,
        "Good morning, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        "There, there...no need to speak.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        (
            "Last night was quite hard for\x01",
            "you, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x107,
        "#065F*sob* I'm so sorry... *sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        (
            "There is nothing you need to\x01",
            "apologize for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xE,
        (
            "Experiments are vital to progress.\x01",
            "And sometimes experiments must\x01",
            "fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        "We all understand this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xE,
        (
            "Tita, make sure you are there\x01",
            "to support your grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x107,
        "#066FYes, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xE,
        (
            "I am always willing to listen if\x01",
            "you need someone to talk to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        (
            "If you have any problems, I welcome\x01",
            "you to bring them here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0A")

    Jump("loc_228F")

    label("loc_1F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_21DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1F97")

    ChrTalk(    #100
        0xE,
        (
            "If you need to talk, I am always\x01",
            "here, ready to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        (
            "The church is not solely a house\x01",
            "of prayers, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DA")

    label("loc_1F97")

    OP_A2(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD9")
    TurnDirection(0xE, 0x107, 0)

    ChrTalk(    #102
        0xE,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xE,
        "Is that young Tita I see?\x02",
    )

    CloseMessageWindow()
    Jump("loc_202A")

    label("loc_1FD9")


    ChrTalk(    #104
        0xE,
        "Hello, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xE,
        (
            "It feels like such a long time\x01",
            "since I've seen your face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202A")


    ChrTalk(    #106
        0x107,
        "#060FHello, Father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        (
            "It appears your grandfather is\x01",
            "as busy as he ever was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xE,
        (
            "When your work has slowed down\x01",
            "we'll be eagerly waiting for you\x01",
            "here at Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xE,
        (
            "You're still a child, Tita. I think it's\x01",
            "important for you to spend time\x01",
            "with other children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x107,
        "#060FYes, Father. I'll try.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        (
            "If you need to talk, I am always\x01",
            "here, ready to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xE,
        (
            "The church is not solely a house\x01",
            "of prayers, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DA")

    Jump("loc_228F")

    label("loc_21DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_228F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2227")

    ChrTalk(    #113
        0xE,
        (
            "Of course you're welcome to\x01",
            "come and pray any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_228F")

    label("loc_2227")

    OP_A2(0x6)

    ChrTalk(    #114
        0xE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xE,
        (
            "I am here to help you, with anything,\x01",
            "spiritual or mundane.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_228F")

    TalkEnd(0xE)
    Return()

    # Function_13_E3F end

    def Function_14_2293(): pass

    label("Function_14_2293")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2336")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_22EB")

    ChrTalk(    #116
        0xFE,
        "Please come back any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "Any time you're ready to pray.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2333")

    label("loc_22EB")

    OP_A2(0x7)

    ChrTalk(    #118
        0xFE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "I am always here to listen.\x02",
    )

    CloseMessageWindow()

    label("loc_2333")

    Jump("loc_2BBB")

    label("loc_2336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2414")

    ChrTalk(    #120
        0xFE,
        (
            "It appears the medicine worked.\x01",
            "Father Vixen is quite a wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Sometimes it seems as though\x01",
            "he is able to save anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I think maybe it's important for\x01",
            "the church to expand its wisdom\x01",
            "like that. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBB")

    label("loc_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_25D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_24D6")

    ChrTalk(    #123
        0xFE,
        (
            "At times like last night, I do feel\x01",
            "that Father Vixen's opinion is\x01",
            "perfectly valid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "But treating the church as an\x01",
            "apothecary is surely not a\x01",
            "proper show of respect?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D0")

    label("loc_24D6")

    OP_A2(0x7)

    ChrTalk(    #125
        0xFE,
        (
            "At times like last night, I feel\x01",
            "that Father Vixen's opinion is\x01",
            "perfectly valid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "If we show generosity to others,\x01",
            "they will surely show generosity\x01",
            "in return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "But treating the church as an\x01",
            "apothecary is not a proper\x01",
            "show of respect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D0")

    Jump("loc_2BBB")

    label("loc_25D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_26E1")

    ChrTalk(    #128
        0xFE,
        "Why, hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "What brings you here this\x01",
            "late at night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "I await your return.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Please be careful, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "Did you find the ingredients?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "The one who can actually mix\x01",
            "the ingredients is Father Vixen.\x01",
            "Please give them to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBB")

    label("loc_26E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_276D")

    ChrTalk(    #134
        0xFE,
        (
            "It certainly seems something\x01",
            "serious has happened at the\x01",
            "central factory...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "But I do not know all of the\x01",
            "circumstances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBB")

    label("loc_276D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_289F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_27E6")

    ChrTalk(    #136
        0xFE,
        (
            "The streets are especially\x01",
            "lively today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "The children can hardly keep\x01",
            "their attention inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_289C")

    label("loc_27E6")

    OP_A2(0x7)

    ChrTalk(    #138
        0xFE,
        (
            "Today's class will deal with the\x01",
            "history of our town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "But first...what is all this racket\x01",
            "coming from outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "The children can hardly keep\x01",
            "their attention inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289C")

    Jump("loc_2BBB")

    label("loc_289F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2927")

    ChrTalk(    #141
        0xFE,
        (
            "I thought someone had come,\x01",
            "but they only needed medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Father Vixen is too lax on the\x01",
            "lack of proper prayers...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBB")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2AB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_29C7")

    ChrTalk(    #143
        0xFE,
        (
            "I believe a church is a house\x01",
            "of prayers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "Currently though, the church is\x01",
            "more like a tourist attraction\x01",
            "or better yet, a drugstore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB1")

    label("loc_29C7")

    OP_A2(0x7)

    ChrTalk(    #145
        0xFE,
        (
            "The people of Zeiss are too busy\x01",
            "with their daily lives to come to\x01",
            "the church and pray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Father Vixen has been trying to\x01",
            "attract people by offering more\x01",
            "community services...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I believe a church is a house\x01",
            "of prayers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB1")

    Jump("loc_2BBB")

    label("loc_2AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2B6D")

    ChrTalk(    #148
        0xFE,
        (
            "Last night was quite a\x01",
            "dangerous affair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "The central factory looked like\x01",
            "it was in total uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Such times of anxiety are best\x01",
            "remedied by a calming prayer...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBB")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BBB")

    ChrTalk(    #151
        0xFE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "Please approach and pray.\x02",
    )

    CloseMessageWindow()

    label("loc_2BBB")

    TalkEnd(0xFE)
    Return()

    # Function_14_2293 end

    SaveToFile()

Try(main)
