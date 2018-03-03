from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0020   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 55,
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
        '03000 エステル',                       # 9
        '03010 ヨシュア',                       # 10
        '03020 シェラ',                         # 11
        '03030 オリビエ',                       # 12
        '03040 クローゼ',                       # 13
        '03050 アガット',                       # 14
        '03060 ティータ',                       # 15
        '03070 ジン',                           # 16
        '03080 ケビン',                         # 17
        '03090 アネラス',                       # 18
        '03100 ジョゼット',                     # 19
        '03110 リシャール',                     # 20
        '03120 カノーネ',                       # 21
        '03130 クルツ',                         # 22
        '03150 リース',                         # 23
        '03180 グラッツ',                       # 24
        '03190 カルナ',                         # 25
        '03200 紋章なしヨシュア',               # 26
        '03210 礼服クローゼ',                   # 27
        '03500 痩せ狼ヴァルター',               # 28
        '03510 殲滅天使レン',                   # 29
        '03520 幻惑のルシオラ',                 # 30
        '03530 ブルブラン伯爵',                 # 31
        '03540 剣帝レオンハルト',               # 32
        '03550 研究服ワイスマン',               # 33
        '03560 ロボヨシュア',                   # 34
        '03570 ミュラー',                       # 35
        '03580 ユリア大尉',                     # 36
        '03590 シード中佐',                     # 37
        '03600 道化師カンパネルラ',             # 38
        '03610 強化猟兵A ',                     # 39
        '03620 強化猟兵B ',                     # 40
        '03630 猟兵クルツ',                     # 41
        '03640 猟兵カルナ',                     # 42
        '03650 強化猟兵ヨシュア',               # 43
        '03670 軍服カシウス',                   # 44
        '03680 軍服オリビエ',                   # 45
        '03690 投獄版リシャール',               # 46
        '03940 ルフィナ\u3000\u3000',           # 47
        '03950 オズボーン\u3000',               # 48
        '03960 クローディア',                   # 49
        '03970 ティータ父\u3000',               # 50
        '03980 ティータ母\u3000',               # 51
        '03990 ドレスユリア',                   # 52
        'CH00000前編エステル',                  # 53
        'CH00010前編ヨシュア',                  # 54
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
        'ED6_DT07/CH00000 ._CH',             # 00
        'ED6_DT07/CH00010 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT27/CH03080 ._CH',             # 08
        'ED6_DT27/CH03090 ._CH',             # 09
        'ED6_DT27/CH03100 ._CH',             # 0A
        'ED6_DT07/CH02030 ._CH',             # 0B
        'ED6_DT07/CH02030 ._CH',             # 0C
        'ED6_DT27/CH03130 ._CH',             # 0D
        'ED6_DT27/CH03150 ._CH',             # 0E
        'ED6_DT07/CH00000 ._CH',             # 0F
        'ED6_DT07/CH00010 ._CH',             # 10
        'ED6_DT27/CH03200 ._CH',             # 11
        'ED6_DT27/CH03210 ._CH',             # 12
        'ED6_DT07/CH01260 ._CH',             # 13
        'ED6_DT07/CH01240 ._CH',             # 14
        'ED6_DT27/CH03500 ._CH',             # 15
        'ED6_DT27/CH03510 ._CH',             # 16
        'ED6_DT27/CH03520 ._CH',             # 17
        'ED6_DT27/CH03530 ._CH',             # 18
        'ED6_DT27/CH03540 ._CH',             # 19
        'ED6_DT27/CH03550 ._CH',             # 1A
        'ED6_DT27/CH03560 ._CH',             # 1B
        'ED6_DT27/CH03570 ._CH',             # 1C
        'ED6_DT27/CH03580 ._CH',             # 1D
        'ED6_DT27/CH03590 ._CH',             # 1E
        'ED6_DT27/CH03600 ._CH',             # 1F
        'ED6_DT27/CH03610 ._CH',             # 20
        'ED6_DT27/CH03620 ._CH',             # 21
        'ED6_DT27/CH03630 ._CH',             # 22
        'ED6_DT27/CH03640 ._CH',             # 23
        'ED6_DT27/CH03650 ._CH',             # 24
        'ED6_DT27/CH03670 ._CH',             # 25
        'ED6_DT27/CH03680 ._CH',             # 26
        'ED6_DT27/CH03690 ._CH',             # 27
        'ED6_DT27/CH03940 ._CH',             # 28
        'ED6_DT27/CH03950 ._CH',             # 29
        'ED6_DT27/CH03960 ._CH',             # 2A
        'ED6_DT27/CH03970 ._CH',             # 2B
        'ED6_DT27/CH03980 ._CH',             # 2C
        'ED6_DT27/CH03990 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH00000P._CP',             # 00
        'ED6_DT07/CH00010P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT27/CH03080P._CP',             # 08
        'ED6_DT27/CH03090P._CP',             # 09
        'ED6_DT27/CH03100P._CP',             # 0A
        'ED6_DT07/CH02030P._CP',             # 0B
        'ED6_DT07/CH02030P._CP',             # 0C
        'ED6_DT27/CH03130P._CP',             # 0D
        'ED6_DT27/CH03150P._CP',             # 0E
        'ED6_DT07/CH00000P._CP',             # 0F
        'ED6_DT07/CH00010P._CP',             # 10
        'ED6_DT27/CH03200P._CP',             # 11
        'ED6_DT27/CH03210P._CP',             # 12
        'ED6_DT07/CH01260P._CP',             # 13
        'ED6_DT07/CH01240P._CP',             # 14
        'ED6_DT27/CH03500P._CP',             # 15
        'ED6_DT27/CH03510P._CP',             # 16
        'ED6_DT27/CH03520P._CP',             # 17
        'ED6_DT27/CH03530P._CP',             # 18
        'ED6_DT27/CH03540P._CP',             # 19
        'ED6_DT27/CH03550P._CP',             # 1A
        'ED6_DT27/CH03560P._CP',             # 1B
        'ED6_DT27/CH03570P._CP',             # 1C
        'ED6_DT27/CH03580P._CP',             # 1D
        'ED6_DT27/CH03590P._CP',             # 1E
        'ED6_DT27/CH03600P._CP',             # 1F
        'ED6_DT27/CH03610P._CP',             # 20
        'ED6_DT27/CH03620P._CP',             # 21
        'ED6_DT27/CH03630P._CP',             # 22
        'ED6_DT27/CH03640P._CP',             # 23
        'ED6_DT27/CH03650P._CP',             # 24
        'ED6_DT27/CH03670P._CP',             # 25
        'ED6_DT27/CH03680P._CP',             # 26
        'ED6_DT27/CH03690P._CP',             # 27
        'ED6_DT27/CH03940P._CP',             # 28
        'ED6_DT27/CH03950P._CP',             # 29
        'ED6_DT27/CH03960P._CP',             # 2A
        'ED6_DT27/CH03970P._CP',             # 2B
        'ED6_DT27/CH03980P._CP',             # 2C
        'ED6_DT27/CH03990P._CP',             # 2D
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )


    ScpFunction(
        "Function_0_7DA",          # 00, 0
        "Function_1_7E0",          # 01, 1
        "Function_2_7E1",          # 02, 2
        "Function_3_7F4",          # 03, 3
        "Function_4_A47",          # 04, 4
        "Function_5_BC0",          # 05, 5
        "Function_6_C25",          # 06, 6
        "Function_7_CCC",          # 07, 7
        "Function_8_DB3",          # 08, 8
        "Function_9_EAB",          # 09, 9
        "Function_10_F81",         # 0A, 10
        "Function_11_1000",        # 0B, 11
        "Function_12_10CD",        # 0C, 12
        "Function_13_11DC",        # 0D, 13
        "Function_14_11F2",        # 0E, 14
        "Function_15_1208",        # 0F, 15
        "Function_16_134B",        # 10, 16
        "Function_17_13DB",        # 11, 17
        "Function_18_1442",        # 12, 18
        "Function_19_14A9",        # 13, 19
        "Function_20_152A",        # 14, 20
        "Function_21_15AB",        # 15, 21
        "Function_22_1666",        # 16, 22
        "Function_23_1769",        # 17, 23
        "Function_24_17CC",        # 18, 24
        "Function_25_182F",        # 19, 25
        "Function_26_1847",        # 1A, 26
        "Function_27_18B2",        # 1B, 27
        "Function_28_18CB",        # 1C, 28
        "Function_29_18E3",        # 1D, 29
        "Function_30_18FB",        # 1E, 30
        "Function_31_1913",        # 1F, 31
        "Function_32_1969",        # 20, 32
        "Function_33_197C",        # 21, 33
        "Function_34_198F",        # 22, 34
        "Function_35_19F6",        # 23, 35
        "Function_36_1A2D",        # 24, 36
        "Function_37_1AB8",        # 25, 37
        "Function_38_1B1F",        # 26, 38
        "Function_39_1BA6",        # 27, 39
        "Function_40_1C4D",        # 28, 40
        "Function_41_1CA4",        # 29, 41
        "Function_42_1D14",        # 2A, 42
        "Function_43_1D61",        # 2B, 43
        "Function_44_1DB8",        # 2C, 44
        "Function_45_1DCB",        # 2D, 45
        "Function_46_1E43",        # 2E, 46
        "Function_47_1EDE",        # 2F, 47
        "Function_48_1EF6",        # 30, 48
        "Function_49_1F0E",        # 31, 49
        "Function_50_1F64",        # 32, 50
        "Function_51_1F77",        # 33, 51
        "Function_52_1F8A",        # 34, 52
        "Function_53_1FB1",        # 35, 53
        "Function_54_21DF",        # 36, 54
        "Function_55_23A8",        # 37, 55
    )


    def Function_0_7DA(): pass

    label("Function_0_7DA")

    OP_3E(0x383, 1)
    Return()

    # Function_0_7DA end

    def Function_1_7E0(): pass

    label("Function_1_7E0")

    Return()

    # Function_1_7E0 end

    def Function_2_7E1(): pass

    label("Function_2_7E1")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_7E1 end

    def Function_3_7F4(): pass

    label("Function_3_7F4")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        (
            "#5P#1000F通常\x01",
            "向き＃５Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "#11P#1001F笑顔\x01",
            "向き＃１１Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "#6P#1002F真剣\x01",
            "向き＃６Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "#12P#1003F悲哀１\x01",
            "向き＃１２Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#1004F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#1005F怒り１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#1006F通常（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#1007F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#1008F照れ１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "#1009F怒り２（ムッ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#1010F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "#1011F通常（口開）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "#1012F瞑目笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "#1013F照れ２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "#1014F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "#1015Fん～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "#1016F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "#1017F照れ３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "#1018F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#1019Fジト目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "#1020Fシリアス驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "#1021F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "#1022F叫び２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "#1023F泣き叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "#1024Fうつろ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "#1025F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "#1026Fうっすら悲しい驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#1027F悲哀２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_7F4 end

    def Function_4_A47(): pass

    label("Function_4_A47")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        (
            "#1030F通常Ａ\x01",
            "Ａは前半用\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#1031F笑顔Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "#1032F真剣Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "#1033F悲哀Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "#1034F驚愕Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "#1035F瞑目Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "#1036F怒りＡ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "#1037F苦痛Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "#1038F睨みＡ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "#1039F泣きＡ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "#1040F通常Ｂ\x01",
            "Ｂは後半用\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "#1041F笑顔Ｂ１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "#1042F真剣Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "#1043F悲哀Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "#1044F驚愕Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "#1046F怒りＢ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "#1047F苦痛Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "#1048Fジト目Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "#1049F笑顔Ｂ２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_A47 end

    def Function_5_BC0(): pass

    label("Function_5_BC0")

    TalkBegin(0xFE)

    ChrTalk(    #48
        0xFE,
        "#020F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "#870Fちびシェラ通常\x02\x03",

            "#871F笑顔\x02\x03",

            "#872F苦笑\x02\x03",

            "#873F困惑\x02\x03",

            "#874F慌て（あわわ）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_BC0 end

    def Function_6_C25(): pass

    label("Function_6_C25")

    TalkBegin(0xFE)

    ChrTalk(    #50
        0xFE,
        "#030F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#031F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#032F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "#033F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#034F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "#035F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "#036F慌て\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "#037F酔っ払い\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "#038F酔いつぶれ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "#039F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_C25 end

    def Function_7_CCC(): pass

    label("Function_7_CCC")

    TalkBegin(0xFE)

    ChrTalk(    #60
        0xFE,
        "#040F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "#041F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "#042F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "#043F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "#044F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "#045F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#046F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "#047F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "#048F笑顔２（お嬢様ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "#049F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "#540F赤面\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "#541F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "#542F苦笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_CCC end

    def Function_8_DB3(): pass

    label("Function_8_DB3")

    TalkBegin(0xFE)

    ChrTalk(    #73
        0xFE,
        "#050F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "#051F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "#052F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "#053F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "#054F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "#055F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "#056Fイタッ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "#057F殺意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "#058F毒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "#059F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "#550Fくっそー！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "#551F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "#552F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "#553Fうつろ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#554Fうつろ笑い\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_DB3 end

    def Function_9_EAB(): pass

    label("Function_9_EAB")

    TalkBegin(0xFE)

    ChrTalk(    #88
        0xFE,
        "#060F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "#061F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "#062F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "#063F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "#064F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "#065F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "#066F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "#067F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "#068F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#069F泣き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "#560F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#561F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "#562F照れ困惑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_EAB end

    def Function_10_F81(): pass

    label("Function_10_F81")

    TalkBegin(0xFE)

    ChrTalk(    #101
        0xFE,
        "#070F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "#071F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "#072F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "#073F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#074F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "#075F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "#076F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "#077F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_F81 end

    def Function_11_1000(): pass

    label("Function_11_1000")

    TalkBegin(0xFE)

    ChrTalk(    #109
        0xFE,
        "#1060F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "#1061F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#1062F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "#1063F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "#1064F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "#1065F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "#1066F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "#1067F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "#1068F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "#1069F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "#1070F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "#1071F笑顔３\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1000 end

    def Function_12_10CD(): pass

    label("Function_12_10CD")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0xFE,
        "#810F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "#811F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "#812F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "#813F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#814F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#815F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "#816F自信\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "#817F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "#818Fん～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "#819F苦笑１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#1310F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "#1311F夢見ごこち\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "#1312F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "#1313Fうつろ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "#1314F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "#1315F苦笑３\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_10CD end

    def Function_13_11DC(): pass

    label("Function_13_11DC")

    TalkBegin(0xFE)

    ChrTalk(    #137
        0xFE,
        "#210F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_11DC end

    def Function_14_11F2(): pass

    label("Function_14_11F2")

    TalkBegin(0xFE)

    ChrTalk(    #138
        0xFE,
        "#110F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_11F2 end

    def Function_15_1208(): pass

    label("Function_15_1208")

    TalkBegin(0xFE)

    ChrTalk(    #139
        0xFE,
        "#1180F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "#1181F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "#1182F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "#1183F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "#1184F驚愕１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "#1185F驚愕２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "#1186F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "#1187Fキリキリ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "#1188F大笑い\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "#1189F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "#1320F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "#1321F目そらし\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "#1322Fえっ！リシャールさまっ！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "#1323Fリシャールさまっ…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "#1324Fリシャールさまぁ～！！（号泣）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1208 end

    def Function_16_134B(): pass

    label("Function_16_134B")

    TalkBegin(0xFE)

    ChrTalk(    #154
        0xFE,
        "#840F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "#841F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "#842F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "#843F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "#844F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "#845F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "#846F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "#847F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "#848Fうつろ\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_134B end

    def Function_17_13DB(): pass

    label("Function_17_13DB")

    TalkBegin(0xFE)

    ChrTalk(    #163
        0xFE,
        "#1440F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "#1450F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "#1460F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "#1470F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "#1480F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "#1490F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_13DB end

    def Function_18_1442(): pass

    label("Function_18_1442")

    TalkBegin(0xFE)

    ChrTalk(    #169
        0xFE,
        "#1160F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "#1161F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "#1162F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "#1163F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "#1164F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "#1165F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_1442 end

    def Function_19_14A9(): pass

    label("Function_19_14A9")

    TalkBegin(0xFE)

    ChrTalk(    #175
        0xFE,
        "#820F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "#821F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "#822F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "#823F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "#824F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "#825F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "#826F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "#827Fうつろ\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_14A9 end

    def Function_20_152A(): pass

    label("Function_20_152A")

    TalkBegin(0xFE)

    ChrTalk(    #183
        0xFE,
        "#830F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "#831F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "#832F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "#833F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "#834F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "#835F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "#836F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "#837Fうつろ\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_152A end

    def Function_21_15AB(): pass

    label("Function_21_15AB")

    TalkBegin(0xFE)

    ChrTalk(    #191
        0xFE,
        "#250F通常（目ナシ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "#251F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "#252F笑顔（目ナシ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "#253F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "#254F真剣（目ナシ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "#255F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "#256F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "#257F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "#258F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "#259F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_15AB end

    def Function_22_1666(): pass

    label("Function_22_1666")

    TalkBegin(0xFE)

    ChrTalk(    #201
        0xFE,
        "#260F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "#261F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "#262F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "#263Fおすまし顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "#264F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "#265F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "#266Fスネ顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "#267Fん～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "#268F企み顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "#269F企み笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "#1300F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "#1301F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "#1302F殺意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "#1303F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "#1304F薄ら笑い\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1666 end

    def Function_23_1769(): pass

    label("Function_23_1769")

    TalkBegin(0xFE)

    ChrTalk(    #216
        0xFE,
        "#240F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "#241F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "#242F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "#243F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "#244F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "#245F苦痛？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1769 end

    def Function_24_17CC(): pass

    label("Function_24_17CC")

    TalkBegin(0xFE)

    ChrTalk(    #222
        0xFE,
        "#230F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "#231F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "#232F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "#233F驚愕？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "#234F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "#235F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_17CC end

    def Function_25_182F(): pass

    label("Function_25_182F")

    TalkBegin(0xFE)

    ChrTalk(    #228
        0xFE,
        "#120Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_182F end

    def Function_26_1847(): pass

    label("Function_26_1847")

    TalkBegin(0xFE)

    ChrTalk(    #229
        0xFE,
        "#1150F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        "#1151F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "#1152F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "#1153F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "#1154F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "#1155F笑顔２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_1847 end

    def Function_27_18B2(): pass

    label("Function_27_18B2")

    TalkBegin(0xFE)

    ChrTalk(    #235
        0xFE,
        "#1140Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_18B2 end

    def Function_28_18CB(): pass

    label("Function_28_18CB")

    TalkBegin(0xFE)

    ChrTalk(    #236
        0xFE,
        "#270Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_18CB end

    def Function_29_18E3(): pass

    label("Function_29_18E3")

    TalkBegin(0xFE)

    ChrTalk(    #237
        0xFE,
        "#170Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_18E3 end

    def Function_30_18FB(): pass

    label("Function_30_18FB")

    TalkBegin(0xFE)

    ChrTalk(    #238
        0xFE,
        "#700Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_18FB end

    def Function_31_1913(): pass

    label("Function_31_1913")

    TalkBegin(0xFE)

    ChrTalk(    #239
        0xFE,
        "#850F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "#851F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#852F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "#853F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "#854F薄ら笑い\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_1913 end

    def Function_32_1969(): pass

    label("Function_32_1969")

    TalkBegin(0xFE)

    ChrTalk(    #244
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_1969 end

    def Function_33_197C(): pass

    label("Function_33_197C")

    TalkBegin(0xFE)

    ChrTalk(    #245
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_197C end

    def Function_34_198F(): pass

    label("Function_34_198F")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        "#1210F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "#1211F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "#1212F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "#1213F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "#1190F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "#1191F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_198F end

    def Function_35_19F6(): pass

    label("Function_35_19F6")

    TalkBegin(0xFE)

    ChrTalk(    #252
        0xFE,
        "#1200F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "#1201F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "#1202F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_19F6 end

    def Function_36_1A2D(): pass

    label("Function_36_1A2D")

    TalkBegin(0xFE)

    ChrTalk(    #255
        0xFE,
        "#1130F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "#1131F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "#1132F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "#1133F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "#1134F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "#1135F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "#1136F悲哀２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "#1137F笑顔２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_1A2D end

    def Function_37_1AB8(): pass

    label("Function_37_1AB8")

    TalkBegin(0xFE)

    ChrTalk(    #263
        0xFE,
        "#1160F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "#1161F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        "#1162F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "#1163F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "#1164F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "#1165F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_1AB8 end

    def Function_38_1B1F(): pass

    label("Function_38_1B1F")

    TalkBegin(0xFE)

    ChrTalk(    #269
        0xFE,
        "#1120F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        "#1121F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "#1122F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "#1123F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "#1124F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "#1125F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "#1126F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "#1127F叫び\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_1B1F end

    def Function_39_1BA6(): pass

    label("Function_39_1BA6")

    TalkBegin(0xFE)

    ChrTalk(    #277
        0xFE,
        "#890F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "#891F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "#892F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "#893F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "#894F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "#895F悪通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "#896F悪笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "#897F悪真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "#898F悪驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "#899F悪瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_1BA6 end

    def Function_40_1C4D(): pass

    label("Function_40_1C4D")

    TalkBegin(0xFE)

    ChrTalk(    #287
        0xFE,
        "#1170F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "#1171F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "#1172F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "#1173F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "#1174F悲哀\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_1C4D end

    def Function_41_1CA4(): pass

    label("Function_41_1CA4")

    TalkBegin(0xFE)

    ChrTalk(    #292
        0xFE,
        "#880F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "#881F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "#882F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "#883F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "#884F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "#885F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "#886Fくっ\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1CA4 end

    def Function_42_1D14(): pass

    label("Function_42_1D14")

    TalkBegin(0xFE)

    ChrTalk(    #299
        0xFE,
        "#1100F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "#1101F真剣・驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "#1102F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "#1103F叫び\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_1D14 end

    def Function_43_1D61(): pass

    label("Function_43_1D61")

    TalkBegin(0xFE)

    ChrTalk(    #303
        0xFE,
        "#1110F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "#1111F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "#1112F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        "#1113F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "#1114F叫び\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1D61 end

    def Function_44_1DB8(): pass

    label("Function_44_1DB8")

    TalkBegin(0xFE)

    ChrTalk(    #308
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_1DB8 end

    def Function_45_1DCB(): pass

    label("Function_45_1DCB")

    TalkBegin(0xFE)

    ChrTalk(    #309
        0xFE,
        "#860F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        "#861F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        "#862F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "#863F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        "#864F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        "#865F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        "#866Fお嬢笑顔\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_1DCB end

    def Function_46_1E43(): pass

    label("Function_46_1E43")

    TalkBegin(0xFE)

    ChrTalk(    #316
        0xFE,
        "#1220F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        "#1221F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        "#1222F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        "#1223F悲哀（目そらし）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "#1224F困惑（驚愕）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        "#1225F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        "#1226F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        "#1227F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_1E43 end

    def Function_47_1EDE(): pass

    label("Function_47_1EDE")

    TalkBegin(0xFE)

    ChrTalk(    #324
        0xFE,
        "#190Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_1EDE end

    def Function_48_1EF6(): pass

    label("Function_48_1EF6")

    TalkBegin(0xFE)

    ChrTalk(    #325
        0xFE,
        "#200Fがおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_48_1EF6 end

    def Function_49_1F0E(): pass

    label("Function_49_1F0E")

    TalkBegin(0xFE)

    ChrTalk(    #326
        0xFE,
        (
            "#870Fちびシェラ通常\x02\x03",

            "#871F笑顔\x02\x03",

            "#872F苦笑\x02\x03",

            "#873F困惑\x02\x03",

            "#874F慌て（あわわ）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_1F0E end

    def Function_50_1F64(): pass

    label("Function_50_1F64")

    TalkBegin(0xFE)

    ChrTalk(    #327
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_1F64 end

    def Function_51_1F77(): pass

    label("Function_51_1F77")

    TalkBegin(0xFE)

    ChrTalk(    #328
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_51_1F77 end

    def Function_52_1F8A(): pass

    label("Function_52_1F8A")

    TalkBegin(0xFE)

    ChrTalk(    #329
        0xFE,
        "#1190F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "#1191F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_52_1F8A end

    def Function_53_1FB1(): pass

    label("Function_53_1FB1")

    TalkBegin(0xFE)

    ChrTalk(    #331
        0xFE,
        "#000F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "#001F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "#002F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        "#003F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        "#004F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        "#005F怒り１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "#006F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        "#007F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "#008F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        "#009F怒り２（ムッ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        "#500F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        "#501Fのんき\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        "#502Fえっへん\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        "#503F照れ２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        "#504F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        "#505Fん～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        "#506F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        "#507F挑発\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        "#508F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        "#509Fジト目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "#580Fシリアス驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        "#581F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        "#582F叫び２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xFE,
        "#583F怒り泣き(ED用) \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        "#584F薬飲み後１(ED用) \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        "#585F薬飲み後２(ED用) \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        "#586F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        "#587Fうっすら悲しい驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xFE,
        "#588F悲哀２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        "#589F号泣\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_53_1FB1 end

    def Function_54_21DF(): pass

    label("Function_54_21DF")

    TalkBegin(0xFE)

    ChrTalk(    #361
        0xFE,
        "#010F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        "#011F笑顔１（企み）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        "#012F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        "#013F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        "#014F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        "#015F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        "#016F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        "#017F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        "#018F照れ（ぼやき）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "#019F笑顔２（怒り）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        "#510F殺意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        "#511Fマジ照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        "#512F笑顔３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        "#513F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        "#514F暗示解除\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        "#515F暗示解除後叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        "#516F暗示解除後怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        "#517FED笑顔４\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        "#518FED通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        "#519FED俯き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        "#590FED俯き驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        "#591F暗示解除後叫び２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        "#592FED笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        "#593FED瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_54_21DF end

    def Function_55_23A8(): pass

    label("Function_55_23A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x383), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2418")
    EventBegin(0x0)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #385
        0x0,
        "アイテムを使ってみたよ！\x02",
    )

    Sleep(500)
    EventEnd(0x0)

    label("loc_2418")

    Return()

    # Function_55_23A8 end

    SaveToFile()

Try(main)
