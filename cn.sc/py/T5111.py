from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T5111   ._SN',
        MapName             = 'Other',
        Location            = 'T5111.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '亚妮拉丝',                             # 9
        '克鲁茨',                               # 10
        '维修师罗伯特',                         # 11
        '菲莉斯管理员',                         # 12
        '猎兵',                                 # 13
        '女猎兵',                               # 14
        '发烟筒用目标角色',                     # 15
        '目标用照相机',                         # 16
        '器皿',                                 # 17
        '器皿',                                 # 18
        '器皿',                                 # 19
        '咖啡',                                 # 20
        '咖啡',                                 # 21
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
        'ED6_DT27/CH03090 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT27/CH03093 ._CH',             # 02
        'ED6_DT07/CH00411 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT27/CH03900 ._CH',             # 05
        'ED6_DT07/CH00341 ._CH',             # 06
        'ED6_DT07/CH00261 ._CH',             # 07
        'ED6_DT06/CH20008 ._CH',             # 08
        'ED6_DT06/CH20020 ._CH',             # 09
        'ED6_DT07/CH00414 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT06/CH20021 ._CH',             # 0C
        'ED6_DT07/CH01620 ._CH',             # 0D
        'ED6_DT27/CH04000 ._CH',             # 0E
        'ED6_DT07/CH00420 ._CH',             # 0F
        'ED6_DT27/CH04820 ._CH',             # 10
        'ED6_DT27/CH04821 ._CH',             # 11
        'ED6_DT27/CH04640 ._CH',             # 12
        'ED6_DT27/CH04641 ._CH',             # 13
        'ED6_DT06/CH20067 ._CH',             # 14
        'ED6_DT27/CH04001 ._CH',             # 15
        'ED6_DT07/CH00421 ._CH',             # 16
        'ED6_DT27/CH03005 ._CH',             # 17
        'ED6_DT27/CH03093 ._CH',             # 18
        'ED6_DT27/CH03133 ._CH',             # 19
        'ED6_DT27/CH03091 ._CH',             # 1A
        'ED6_DT27/CH04824 ._CH',             # 1B
        'ED6_DT26/CH20265 ._CH',             # 1C
        'ED6_DT26/CH20267 ._CH',             # 1D
    )

    AddCharChipPat(
        'ED6_DT27/CH03090P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT27/CH03093P._CP',             # 02
        'ED6_DT07/CH00411P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT27/CH03900P._CP',             # 05
        'ED6_DT07/CH00341P._CP',             # 06
        'ED6_DT07/CH00261P._CP',             # 07
        'ED6_DT06/CH20008P._CP',             # 08
        'ED6_DT06/CH20000P._CP',             # 09
        'ED6_DT07/CH00414P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT06/CH20021P._CP',             # 0C
        'ED6_DT07/CH01620P._CP',             # 0D
        'ED6_DT27/CH04000P._CP',             # 0E
        'ED6_DT07/CH00420P._CP',             # 0F
        'ED6_DT27/CH04820P._CP',             # 10
        'ED6_DT27/CH04821P._CP',             # 11
        'ED6_DT27/CH04640P._CP',             # 12
        'ED6_DT27/CH04641P._CP',             # 13
        'ED6_DT06/CH20067P._CP',             # 14
        'ED6_DT27/CH04001P._CP',             # 15
        'ED6_DT07/CH00421P._CP',             # 16
        'ED6_DT27/CH03005P._CP',             # 17
        'ED6_DT27/CH03093P._CP',             # 18
        'ED6_DT27/CH03133P._CP',             # 19
        'ED6_DT27/CH03091P._CP',             # 1A
        'ED6_DT27/CH04824P._CP',             # 1B
        'ED6_DT26/CH20265P._CP',             # 1C
        'ED6_DT26/CH20267P._CP',             # 1D
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
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 26690,
        Z                   = 0,
        Y                   = 5140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 12470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900553,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65547,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65547,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65547,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638411,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 120250,
        Y                   = 0,
        Z                   = 1000,
        Range               = 123170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 25470,
        TriggerZ            = -300,
        TriggerY            = 4940,
        TriggerRange        = 800,
        ActorX              = 26690,
        ActorZ              = 1500,
        ActorY              = 5140,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22500,
        TriggerZ            = 0,
        TriggerY            = 12360,
        TriggerRange        = 800,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 12470,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85780,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 800,
        ActorX              = 85180,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3C6",          # 00, 0
        "Function_1_4B1",          # 01, 1
        "Function_2_522",          # 02, 2
        "Function_3_5C9",          # 03, 3
        "Function_4_A45",          # 04, 4
        "Function_5_C03",          # 05, 5
        "Function_6_C08",          # 06, 6
        "Function_7_DE8",          # 07, 7
        "Function_8_DED",          # 08, 8
        "Function_9_1106",         # 09, 9
        "Function_10_1B99",        # 0A, 10
        "Function_11_238C",        # 0B, 11
        "Function_12_2FA0",        # 0C, 12
    )


    def Function_0_3C6(): pass

    label("Function_0_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0x10, 18160, 800, 11990, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, 17670, 800, 12040, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 17600, 800, 11180, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x14, 18270, 750, 10980, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x12, 18190, 750, 11550, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 115820, 0, 39550, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 88540, 200, -30700, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 25)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499")
    Event(0, 9)

    label("loc_499")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_END)), "loc_4B0")
    Event(0, 11)

    label("loc_4B0")

    Return()

    # Function_0_3C6 end

    def Function_1_4B1(): pass

    label("Function_1_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C4")
    OP_64(0x2, 0x1)
    Jump("loc_4C8")

    label("loc_4C4")

    OP_65(0x2, 0x1)

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF")
    OP_72(0x0, 0x20)
    OP_70(0x19, 0x0)
    Jump("loc_4EB")

    label("loc_4DF")

    OP_72(0x0, 0x20)
    OP_6F(0x19, 60)

    label("loc_4EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x397), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_521")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_521")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_521")

    Return()

    # Function_1_4B1 end

    def Function_2_522(): pass

    label("Function_2_522")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_553"),
        (1, "loc_55F"),
        (2, "loc_56B"),
        (3, "loc_577"),
        (4, "loc_583"),
        (5, "loc_58F"),
        (6, "loc_59B"),
        (SWITCH_DEFAULT, "loc_5A7"),
    )


    label("loc_553")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5B3")

    label("loc_55F")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5B3")

    label("loc_56B")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5B3")

    label("loc_577")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5B3")

    label("loc_583")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B3")

    label("loc_58F")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5B3")

    label("loc_59B")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B3")

    label("loc_5A7")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B3")

    label("loc_5B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B3")

    label("loc_5C8")

    Return()

    # Function_2_522 end

    def Function_3_5C9(): pass

    label("Function_3_5C9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_659")
    Jump("loc_69B")

    label("loc_659")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_675")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69B")

    label("loc_675")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_691")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69B")

    label("loc_691")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69B")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B6")
    OP_A2(0x1039)

    ChrTalk(    #0
        0x9,
        "#840F哟，是艾丝蒂尔啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000F嘿嘿，晚上好。\x02\x03",

            "克鲁茨前辈在看书？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#840F嗯嗯，正在复习\x01",
            "东方的兵书呢。\x02\x03",

            "虽然记载的是古代战争，\x01",
            "但我们也能从中学到不少。\x02\x03",

            "建议你也看一看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1016F唔，嗯～对我来说\x01",
            "大概有点难。\x02\x03",

            "#1015F不过，东方的兵书啊……\x02\x03",

            "……那个，克鲁茨前辈\x01",
            "难道是东方出身的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#843F嗯，出身虽是利贝尔，\x01",
            "但原本好像是来自东方的家族。\x02\x03",

            "据说我祖父那代是\x01",
            "从那边远道移民而来的。\x02\x03",

            "#840F我施展的方术也是祖父\x01",
            "传授的家传秘技。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F啊，是这样啊……\x02\x03",

            "这么方便的法术，\x01",
            "我说怎么从来没见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#844F确实在利贝尔\x01",
            "没见过除我之外的使用者……\x02\x03",

            "#840F你要是有心，艾丝蒂尔。\x01",
            "传授给你怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004F真、真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#840F啊啊，当然是真的。\x02\x03",

            "不过，在那之前需要\x01",
            "读破万卷兵书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1007F又受打击了…………\x02\x03",

            "我，我办不到啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C")

    label("loc_9B6")


    ChrTalk(    #10
        0x9,
        (
            "#840F古代的书里\x01",
            "隐藏着大量值得学习的智慧。\x02\x03",

            "如果有机会可别对它们敬而远之，\x01",
            "还是多多接触才好。\x02\x03",

            "广泛增长见识\x01",
            "也是游击士所必须的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3C")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_3_5C9 end

    def Function_4_A45(): pass

    label("Function_4_A45")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB8")
    OP_A2(0x1038)

    ChrTalk(    #11
        0x8,
        (
            "#814F啊，艾丝蒂尔。\x01",
            "还没休息啊。\x02\x03",

            "难道你\x01",
            "在准备明天的训练？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1011F啊，嗯。\x01",
            "准备是有准备啦……\x02\x03",

            "亚妮拉丝在做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#810F嗯，和小熊们\x01",
            "稍微说说话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F小、小熊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#1310F很可爱吧？\x02\x03",

            "#1311F啊～这蓬蓬松松\x01",
            "又柔软无比～的毛……\x02\x03",

            "只是摸摸\x01",
            "就精神十足哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "这就是亚妮拉丝\x01",
            "的精神之源啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#816F嗯！就是这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFF")

    label("loc_BB8")


    ChrTalk(    #18
        0x8,
        (
            "#1311F啊～抱着玩偶\x01",
            "就能被治愈呢。\x02\x03",

            "#811F嗯！果然\x01",
            "可爱就是正义啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFF")

    TalkEnd(0x8)
    Return()

    # Function_4_A45 end

    def Function_5_C03(): pass

    label("Function_5_C03")

    Call(0, 6)
    Return()

    # Function_5_C03 end

    def Function_6_C08(): pass

    label("Function_6_C08")

    TalkBegin(0xB)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_C28")
    OP_A9(0xFC)
    Jump("loc_C2A")

    label("loc_C28")

    OP_A9(0xFF)

    label("loc_C2A")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_C33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C44")
    TalkEnd(0xB)
    Return()

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D92")
    OP_A2(0x1036)

    ChrTalk(    #19
        0xB,
        (
            "哎呀，艾丝蒂尔。\x01",
            "演习辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "哈哈哈，看这表情\x01",
            "似乎相当地严苛呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1007F嗯，全身都快散架了。\x02\x03",

            "#1006F不过，训练还在继续。\x01",
            "这点程度得要忍受下去才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "嗯嗯，就是这种气势㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        (
            "那么，为了明天\x01",
            "还得补充装备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "早上来做就太匆忙了，\x01",
            "最好是趁现在就做好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1011F啊，嗯。\x02\x03",

            "那么，麻烦\x01",
            "再给我看看道具。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE4")

    label("loc_D92")


    ChrTalk(    #26
        0xB,
        (
            "为了明天的训练趁现在\x01",
            "补充一下装备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "早上再做的话，\x01",
            "匆匆忙忙挺麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE4")

    TalkEnd(0xB)
    Return()

    # Function_6_C08 end

    def Function_7_DE8(): pass

    label("Function_7_DE8")

    Call(0, 8)
    Return()

    # Function_7_DE8 end

    def Function_8_DED(): pass

    label("Function_8_DED")

    TalkBegin(0xA)
    OP_A2(0x1007)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x2D6, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF6")

    ChrTalk(    #28
        0xA,
        (
            "啊，艾丝蒂尔……\x01",
            "得到『天眼』了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "那可是所谓的\x01",
            "高级结晶回路呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "要安装的话\x01",
            "需要强化结晶孔才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "虽然需要相应的耀晶片，\x01",
            "但能提高最大ＥＰ，所以推荐试试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "工房的菜单里\x01",
            "选[改造·换钱]-[结晶孔]\x01",
            "就能强化结晶孔。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x1041)
    TalkEnd(0xA)
    Return()

    label("loc_EF6")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "买东西\x01",          # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F")
    OP_0D()
    OP_A9(0xFA)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_F5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78")
    OP_0D()
    OP_A9(0xFB)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_F78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F89")
    TalkEnd(0xA)
    Return()

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1001")

    ChrTalk(    #33
        0xA,
        (
            "没有强化过的结晶孔\x01",
            "是不能安装高级结晶回路的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "强化结晶孔需要耀晶片，\x01",
            "但能提高最大ＥＰ，就试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1102")

    label("loc_1001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A6")
    OP_A2(0x1)

    ChrTalk(    #35
        0xA,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "今天的演习中应该也\x01",
            "得到了一些耀晶片吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "可以的话就试着\x01",
            "合成新结晶回路看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "为了适应新型导力器\x01",
            "不断尝试也很重要哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1102")

    label("loc_10A6")


    ChrTalk(    #39
        0xA,
        (
            "可以的话就试着\x01",
            "合成新结晶回路看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "总之与其学习不如习惯。\x01",
            "不断尝试也很重要哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1102")

    TalkEnd(0xA)
    Return()

    # Function_8_DED end

    def Function_9_1106(): pass

    label("Function_9_1106")

    EventBegin(0x0)
    OP_70(0x19, 0x0)
    OP_6D(27560, 0, 11600, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 18080, 200, 12890, 180)
    SetChrPos(0x101, 18120, 200, 10470, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x10A, 2)
    SetChrPos(0x10, 18160, 800, 11990, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, 17670, 800, 12040, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 17600, 800, 11180, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x14, 18270, 800, 10980, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x12, 18190, 800, 11550, 0)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)

    def lambda_1209():
        OP_6D(18250, 200, 11830, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1209)

    def lambda_1221():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1221)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #41
        0x10A,
        (
            "#819F#5P唉……\x01",
            "今天真是严苛啊。\x02\x03",

            "#810F不过，在这里的训练\x01",
            "也差不多快结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1015F嗯～\x01",
            "好像又高兴，又遗憾。\x02\x03",

            "#1011F不过话说回来……\x01",
            "克鲁茨前辈相当强吧？\x02\x03",

            "即使面对我们２人\x01",
            "还绰绰有余的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        (
            "#811F#5P啊哈哈，那当然了。\x02\x03",

            "#816F说到『方术使』克鲁茨\x01",
            "那可是利贝尔游击士的ＮＯ．２啊。\x02\x03",

            "第一就不用说了，\x01",
            "当然是艾丝蒂尔的爸爸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1025F啊……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#810F#5P顺带一提，正游击士的等级\x01",
            "从Ｇ到Ａ有７级。\x02\x03",

            "比如说我，花了半年\x01",
            "才终于升级到Ｆ……\x02\x03",

            "克鲁茨前辈可是马上\x01",
            "要从Ｂ升级到Ａ了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1011F啊，Ａ级的话\x01",
            "就和金先生一样了呢。\x02\x03",

            "#1003F（不过，让那么厉害的克鲁茨前辈\x01",
            "失忆的犯人……）\x02\x03",

            "（我……能阻止吗……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        (
            "#814F#5P……艾丝蒂尔？\x02\x03",

            "怎么了，一脸严肃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1004F啊……\x02\x03",

            "#1013F抱、抱歉。\x01",
            "稍微发了会儿呆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10A,
        (
            "#812F#5P………………………………\x02\x03",

            "难道…\x01",
            "在想约修亚的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1013F啊……\x02\x03",

            "#1025F嗯，算是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        (
            "#1314F#5P是吗……\x02\x03",

            "我从雪拉前辈\x01",
            "那里稍微听说了点情况……\x02\x03",

            "你很担心他吧……\x01",
            "现在，在哪里呢?在干什么呢?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1003F……嗯。\x02\x03",

            "#1006F不过，没关系！\x01",
            "不用太担心啦。\x02\x03",

            "反正约修亚\x01",
            "只不过是一个自己在胡乱\x01",
            "钻牛角尖的离家小孩……\x02\x03",

            "#1005F我一定要找到他，\x01",
            "用绳子套住他的脖子拖回来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        (
            "#811F#5P对了，就是这股气势！\x02\x03",

            "#816F艾丝蒂尔只要有这种气势，\x01",
            "就绝对能够找到约修亚的！\x02\x03",

            "姐姐向你保证哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1016F哈哈，谢谢你啦。\x02\x03",

            "#1015F啊，不过……\x01",
            "亚妮拉丝前辈可没什么\x01",
            "姐姐的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10A,
        (
            "#812F#5P啊～好过分，艾丝蒂尔。\x02\x03",

            "你一直觉得\x01",
            "我很孩子气对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1008F（这……）\x01",
            "哪、哪有～那倒不至于啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10A,
        (
            "#1316F#5P嗯，再怎么说，\x01",
            "我也比你大两岁啊。\x02\x03",

            "#810F不过算了，与其被看作前辈，\x01",
            "不如以朋友的身份交往要更开心一点。\x02\x03",

            "#811F呵呵，今后就请多指教啰？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1008F啊……\x01",
            "嗯，彼此彼此！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 0)
    ClearChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 19230, 0, 12970, 98)
    OP_0D()
    SetChrSubChip(0x101, 2)
    TurnDirection(0x10A, 0x101, 400)
    Sleep(500)

    ChrTalk(    #59
        0x10A,
        (
            "#810F#5P好了～也该休息了，\x01",
            "明天还要早起呢。\x02\x03",

            "今天也很累了。\x01",
            "明天的晨练，还能参加吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1006F啊，那没关系的。\x02\x03",

            "我无论多累\x01",
            "第二天都会没事的。\x02\x03",

            "只要亚妮拉丝前辈还撑得住，\x01",
            "多少个回合都奉陪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10A,
        (
            "#811F#5P太好了，就是要这样。\x02\x03",

            "#1310F那就晚安了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1011F嗯，晚安。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10A, 0x5154, 0x0, 0x2472, 0xBB8, 0x0)

    def lambda_19C9():
        OP_8E(0x10A, 0x6CAC, 0x7D0, 0x2346, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_19C9)

    def lambda_19E4():
        OP_6D(20870, 200, 10700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19E4)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x1)

    def lambda_1A06():
        OP_8E(0x10A, 0x6C84, 0x7D0, 0x2ABC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A06)
    WaitChrThread(0x10A, 0x1)

    def lambda_1A26():
        OP_8E(0x10A, 0x63D8, 0xDAC, 0x2C1A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A26)

    def lambda_1A41():
        OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1A41)
    WaitChrThread(0x10A, 0x1)

    def lambda_1A58():
        OP_69(0x101, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A58)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x10A, 0x80)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #63
        0x101,
        (
            "#1012F#5P好了……\x01",
            "我也该回房间休息了。\x02\x03",

            "#1015F啊，对了。\x01",
            "演习时候得到了很多耀晶片。\x02\x03",

            "#1006F想准备点新的结晶回路，\x01",
            "睡觉前先去工房看看吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(19120, 0, 10210, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 19120, 0, 10210, 103)
    RemoveParty(0x9, 0xFF)
    OP_A2(0x100B)
    OP_28(0x7E, 0x1, 0x100)
    OP_28(0x7E, 0x1, 0x200)
    OP_28(0x7E, 0x1, 0x400)
    OP_28(0x7E, 0x1, 0x800)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_1106 end

    def Function_10_1B99(): pass

    label("Function_10_1B99")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【暂时还不休息】\x01",        # 0
            "【今天可以休息了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C05")
    EventEnd(0x0)
    Return()

    label("loc_1C05")


    ChrTalk(    #64
        0x101,
        (
            "#1007F啊，快累瘫了……\x02\x03",

            "#1000F为了明天\x01",
            "还是赶快去睡吧……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x3E8)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_0D()
    Sleep(5000)
    SetChrFlags(0x8, 0x80)
    OP_22(0x1F7, 0x0, 0x1E)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x28)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x23)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x28)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x2D)
    Sleep(400)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x3C)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x37)
    Sleep(300)
    OP_22(0x20F, 0x0, 0x4B)
    Sleep(800)
    OP_22(0x1F7, 0x0, 0x4B)
    Sleep(300)
    OP_22(0x246, 0x0, 0x5A)
    Sleep(800)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(400)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, 85170, 300, 42180, 180)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #65
        0x101,
        (
            "#5P#455F（嗯……？）\x02\x03",

            "#452F（这是……什么声音……）\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【马上起来】\x01",          # 0
            "【不管它继续睡】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20EF")

    ChrTalk(    #66
        0x101,
        (
            "#459F（嗯－……好困啊……）\x02\x03",

            "#455F（……不行……爬不起来……）\x02\x03",

            "（…………………………………）\x02\x03",

            "#456F……丝……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x72, 0x0, 0x64)
    Sleep(300)
    Sleep(1000)
    SetChrPos(0x8, 86790, 0, 33860, 0)

    NpcTalk(    #67
        0x8,
        "女孩的声音",
        "#40W#5P………蒂尔………\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    NpcTalk(    #68
        0x8,
        "女孩的声音",
        (
            "#40W#5P……艾丝蒂尔……\x01",
            "…………………快起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#459F#5P………？…………\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    OP_22(0x1B, 0x0, 0x3C)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x3C)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x46)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x46)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x50)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x50)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x5A)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x5A)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x8, 86100, 0, 41700, 270)
    OP_44(0x8, 0x0)
    Sleep(500)

    ChrTalk(    #70
        0x8,
        (
            "#5P#3S……起来啦！\x01",
            "艾丝蒂尔！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#453F！！！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 86510, 0, 40980, 259)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 60)
    OP_70(0x0, 0x14)
    OP_99(0x101, 0x0, 0x8, 0x4B0)
    OP_99(0x101, 0x11, 0x12, 0x4B0)
    SetChrSubChip(0x101, 23)

    ChrTalk(    #72
        0x101,
        (
            "#453F啊……\x01",
            "亚妮拉丝……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#2P#812F艾丝蒂尔，起来啦！\x02\x03",

            "好，赶快准备吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#451F怎、怎么了？\x01",
            "神色那么慌张……\x02\x03",

            "而且这个声音……\x01",
            "……难道是枪声！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#2P#815F虽然不明白发生了什么\x01",
            "但好像是有什么人来袭击了！\x02\x03",

            "克鲁茨前辈正在应战\x01",
            "艾丝蒂尔也赶快吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EC")

    label("loc_20EF")

    OP_2B(0x7E, 0x3)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 60)
    OP_70(0x0, 0x14)
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    OP_99(0x101, 0x11, 0x12, 0x3E8)

    ChrTalk(    #76
        0x101,
        (
            "#451F这是什么声音……\x02\x03",

            "#453F难道是枪声！？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x72, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x8, 86790, 0, 33860, 0)

    ChrTalk(    #77
        0x8,
        (
            "#1P……艾丝蒂尔！\x02\x03",

            "艾丝蒂尔，起来了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)
    Sleep(200)
    SetChrPos(0x8, 86530, 0, 35990, 0)
    OP_9F(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 26)

    def lambda_21EF():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_21EF)
    OP_8E(0x8, 0x15202, 0x0, 0x9B64, 0xFA0, 0x0)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x101, 23)

    ChrTalk(    #78
        0x101,
        "#451F亚妮拉丝！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#2P#812F太好了！\x01",
            "你醒啦！\x02\x03",

            "好，赶快准备吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#451F嗯、嗯！\x02\x03",

            "这个枪声不会是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#2P#815F虽然不清楚怎么了，\x01",
            "但好像是有什么人来袭击了！\x02\x03",

            "克鲁茨前辈正在应战，\x01",
            "艾丝蒂尔也赶快吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EC")

    OP_1D(0x29)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(86600, 0, 40930, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 86600, 0, 40930, 180)
    SetChrFlags(0x8, 0x80)
    AddParty(0x9, 0xF7, 0xFF)
    Sleep(500)
    OP_A2(0x100C)
    OP_28(0x7F, 0x4, 0x2)
    OP_28(0x7F, 0x4, 0x8)
    OP_28(0x7F, 0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1B99 end

    def Function_11_238C(): pass

    label("Function_11_238C")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0xB, 0x0)
    SetChrPos(0x101, 27210, 2000, 9020, 253)
    SetChrPos(0x10A, 28160, 2000, 8910, 262)
    SetChrPos(0xA, 18980, -300, 5950, 166)
    SetChrPos(0xB, 17150, -300, 5260, 170)
    SetChrPos(0x9, 19400, -550, 370, 0)
    SetChrPos(0xC, 20970, 0, 18840, 176)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    TurnDirection(0xA, 0x9, 1000)
    TurnDirection(0xB, 0x9, 1000)

    def lambda_2431():

        label("loc_2431")

        TurnDirection(0xA, 0x9, 0)
        OP_48()
        Jump("loc_2431")

    QueueWorkItem2(0xA, 1, lambda_2431)

    def lambda_2442():

        label("loc_2442")

        TurnDirection(0xB, 0x9, 0)
        OP_48()
        Jump("loc_2442")

    QueueWorkItem2(0xB, 1, lambda_2442)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_9F(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    def lambda_24A1():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_24A1)
    OP_8E(0x9, 0x4BC8, 0xFFFFFDDA, 0x73A, 0x3E8, 0x0)
    Sleep(500)
    OP_8C(0x9, 180, 2000)
    Sleep(500)
    WaitChrThread(0x9, 0x1)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0x9,
        (
            "#847F唔……\x01",
            "这下暂且……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 10)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x9, 0x0, 0x3, 0x4B0)

    ChrTalk(    #83
        0xA,
        "#5P没、没事吗！？\x02",
    )

    CloseMessageWindow()

    def lambda_2534():
        OP_8E(0xB, 0x4934, 0xFFFFFDDA, 0x898, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2534)
    Sleep(500)

    def lambda_2554():
        OP_8E(0xA, 0x4A06, 0xFFFFFED4, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2554)
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 125, 500)

    ChrTalk(    #84
        0xB,
        (
            "#5P不、不得了！\x01",
            "手臂受伤了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "#844F没关系……\x01",
            "只是擦伤……\x02\x03",

            "别说这个了……\x01",
            "赶快抵御敌人的入侵……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25E6():
        OP_6D(21710, 0, 8600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25E6)

    def lambda_25FE():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25FE)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10A, 0x80)

    def lambda_2620():
        OP_8E(0x101, 0x54CE, 0x0, 0x2198, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2620)
    Sleep(200)

    def lambda_2640():
        OP_8E(0x10A, 0x5A8C, 0x0, 0x229C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2640)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x9, 1000)
    TurnDirection(0x10A, 0x9, 1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #86
        0x101,
        "#1020F#5P克、克鲁茨前辈！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        (
            "#815F#5P前、前辈！？\x01",
            "受伤了吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 1000)
    TurnDirection(0xA, 0x101, 1000)

    ChrTalk(    #88
        0xB,
        (
            "#1P艾丝蒂尔！\x01",
            "亚妮拉丝！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_271A():
        OP_6D(19720, -300, 3340, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_271A)

    def lambda_2732():
        OP_8E(0x101, 0x4D08, 0xFFFFFED4, 0xD0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2732)
    Sleep(200)

    def lambda_2752():
        OP_8E(0x10A, 0x51D6, 0xFFFFFED4, 0xC3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_2752)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0xB, 0x9, 500)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x2)
    TurnDirection(0x101, 0x9, 1000)
    TurnDirection(0x10A, 0x9, 1000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 1)

    ChrTalk(    #89
        0x9,
        (
            "#844F抱歉，一时大意……\x02\x03",

            "你们都看到了，武装集团\x01",
            "袭击了这建筑……\x02\x03",

            "你们俩快协助迎击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1005F明、明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        (
            "#813F#5P怎么会……\x01",
            "居然让前辈受伤……\x02\x03",

            "#815F是谁在攻击！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "#844F刚才稍微交过手……\x02\x03",

            "那个样子……\x01",
            "恐怕是『猎兵团』中的一支部队吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #93
        0x101,
        (
            "#1004F猎兵团……\x01",
            "那些身经百战的佣兵们！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10A,
        (
            "#1317F#5P但、但是……\x01",
            "为什么他们会！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#844F利贝尔国外\x01",
            "游击士协会和猎兵团\x01",
            "常因一些事情而对立……\x02\x03",

            "这里成为他们的靶子\x01",
            "也并不奇怪……\x02\x03",

            "#843F难不成……\x01",
            "又是那个结社做的手脚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1020F哎！？\x02",
    )

    CloseMessageWindow()
    OP_22(0x134, 0x0, 0x64)
    OP_72(0x19, 0x20)
    OP_6F(0x19, 0)
    OP_70(0x19, 0x3C)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_2A60():
        OP_6D(21830, 0, 13880, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A60)

    def lambda_2A78():
        TurnDirection(0x101, 0xC, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A78)

    def lambda_2A86():
        TurnDirection(0x10A, 0xC, 600)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2A86)

    def lambda_2A94():
        TurnDirection(0xA, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A94)

    def lambda_2AA2():
        TurnDirection(0xB, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2AA2)
    Sleep(800)
    SetChrChipByIndex(0xC, 17)
    OP_9F(0xC, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)

    def lambda_2ACF():
        OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2ACF)
    OP_96(0xC, 0x52D0, 0x0, 0x3A7A, 0x7D0, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xC, 16)
    Sleep(500)

    ChrTalk(    #97
        0x10A,
        "#1P#1317F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1P#1005F糟了！\x02",
    )

    CloseMessageWindow()

    def lambda_2B33():
        OP_6D(21130, 0, 9590, 800)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2B33)
    SetChrChipByIndex(0xC, 17)

    def lambda_2B50():
        OP_8E(0xC, 0x51B8, 0x0, 0x2774, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B50)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x10A, 22)
    SetChrSubChip(0x10A, 0)

    def lambda_2B89():
        OP_8E(0x101, 0x512C, 0xFFFFFED4, 0x1D2E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B89)
    Sleep(100)

    def lambda_2BA9():
        OP_8E(0x10A, 0x55DC, 0xFFFFFED4, 0x1D6A, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2BA9)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2C12"),
        (0, "loc_2C1F"),
        (SWITCH_DEFAULT, "loc_2C2C"),
    )


    label("loc_2C12")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C2C")

    label("loc_2C1F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C2C")

    label("loc_2C2C")

    EventBegin(0x0)
    OP_72(0x19, 0x20)
    OP_72(0x19, 0x8)
    OP_6F(0x19, 60)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C55")
    OP_28(0x7F, 0x1, 0x40)
    Jump("loc_2F96")

    label("loc_2C55")

    OP_2B(0x7E, 0x3)
    OP_6D(21510, 0, 12500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0xB, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x101, 20540, 0, 9660, 0)
    SetChrChipByIndex(0x101, 14)
    SetChrPos(0x10A, 21750, 0, 9710, 0)
    SetChrChipByIndex(0x10A, 15)
    SetChrPos(0xC, 21300, 0, 14260, 170)
    SetChrPos(0xD, 21060, 0, 18750, 182)
    SetChrChipByIndex(0xC, 27)
    SetChrSubChip(0xC, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #99
        0x101,
        (
            "#6P#1002F呼呼……\x01",
            "总、总算是赢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10A,
        (
            "#815F#4P那、那边的人！\x01",
            "快放下武器投降吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xC,
        (
            "#2P#5P呵呵……\x01",
            "比想象中的还能干呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xC,
        "#2P#5P只不过在最后关头，你们太天真了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10A,
        "#814F#4P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_2DDC():
        OP_6D(21490, 0, 14710, 1200)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2DDC)

    def lambda_2DF4():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DF4)
    SetChrChipByIndex(0xD, 19)
    SetChrSubChip(0xD, 2)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x80)
    OP_96(0xD, 0x4F1A, 0x0, 0x3B4C, 0x7D0, 0x1B58)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xD, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_99(0xC, 0x3, 0x0, 0x708)
    SetChrChipByIndex(0xC, 16)
    SetChrChipByIndex(0xD, 28)
    SetChrFlags(0xD, 0x2)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0xE, 21290, 0, 11110, 13)

    def lambda_2E83():
        OP_99(0xFE, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E83)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xD, 250, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    Sleep(300)

    def lambda_2ED2():
        OP_6D(21360, 0, 11490, 1000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_2ED2)
    Sleep(1000)
    OP_22(0x7F, 0x0, 0x64)
    Sleep(500)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_71(0xD, 0x4)
    Sleep(2000)

    ChrTalk(    #104
        0x10A,
        "#1317F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#6P#1020F发、发烟筒！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xD,
        "#5P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        "#5P睡吧，小猫咪们。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    Sleep(1000)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 16777215)
    Sleep(1000)
    OP_28(0x7F, 0x1, 0x10)

    label("loc_2F96")

    NewScene("ED6_DT21/C5504   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_238C end

    def Function_12_2FA0(): pass

    label("Function_12_2FA0")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    AnonymousTalk(    #108
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_12_2FA0 end

    SaveToFile()

Try(main)
