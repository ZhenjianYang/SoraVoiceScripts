from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0042   ._SN',
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
        '03940ルフィナ',                        # 9
        '03950オズボーン',                      # 10
        '03960クローディア',                    # 11
        '03980ティータ母',                      # 12
        '03970ティータ父',                      # 13
        '03990ドレスユリア',                    # 14
        '03420ボディカード',                    # 15
        '03430黒の猟兵(武器もち)',              # 16
        '03440黒騎士レーヴェ',                  # 17
        '02650主催者',                          # 18
        '02670先輩１レクター',                  # 19
        '02680先輩２レオ',                      # 20
        '02690先輩３ルーシー',                  # 21
        '02700先輩４リゲル',                    # 22
        '02710アイナ１８歳',                    # 23
        '02720ドロシー１５歳',                  # 24
        '02730エリッサ１１歳',                  # 25
        '02740ティオ１１際',                    # 26
        '02750ヨシュア１１歳',                  # 27
        '02560アイナ',                          # 28
        '02070ドロシー',                        # 29
        '03460ボディカード',                    # 30
        '02660来賓エキストラ①',                # 31
        '02840来賓エキストラ②',                # 32
        '02850来賓エキストラ③',                # 33
        '02860来賓エキストラ④',                # 34
        '02870来賓エキストラ⑤',                # 35
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
        'ED6_DT27/CH03940 ._CH',             # 00
        'ED6_DT27/CH03950 ._CH',             # 01
        'ED6_DT27/CH03960 ._CH',             # 02
        'ED6_DT27/CH03970 ._CH',             # 03
        'ED6_DT27/CH03980 ._CH',             # 04
        'ED6_DT27/CH03990 ._CH',             # 05
        'ED6_DT27/CH03420 ._CH',             # 06
        'ED6_DT27/CH03430 ._CH',             # 07
        'ED6_DT27/CH03440 ._CH',             # 08
        'ED6_DT07/CH02650 ._CH',             # 09
        'ED6_DT07/CH02660 ._CH',             # 0A
        'ED6_DT07/CH02670 ._CH',             # 0B
        'ED6_DT07/CH02680 ._CH',             # 0C
        'ED6_DT07/CH02690 ._CH',             # 0D
        'ED6_DT07/CH02700 ._CH',             # 0E
        'ED6_DT07/CH02710 ._CH',             # 0F
        'ED6_DT07/CH02720 ._CH',             # 10
        'ED6_DT07/CH02730 ._CH',             # 11
        'ED6_DT07/CH02740 ._CH',             # 12
        'ED6_DT07/CH02750 ._CH',             # 13
        'ED6_DT07/CH02560 ._CH',             # 14
        'ED6_DT07/CH02070 ._CH',             # 15
        'ED6_DT27/CH03460 ._CH',             # 16
        'ED6_DT07/CH02840 ._CH',             # 17
        'ED6_DT07/CH02850 ._CH',             # 18
        'ED6_DT07/CH02860 ._CH',             # 19
        'ED6_DT07/CH02870 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT27/CH03940P._CP',             # 00
        'ED6_DT27/CH03950P._CP',             # 01
        'ED6_DT27/CH03960P._CP',             # 02
        'ED6_DT27/CH03970P._CP',             # 03
        'ED6_DT27/CH03980P._CP',             # 04
        'ED6_DT27/CH03990P._CP',             # 05
        'ED6_DT27/CH03420P._CP',             # 06
        'ED6_DT27/CH03430P._CP',             # 07
        'ED6_DT27/CH03440P._CP',             # 08
        'ED6_DT07/CH02650P._CP',             # 09
        'ED6_DT07/CH02660P._CP',             # 0A
        'ED6_DT07/CH02670P._CP',             # 0B
        'ED6_DT07/CH02680P._CP',             # 0C
        'ED6_DT07/CH02690P._CP',             # 0D
        'ED6_DT07/CH02700P._CP',             # 0E
        'ED6_DT07/CH02710P._CP',             # 0F
        'ED6_DT07/CH02720P._CP',             # 10
        'ED6_DT07/CH02730P._CP',             # 11
        'ED6_DT07/CH02740P._CP',             # 12
        'ED6_DT07/CH02750P._CP',             # 13
        'ED6_DT07/CH02560P._CP',             # 14
        'ED6_DT07/CH02070P._CP',             # 15
        'ED6_DT27/CH03460P._CP',             # 16
        'ED6_DT07/CH02840P._CP',             # 17
        'ED6_DT07/CH02850P._CP',             # 18
        'ED6_DT07/CH02860P._CP',             # 19
        'ED6_DT07/CH02870P._CP',             # 1A
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
        Y                   = 24000,
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

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )


    ScpFunction(
        "Function_0_4E2",          # 00, 0
        "Function_1_4E3",          # 01, 1
        "Function_2_4E4",          # 02, 2
        "Function_3_4FE",          # 03, 3
        "Function_4_5A5",          # 04, 4
        "Function_5_5BC",          # 05, 5
        "Function_6_5D3",          # 06, 6
        "Function_7_5EA",          # 07, 7
        "Function_8_601",          # 08, 8
        "Function_9_618",          # 09, 9
        "Function_10_62F",         # 0A, 10
        "Function_11_640",         # 0B, 11
        "Function_12_651",         # 0C, 12
        "Function_13_668",         # 0D, 13
        "Function_14_679",         # 0E, 14
        "Function_15_68A",         # 0F, 15
        "Function_16_6A1",         # 10, 16
        "Function_17_6B8",         # 11, 17
        "Function_18_6CF",         # 12, 18
        "Function_19_6E0",         # 13, 19
        "Function_20_6F7",         # 14, 20
        "Function_21_70E",         # 15, 21
        "Function_22_725",         # 16, 22
        "Function_23_73C",         # 17, 23
        "Function_24_753",         # 18, 24
        "Function_25_769",         # 19, 25
        "Function_26_77F",         # 1A, 26
        "Function_27_790",         # 1B, 27
        "Function_28_7A1",         # 1C, 28
        "Function_29_7B2",         # 1D, 29
    )


    def Function_0_4E2(): pass

    label("Function_0_4E2")

    Return()

    # Function_0_4E2 end

    def Function_1_4E3(): pass

    label("Function_1_4E3")

    Return()

    # Function_1_4E3 end

    def Function_2_4E4(): pass

    label("Function_2_4E4")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "はにゃ。\x02",
    )

    CloseMessageWindow()
    OP_AE(0x5DC)
    TalkEnd(0xFE)
    Return()

    # Function_2_4E4 end

    def Function_3_4FE(): pass

    label("Function_3_4FE")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_52F"),
        (1, "loc_53B"),
        (2, "loc_547"),
        (3, "loc_553"),
        (4, "loc_55F"),
        (5, "loc_56B"),
        (6, "loc_577"),
        (SWITCH_DEFAULT, "loc_583"),
    )


    label("loc_52F")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_58F")

    label("loc_53B")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_58F")

    label("loc_547")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_58F")

    label("loc_553")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_58F")

    label("loc_55F")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_58F")

    label("loc_56B")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_58F")

    label("loc_577")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58F")

    label("loc_583")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58F")

    label("loc_58F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58F")

    label("loc_5A4")

    Return()

    # Function_3_4FE end

    def Function_4_5A5(): pass

    label("Function_4_5A5")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "#1470F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_5A5 end

    def Function_5_5BC(): pass

    label("Function_5_5BC")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "#1480F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_5BC end

    def Function_6_5D3(): pass

    label("Function_6_5D3")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "#1810F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_5D3 end

    def Function_7_5EA(): pass

    label("Function_7_5EA")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "#1450F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_5EA end

    def Function_8_601(): pass

    label("Function_8_601")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#1460F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_601 end

    def Function_9_618(): pass

    label("Function_9_618")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "#1490F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_618 end

    def Function_10_62F(): pass

    label("Function_10_62F")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_62F end

    def Function_11_640(): pass

    label("Function_11_640")

    TalkBegin(0xFE)

    ChrTalk(    #8
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_640 end

    def Function_12_651(): pass

    label("Function_12_651")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        "#1590F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_651 end

    def Function_13_668(): pass

    label("Function_13_668")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_668 end

    def Function_14_679(): pass

    label("Function_14_679")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_679 end

    def Function_15_68A(): pass

    label("Function_15_68A")

    TalkBegin(0xFE)

    ChrTalk(    #12
        0xFE,
        "#1770F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_68A end

    def Function_16_6A1(): pass

    label("Function_16_6A1")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        "#1780F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_6A1 end

    def Function_17_6B8(): pass

    label("Function_17_6B8")

    TalkBegin(0xFE)

    ChrTalk(    #14
        0xFE,
        "#1790F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_6B8 end

    def Function_18_6CF(): pass

    label("Function_18_6CF")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_6CF end

    def Function_19_6E0(): pass

    label("Function_19_6E0")

    TalkBegin(0xFE)

    ChrTalk(    #16
        0xFE,
        "#1650F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_6E0 end

    def Function_20_6F7(): pass

    label("Function_20_6F7")

    TalkBegin(0xFE)

    ChrTalk(    #17
        0xFE,
        "#1660F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_6F7 end

    def Function_21_70E(): pass

    label("Function_21_70E")

    TalkBegin(0xFE)

    ChrTalk(    #18
        0xFE,
        "#1690F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_70E end

    def Function_22_725(): pass

    label("Function_22_725")

    TalkBegin(0xFE)

    ChrTalk(    #19
        0xFE,
        "#1680F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_725 end

    def Function_23_73C(): pass

    label("Function_23_73C")

    TalkBegin(0xFE)

    ChrTalk(    #20
        0xFE,
        "#1670F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_73C end

    def Function_24_753(): pass

    label("Function_24_753")

    TalkBegin(0xFE)

    ChrTalk(    #21
        0xFE,
        "#410F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_753 end

    def Function_25_769(): pass

    label("Function_25_769")

    TalkBegin(0xFE)

    ChrTalk(    #22
        0xFE,
        "#150F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_769 end

    def Function_26_77F(): pass

    label("Function_26_77F")

    TalkBegin(0xFE)

    ChrTalk(    #23
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_77F end

    def Function_27_790(): pass

    label("Function_27_790")

    TalkBegin(0xFE)

    ChrTalk(    #24
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_790 end

    def Function_28_7A1(): pass

    label("Function_28_7A1")

    TalkBegin(0xFE)

    ChrTalk(    #25
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_7A1 end

    def Function_29_7B2(): pass

    label("Function_29_7B2")

    TalkBegin(0xFE)

    ChrTalk(    #26
        0xFE,
        "通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_7B2 end

    SaveToFile()

Try(main)
