from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0039   ._SN',
        MapName             = 'map1',
        Location            = 'T0002.x',
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
        'CH03003エステル',                      # 9
        'CH03013ヨシュア',                      # 10
        'CH03023シェラ',                        # 11
        'CH03033オリビエ',                      # 12
        'CH03043クローゼ',                      # 13
        'CH03053アガット',                      # 14
        'CH03063ティータ',                      # 15
        'CH03073ジン',                          # 16
        'CH03083ケビン',                        # 17
        'CH03093アネラス',                      # 18
        'CH03103ジョゼット',                    # 19
        'CH03123カノーネ(特務兵版)',            # 20
        'CH03213クローゼ(礼服)',                # 21
        'CH03503痩せ狼ヴァルター',              # 22
        'CH03523幻惑のルシオラ',                # 23
        'CH03543剣帝レオンハルト',              # 24
        'CH03553研究服ワイスマン',              # 25
        'CH03573ミュラー',                      # 26
        'CH03583ユリア大尉',                    # 27
        'CH03593シード中佐',                    # 28
        'CH03673軍服カシウス      ',            # 29
        'CH03683軍服オリビエ      ',            # 30
        'CH03703ゼクス中将        ',            # 31
        'CH03713ダヴィル帝国大使  ',            # 32
        'CH03723ルイーゼ共和国大使',            # 33
        'CH03743母親レナ・ブライト',            # 34
        'CH03763ドルン\u3000\u3000\u3000\u3000\u3000\u3000',# 35
        'CH03773キール\u3000\u3000\u3000\u3000\u3000\u3000',# 36
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
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT27/CH03013 ._CH',             # 01
        'ED6_DT27/CH03023 ._CH',             # 02
        'ED6_DT27/CH03033 ._CH',             # 03
        'ED6_DT27/CH03043 ._CH',             # 04
        'ED6_DT27/CH03053 ._CH',             # 05
        'ED6_DT27/CH03063 ._CH',             # 06
        'ED6_DT27/CH03073 ._CH',             # 07
        'ED6_DT27/CH03083 ._CH',             # 08
        'ED6_DT27/CH03093 ._CH',             # 09
        'ED6_DT27/CH03103 ._CH',             # 0A
        'ED6_DT27/CH03003 ._CH',             # 0B
        'ED6_DT27/CH03123 ._CH',             # 0C
        'ED6_DT27/CH03003 ._CH',             # 0D
        'ED6_DT27/CH03003 ._CH',             # 0E
        'ED6_DT27/CH03213 ._CH',             # 0F
        'ED6_DT27/CH03003 ._CH',             # 10
        'ED6_DT27/CH03003 ._CH',             # 11
        'ED6_DT27/CH03003 ._CH',             # 12
        'ED6_DT27/CH03003 ._CH',             # 13
        'ED6_DT27/CH03503 ._CH',             # 14
        'ED6_DT27/CH03003 ._CH',             # 15
        'ED6_DT27/CH03523 ._CH',             # 16
        'ED6_DT27/CH03003 ._CH',             # 17
        'ED6_DT27/CH03543 ._CH',             # 18
        'ED6_DT27/CH03553 ._CH',             # 19
        'ED6_DT27/CH03003 ._CH',             # 1A
        'ED6_DT27/CH03573 ._CH',             # 1B
        'ED6_DT27/CH03583 ._CH',             # 1C
        'ED6_DT27/CH03593 ._CH',             # 1D
        'ED6_DT27/CH03003 ._CH',             # 1E
        'ED6_DT27/CH03003 ._CH',             # 1F
        'ED6_DT27/CH03003 ._CH',             # 20
        'ED6_DT27/CH03003 ._CH',             # 21
        'ED6_DT27/CH03003 ._CH',             # 22
        'ED6_DT27/CH03003 ._CH',             # 23
        'ED6_DT27/CH03003 ._CH',             # 24
        'ED6_DT27/CH03673 ._CH',             # 25
        'ED6_DT27/CH03683 ._CH',             # 26
        'ED6_DT27/CH03003 ._CH',             # 27
        'ED6_DT27/CH03703 ._CH',             # 28
        'ED6_DT27/CH03713 ._CH',             # 29
        'ED6_DT27/CH03723 ._CH',             # 2A
        'ED6_DT27/CH03003 ._CH',             # 2B
        'ED6_DT27/CH03743 ._CH',             # 2C
        'ED6_DT27/CH03003 ._CH',             # 2D
        'ED6_DT27/CH03763 ._CH',             # 2E
        'ED6_DT27/CH03773 ._CH',             # 2F
        'ED6_DT27/CH03003 ._CH',             # 30
        'ED6_DT27/CH03003 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT27/CH03013P._CP',             # 01
        'ED6_DT27/CH03023P._CP',             # 02
        'ED6_DT27/CH03033P._CP',             # 03
        'ED6_DT27/CH03043P._CP',             # 04
        'ED6_DT27/CH03053P._CP',             # 05
        'ED6_DT27/CH03063P._CP',             # 06
        'ED6_DT27/CH03073P._CP',             # 07
        'ED6_DT27/CH03083P._CP',             # 08
        'ED6_DT27/CH03093P._CP',             # 09
        'ED6_DT27/CH03103P._CP',             # 0A
        'ED6_DT27/CH03003P._CP',             # 0B
        'ED6_DT27/CH03123P._CP',             # 0C
        'ED6_DT27/CH03003P._CP',             # 0D
        'ED6_DT27/CH03003P._CP',             # 0E
        'ED6_DT27/CH03213P._CP',             # 0F
        'ED6_DT27/CH03003P._CP',             # 10
        'ED6_DT27/CH03003P._CP',             # 11
        'ED6_DT27/CH03003P._CP',             # 12
        'ED6_DT27/CH03003P._CP',             # 13
        'ED6_DT27/CH03503P._CP',             # 14
        'ED6_DT27/CH03003P._CP',             # 15
        'ED6_DT27/CH03523P._CP',             # 16
        'ED6_DT27/CH03003P._CP',             # 17
        'ED6_DT27/CH03543P._CP',             # 18
        'ED6_DT27/CH03553P._CP',             # 19
        'ED6_DT27/CH03003P._CP',             # 1A
        'ED6_DT27/CH03573P._CP',             # 1B
        'ED6_DT27/CH03583P._CP',             # 1C
        'ED6_DT27/CH03593P._CP',             # 1D
        'ED6_DT27/CH03003P._CP',             # 1E
        'ED6_DT27/CH03003P._CP',             # 1F
        'ED6_DT27/CH03003P._CP',             # 20
        'ED6_DT27/CH03003P._CP',             # 21
        'ED6_DT27/CH03003P._CP',             # 22
        'ED6_DT27/CH03003P._CP',             # 23
        'ED6_DT27/CH03003P._CP',             # 24
        'ED6_DT27/CH03673P._CP',             # 25
        'ED6_DT27/CH03683P._CP',             # 26
        'ED6_DT27/CH03003P._CP',             # 27
        'ED6_DT27/CH03703P._CP',             # 28
        'ED6_DT27/CH03713P._CP',             # 29
        'ED6_DT27/CH03723P._CP',             # 2A
        'ED6_DT27/CH03003P._CP',             # 2B
        'ED6_DT27/CH03743P._CP',             # 2C
        'ED6_DT27/CH03003P._CP',             # 2D
        'ED6_DT27/CH03763P._CP',             # 2E
        'ED6_DT27/CH03773P._CP',             # 2F
        'ED6_DT27/CH03003P._CP',             # 30
        'ED6_DT27/CH03003P._CP',             # 31
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_5BA",          # 00, 0
        "Function_1_5C6",          # 01, 1
        "Function_2_5C7",          # 02, 2
        "Function_3_5DD",          # 03, 3
    )


    def Function_0_5BA(): pass

    label("Function_0_5BA")

    OP_51(0xE, 0x31, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_5BA end

    def Function_1_5C6(): pass

    label("Function_1_5C6")

    Return()

    # Function_1_5C6 end

    def Function_2_5C7(): pass

    label("Function_2_5C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DC")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Jump("Function_2_5C7")

    label("loc_5DC")

    Return()

    # Function_2_5C7 end

    def Function_3_5DD(): pass

    label("Function_3_5DD")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "はにゃ。\x02",
    )

    CloseMessageWindow()
    OP_AE(0x5DC)
    TalkEnd(0xFE)
    Return()

    # Function_3_5DD end

    SaveToFile()

Try(main)
