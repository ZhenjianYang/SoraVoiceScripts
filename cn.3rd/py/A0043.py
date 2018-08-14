from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0043   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
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
        '3250约修亚 走',                        # 9
        '3251约修亚 跑',                        # 10
        '3253约修亚 坐',                        # 11
        '3254约修亚 倒下',                      # 12
        '3255约修亚 弯腰',                      # 13
        '3240雪拉 走',                          # 14
        '3241雪拉 跑',                          # 15
        '3243雪拉 坐',                          # 16
        '3244雪拉 倒下',                        # 17
        '3245雪拉 弯腰',                        # 18
        '3260奥利维尔 走',                      # 19
        '3261奥利维尔 跑',                      # 20
        '3263奥利维尔 坐',                      # 21
        '3264奥利维尔 倒下',                    # 22
        '3265奥利维尔 弯腰',                    # 23
        '3230雪拉18岁 走',                      # 24
        '3231雪拉18岁 跑',                      # 25
        '3233雪拉18岁 坐',                      # 26
        '3235雪拉18岁 弯腰',                    # 27
        '3270乔丝特 走',                        # 28
        '3271乔丝特 跑',                        # 29
        '3273乔丝特 坐',                        # 30
        '3150莉丝 走',                          # 31
        '3151莉丝 跑',                          # 32
        '3153莉丝 坐',                          # 33
        '3154莉丝 倒下',                        # 34
        '3155莉丝 弯腰',                        # 35
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = 2000,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT27/CH03250 ._CH',             # 00
        'ED6_DT27/CH03251 ._CH',             # 01
        'ED6_DT27/CH03253 ._CH',             # 02
        'ED6_DT27/CH03254 ._CH',             # 03
        'ED6_DT27/CH03255 ._CH',             # 04
        'ED6_DT27/CH03240 ._CH',             # 05
        'ED6_DT27/CH03241 ._CH',             # 06
        'ED6_DT27/CH03243 ._CH',             # 07
        'ED6_DT27/CH03244 ._CH',             # 08
        'ED6_DT27/CH03245 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT27/CH03261 ._CH',             # 0B
        'ED6_DT27/CH03263 ._CH',             # 0C
        'ED6_DT27/CH03264 ._CH',             # 0D
        'ED6_DT27/CH03265 ._CH',             # 0E
        'ED6_DT27/CH03230 ._CH',             # 0F
        'ED6_DT27/CH03231 ._CH',             # 10
        'ED6_DT27/CH03233 ._CH',             # 11
        'ED6_DT27/CH03244 ._CH',             # 12
        'ED6_DT27/CH03235 ._CH',             # 13
        'ED6_DT27/CH03270 ._CH',             # 14
        'ED6_DT27/CH03271 ._CH',             # 15
        'ED6_DT27/CH03273 ._CH',             # 16
        'ED6_DT27/CH03273 ._CH',             # 17
        'ED6_DT27/CH03273 ._CH',             # 18
        'ED6_DT27/CH03150 ._CH',             # 19
        'ED6_DT27/CH03151 ._CH',             # 1A
        'ED6_DT27/CH03153 ._CH',             # 1B
        'ED6_DT27/CH03154 ._CH',             # 1C
        'ED6_DT27/CH03155 ._CH',             # 1D
    )

    AddCharChipPat(
        'ED6_DT27/CH03250P._CP',             # 00
        'ED6_DT27/CH03251P._CP',             # 01
        'ED6_DT27/CH03253P._CP',             # 02
        'ED6_DT27/CH03254P._CP',             # 03
        'ED6_DT27/CH03255P._CP',             # 04
        'ED6_DT27/CH03240P._CP',             # 05
        'ED6_DT27/CH03241P._CP',             # 06
        'ED6_DT27/CH03243P._CP',             # 07
        'ED6_DT27/CH03244P._CP',             # 08
        'ED6_DT27/CH03245P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT27/CH03261P._CP',             # 0B
        'ED6_DT27/CH03263P._CP',             # 0C
        'ED6_DT27/CH03264P._CP',             # 0D
        'ED6_DT27/CH03265P._CP',             # 0E
        'ED6_DT27/CH03230P._CP',             # 0F
        'ED6_DT27/CH03231P._CP',             # 10
        'ED6_DT27/CH03233P._CP',             # 11
        'ED6_DT27/CH03244P._CP',             # 12
        'ED6_DT27/CH03235P._CP',             # 13
        'ED6_DT27/CH03270P._CP',             # 14
        'ED6_DT27/CH03271P._CP',             # 15
        'ED6_DT27/CH03273P._CP',             # 16
        'ED6_DT27/CH03273P._CP',             # 17
        'ED6_DT27/CH03273P._CP',             # 18
        'ED6_DT27/CH03150P._CP',             # 19
        'ED6_DT27/CH03151P._CP',             # 1A
        'ED6_DT27/CH03153P._CP',             # 1B
        'ED6_DT27/CH03154P._CP',             # 1C
        'ED6_DT27/CH03155P._CP',             # 1D
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_4FA",          # 00, 0
        "Function_1_4FB",          # 01, 1
        "Function_2_4FC",          # 02, 2
        "Function_3_51F",          # 03, 3
        "Function_4_5C6",          # 04, 4
        "Function_5_5C7",          # 05, 5
        "Function_6_5E0",          # 06, 6
        "Function_7_5F9",          # 07, 7
        "Function_8_612",          # 08, 8
        "Function_9_62B",          # 09, 9
        "Function_10_644",         # 0A, 10
    )


    def Function_0_4FA(): pass

    label("Function_0_4FA")

    Return()

    # Function_0_4FA end

    def Function_1_4FB(): pass

    label("Function_1_4FB")

    Return()

    # Function_1_4FB end

    def Function_2_4FC(): pass

    label("Function_2_4FC")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "你好。\x02",
    )

    Jump("loc_515")

    label("loc_515")

    CloseMessageWindow()
    OP_AE(0x5DC)
    TalkEnd(0xFE)
    Return()

    # Function_2_4FC end

    def Function_3_51F(): pass

    label("Function_3_51F")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_550"),
        (1, "loc_55C"),
        (2, "loc_568"),
        (3, "loc_574"),
        (4, "loc_580"),
        (5, "loc_58C"),
        (6, "loc_598"),
        (SWITCH_DEFAULT, "loc_5A4"),
    )


    label("loc_550")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5B0")

    label("loc_55C")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5B0")

    label("loc_568")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5B0")

    label("loc_574")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5B0")

    label("loc_580")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B0")

    label("loc_58C")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5B0")

    label("loc_598")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B0")

    label("loc_5A4")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B0")

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B0")

    label("loc_5C5")

    Return()

    # Function_3_51F end

    def Function_4_5C6(): pass

    label("Function_4_5C6")

    Return()

    # Function_4_5C6 end

    def Function_5_5C7(): pass

    label("Function_5_5C7")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "#1500F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_5C7 end

    def Function_6_5E0(): pass

    label("Function_6_5E0")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "#1520F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_5E0 end

    def Function_7_5F9(): pass

    label("Function_7_5F9")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "#1540F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_5F9 end

    def Function_8_612(): pass

    label("Function_8_612")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "#1640F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_612 end

    def Function_9_62B(): pass

    label("Function_9_62B")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#1560F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_62B end

    def Function_10_644(): pass

    label("Function_10_644")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "#1440F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_644 end

    SaveToFile()

Try(main)
