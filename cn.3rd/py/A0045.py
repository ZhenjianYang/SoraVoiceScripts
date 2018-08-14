from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0045   ._SN',
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
        '02760赛雷斯托·Ｄ·奥赛雷丝',          # 9
        '02770蒙面之王',                        # 10
        '02780僧兵',                            # 11
        '02790扮装凯文',                        # 12
        '02800随从骑士凯文',                    # 13
        '02810莉丝１４岁',                      # 14
        '02820黑猎兵(无兵器)',                  # 15
        '02830卡玲',                            # 16
        '02840',                                # 17
        '02850',                                # 18
        '02630玛丽',                            # 19
        '02640达尼艾尔',                        # 20
        '02500波利',                            # 21
        '02510迪恩',                            # 22
        '02520雷斯',                            # 23
        '02530洛克',                            # 24
        '02900安敦（男学生）',                  # 25
        '02910利库（男学生）',                  # 26
        '02920蒙面之王\u3000浮游',              # 27
        '02930蒙面之王（露菲娜）步行',          # 28
        '02940蒙面之王（露菲娜）浮游',          # 29
        '',                                     # 30
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02760 ._CH',             # 00
        'ED6_DT07/CH02770 ._CH',             # 01
        'ED6_DT07/CH02780 ._CH',             # 02
        'ED6_DT07/CH02790 ._CH',             # 03
        'ED6_DT07/CH02800 ._CH',             # 04
        'ED6_DT07/CH02810 ._CH',             # 05
        'ED6_DT07/CH02820 ._CH',             # 06
        'ED6_DT07/CH02830 ._CH',             # 07
        'ED6_DT07/CH02840 ._CH',             # 08
        'ED6_DT07/CH02850 ._CH',             # 09
        'ED6_DT07/CH02630 ._CH',             # 0A
        'ED6_DT07/CH02640 ._CH',             # 0B
        'ED6_DT07/CH02500 ._CH',             # 0C
        'ED6_DT07/CH02510 ._CH',             # 0D
        'ED6_DT07/CH02520 ._CH',             # 0E
        'ED6_DT07/CH02530 ._CH',             # 0F
        'ED6_DT07/CH02900 ._CH',             # 10
        'ED6_DT07/CH02910 ._CH',             # 11
        'ED6_DT07/CH02920 ._CH',             # 12
        'ED6_DT07/CH02930 ._CH',             # 13
        'ED6_DT07/CH02940 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02760P._CP',             # 00
        'ED6_DT07/CH02770P._CP',             # 01
        'ED6_DT07/CH02780P._CP',             # 02
        'ED6_DT07/CH02790P._CP',             # 03
        'ED6_DT07/CH02800P._CP',             # 04
        'ED6_DT07/CH02810P._CP',             # 05
        'ED6_DT07/CH02820P._CP',             # 06
        'ED6_DT07/CH02830P._CP',             # 07
        'ED6_DT07/CH02840P._CP',             # 08
        'ED6_DT07/CH02850P._CP',             # 09
        'ED6_DT07/CH02630P._CP',             # 0A
        'ED6_DT07/CH02640P._CP',             # 0B
        'ED6_DT07/CH02500P._CP',             # 0C
        'ED6_DT07/CH02510P._CP',             # 0D
        'ED6_DT07/CH02520P._CP',             # 0E
        'ED6_DT07/CH02530P._CP',             # 0F
        'ED6_DT07/CH02900P._CP',             # 10
        'ED6_DT07/CH02910P._CP',             # 11
        'ED6_DT07/CH02920P._CP',             # 12
        'ED6_DT07/CH02930P._CP',             # 13
        'ED6_DT07/CH02940P._CP',             # 14
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 32000,
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

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 8000,
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
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8000,
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
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
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
        TalkScenaIndex      = 24,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_3F4",          # 02, 2
        "Function_3_417",          # 03, 3
        "Function_4_4BE",          # 04, 4
        "Function_5_4D7",          # 05, 5
        "Function_6_4F0",          # 06, 6
        "Function_7_509",          # 07, 7
        "Function_8_522",          # 08, 8
        "Function_9_53B",          # 09, 9
        "Function_10_554",         # 0A, 10
        "Function_11_56D",         # 0B, 11
        "Function_12_586",         # 0C, 12
        "Function_13_59F",         # 0D, 13
        "Function_14_5B8",         # 0E, 14
        "Function_15_5D1",         # 0F, 15
        "Function_16_5EA",         # 10, 16
        "Function_17_603",         # 11, 17
        "Function_18_61C",         # 12, 18
        "Function_19_635",         # 13, 19
        "Function_20_64E",         # 14, 20
        "Function_21_667",         # 15, 21
        "Function_22_680",         # 16, 22
        "Function_23_699",         # 17, 23
        "Function_24_6B2",         # 18, 24
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    Return()

    # Function_0_3F2 end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Return()

    # Function_1_3F3 end

    def Function_2_3F4(): pass

    label("Function_2_3F4")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "你好。\x02",
    )

    Jump("loc_40D")

    label("loc_40D")

    CloseMessageWindow()
    OP_AE(0x5DC)
    TalkEnd(0xFE)
    Return()

    # Function_2_3F4 end

    def Function_3_417(): pass

    label("Function_3_417")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_448"),
        (1, "loc_454"),
        (2, "loc_460"),
        (3, "loc_46C"),
        (4, "loc_478"),
        (5, "loc_484"),
        (6, "loc_490"),
        (SWITCH_DEFAULT, "loc_49C"),
    )


    label("loc_448")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_4A8")

    label("loc_454")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_4A8")

    label("loc_460")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_4A8")

    label("loc_46C")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_4A8")

    label("loc_478")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4A8")

    label("loc_484")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_4A8")

    label("loc_490")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A8")

    label("loc_49C")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A8")

    label("loc_4A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A8")

    label("loc_4BD")

    Return()

    # Function_3_417 end

    def Function_4_4BE(): pass

    label("Function_4_4BE")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "#1610F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_4BE end

    def Function_5_4D7(): pass

    label("Function_5_4D7")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "#1580F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_4D7 end

    def Function_6_4F0(): pass

    label("Function_6_4F0")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "普通\x02",
    )

    Jump("loc_504")

    label("loc_504")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_4F0 end

    def Function_7_509(): pass

    label("Function_7_509")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "#1600F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_509 end

    def Function_8_522(): pass

    label("Function_8_522")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#1620F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_522 end

    def Function_9_53B(): pass

    label("Function_9_53B")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "#1630F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_53B end

    def Function_10_554(): pass

    label("Function_10_554")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "普通\x02",
    )

    Jump("loc_568")

    label("loc_568")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_554 end

    def Function_11_56D(): pass

    label("Function_11_56D")

    TalkBegin(0xFE)

    ChrTalk(    #8
        0xFE,
        "#1700F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_56D end

    def Function_12_586(): pass

    label("Function_12_586")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        "普通\x02",
    )

    Jump("loc_59A")

    label("loc_59A")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_586 end

    def Function_13_59F(): pass

    label("Function_13_59F")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0xFE,
        "普通\x02",
    )

    Jump("loc_5B3")

    label("loc_5B3")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_59F end

    def Function_14_5B8(): pass

    label("Function_14_5B8")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0xFE,
        "#1710F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_5B8 end

    def Function_15_5D1(): pass

    label("Function_15_5D1")

    TalkBegin(0xFE)

    ChrTalk(    #12
        0xFE,
        "#1720F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_5D1 end

    def Function_16_5EA(): pass

    label("Function_16_5EA")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        "#1730F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_5EA end

    def Function_17_603(): pass

    label("Function_17_603")

    TalkBegin(0xFE)

    ChrTalk(    #14
        0xFE,
        "#1740F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_603 end

    def Function_18_61C(): pass

    label("Function_18_61C")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        "#1750F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_61C end

    def Function_19_635(): pass

    label("Function_19_635")

    TalkBegin(0xFE)

    ChrTalk(    #16
        0xFE,
        "#1760F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_635 end

    def Function_20_64E(): pass

    label("Function_20_64E")

    TalkBegin(0xFE)

    ChrTalk(    #17
        0xFE,
        "普通\x02",
    )

    Jump("loc_662")

    label("loc_662")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_64E end

    def Function_21_667(): pass

    label("Function_21_667")

    TalkBegin(0xFE)

    ChrTalk(    #18
        0xFE,
        "普通\x02",
    )

    Jump("loc_67B")

    label("loc_67B")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_667 end

    def Function_22_680(): pass

    label("Function_22_680")

    TalkBegin(0xFE)

    ChrTalk(    #19
        0xFE,
        "普通\x02",
    )

    Jump("loc_694")

    label("loc_694")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_680 end

    def Function_23_699(): pass

    label("Function_23_699")

    TalkBegin(0xFE)

    ChrTalk(    #20
        0xFE,
        "普通\x02",
    )

    Jump("loc_6AD")

    label("loc_6AD")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_699 end

    def Function_24_6B2(): pass

    label("Function_24_6B2")

    TalkBegin(0xFE)

    ChrTalk(    #21
        0xFE,
        "普通\x02",
    )

    Jump("loc_6C6")

    label("loc_6C6")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_6B2 end

    SaveToFile()

Try(main)
