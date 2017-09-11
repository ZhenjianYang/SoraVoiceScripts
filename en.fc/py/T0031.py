from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0031   ._SN',
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
        'CH00000エステル',                      # 9
        'CH00010ヨシュア',                      # 10
        'CH00020シェラ',                        # 11
        'CH00030オリビエ',                      # 12
        'CH00040クローゼ',                      # 13
        'エモーション',                         # 14
        'CH00050アガット',                      # 15
        'CH00060ティータ',                      # 16
        'CH00070ジン',                          # 17
        'CH02000カシウス親父',                  # 18
        'CH02010アリシア女王',                  # 19
        'CH02020Ｄｒ．ラッセル',                # 20
        'CH02030リシャール大佐',                # 21
        'CH02040レーヴェ',                      # 22
        'CH02050アルバ教授(ワイスマン)',        # 23
        'CH02060記者ナイアル',                  # 24
        'CH02070カメラマン・ドロシー',          # 25
        'CH02080モルガン将軍',                  # 26
        'CH02090親衛隊ユリア',                  # 27
        'CH02100元特務兵カノーネ隊長',          # 28
        'CH02110空賊団長男ドルン',              # 29
        'CH02120空賊団次男キール',              # 30
        'CH02130空賊団妹ジョゼット',            # 31
        'CH02140デュナン公爵',                  # 32
        'CH02190ミュラー',                      # 33
        'CH02200ロランス',                      # 34
        'CH02210エステル１１歳',                # 35
        'CH02220ヨシュア１１歳',                # 36
        'CH02230メイドエステル',                # 37
        'CH02240メイドヨシュア',                # 38
        'CH02260騎士エステル',                  # 39
        'CH02270騎士クローゼ',                  # 40
        'CH02280姫ヨシュア',                    # 41
        'CH02290温泉ヨシュア',                  # 42
        'CH02300温泉エステル',                  # 43
        'CH02310温泉ティータ',                  # 44
        'CH02320ジーク',                        # 45
        'CH02330学生ジョゼット',                # 46
        'CH02340姫クローゼ',                    # 47
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
        'ED6_DT07/CH02000 ._CH',             # 08
        'ED6_DT07/CH02010 ._CH',             # 09
        'ED6_DT07/CH02020 ._CH',             # 0A
        'ED6_DT07/CH02030 ._CH',             # 0B
        'ED6_DT07/CH02040 ._CH',             # 0C
        'ED6_DT07/CH02050 ._CH',             # 0D
        'ED6_DT07/CH02060 ._CH',             # 0E
        'ED6_DT07/CH02070 ._CH',             # 0F
        'ED6_DT07/CH02080 ._CH',             # 10
        'ED6_DT07/CH02090 ._CH',             # 11
        'ED6_DT07/CH02100 ._CH',             # 12
        'ED6_DT07/CH02110 ._CH',             # 13
        'ED6_DT07/CH02120 ._CH',             # 14
        'ED6_DT07/CH02130 ._CH',             # 15
        'ED6_DT07/CH02140 ._CH',             # 16
        'ED6_DT07/CH02190 ._CH',             # 17
        'ED6_DT07/CH02200 ._CH',             # 18
        'ED6_DT07/CH02210 ._CH',             # 19
        'ED6_DT07/CH02220 ._CH',             # 1A
        'ED6_DT07/CH02230 ._CH',             # 1B
        'ED6_DT07/CH02240 ._CH',             # 1C
        'ED6_DT07/CH02250 ._CH',             # 1D
        'ED6_DT07/CH02260 ._CH',             # 1E
        'ED6_DT07/CH02270 ._CH',             # 1F
        'ED6_DT07/CH02280 ._CH',             # 20
        'ED6_DT07/CH02290 ._CH',             # 21
        'ED6_DT07/CH02300 ._CH',             # 22
        'ED6_DT07/CH02310 ._CH',             # 23
        'ED6_DT07/CH02320 ._CH',             # 24
        'ED6_DT07/CH02330 ._CH',             # 25
        'ED6_DT07/CH02340 ._CH',             # 26
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
        'ED6_DT07/CH02000P._CP',             # 08
        'ED6_DT07/CH02010P._CP',             # 09
        'ED6_DT07/CH02020P._CP',             # 0A
        'ED6_DT07/CH02030P._CP',             # 0B
        'ED6_DT07/CH02040P._CP',             # 0C
        'ED6_DT07/CH02050P._CP',             # 0D
        'ED6_DT07/CH02060P._CP',             # 0E
        'ED6_DT07/CH02070P._CP',             # 0F
        'ED6_DT07/CH02080P._CP',             # 10
        'ED6_DT07/CH02090P._CP',             # 11
        'ED6_DT07/CH02100P._CP',             # 12
        'ED6_DT07/CH02110P._CP',             # 13
        'ED6_DT07/CH02120P._CP',             # 14
        'ED6_DT07/CH02130P._CP',             # 15
        'ED6_DT07/CH02140P._CP',             # 16
        'ED6_DT07/CH02190P._CP',             # 17
        'ED6_DT07/CH02200P._CP',             # 18
        'ED6_DT07/CH02210P._CP',             # 19
        'ED6_DT07/CH02220P._CP',             # 1A
        'ED6_DT07/CH02230P._CP',             # 1B
        'ED6_DT07/CH02240P._CP',             # 1C
        'ED6_DT07/CH02250P._CP',             # 1D
        'ED6_DT07/CH02260P._CP',             # 1E
        'ED6_DT07/CH02270P._CP',             # 1F
        'ED6_DT07/CH02280P._CP',             # 20
        'ED6_DT07/CH02290P._CP',             # 21
        'ED6_DT07/CH02300P._CP',             # 22
        'ED6_DT07/CH02310P._CP',             # 23
        'ED6_DT07/CH02320P._CP',             # 24
        'ED6_DT07/CH02330P._CP',             # 25
        'ED6_DT07/CH02340P._CP',             # 26
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 15000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )


    ScpFunction(
        "Function_0_6C2",          # 00, 0
        "Function_1_6C3",          # 01, 1
        "Function_2_6C4",          # 02, 2
        "Function_3_6DA",          # 03, 3
        "Function_4_6F0",          # 04, 4
        "Function_5_706",          # 05, 5
        "Function_6_72A",          # 06, 6
        "Function_7_74E",          # 07, 7
        "Function_8_763",          # 08, 8
        "Function_9_784",          # 09, 9
        "Function_10_7EB",         # 0A, 10
        "Function_11_942",         # 0B, 11
        "Function_12_B0B",         # 0C, 12
        "Function_13_BC6",         # 0D, 13
        "Function_14_C73",         # 0E, 14
        "Function_15_D2D",         # 0F, 15
        "Function_16_DFF",         # 10, 16
        "Function_17_EC2",         # 11, 17
        "Function_18_F14",         # 12, 18
        "Function_19_F84",         # 13, 19
        "Function_20_FD6",         # 14, 20
        "Function_21_1038",        # 15, 21
        "Function_22_1099",        # 16, 22
        "Function_23_11CF",        # 17, 23
        "Function_24_124F",        # 18, 24
        "Function_25_12E8",        # 19, 25
        "Function_26_133E",        # 1A, 26
        "Function_27_1381",        # 1B, 27
        "Function_28_13F1",        # 1C, 28
        "Function_29_1431",        # 1D, 29
        "Function_30_14C2",        # 1E, 30
        "Function_31_14E7",        # 1F, 31
        "Function_32_15A9",        # 20, 32
        "Function_33_15FB",        # 21, 33
        "Function_34_1683",        # 22, 34
        "Function_35_1715",        # 23, 35
        "Function_36_173A",        # 24, 36
        "Function_37_176E",        # 25, 37
        "Function_38_1792",        # 26, 38
        "Function_39_1820",        # 27, 39
        "Function_40_1873",        # 28, 40
        "Function_41_1997",        # 29, 41
        "Function_42_1A86",        # 2A, 42
        "Function_43_1B1F",        # 2B, 43
        "Function_44_1C05",        # 2C, 44
        "Function_45_1CC1",        # 2D, 45
        "Function_46_1D33",        # 2E, 46
        "Function_47_1D8C",        # 2F, 47
        "Function_48_1E26",        # 30, 48
    )


    def Function_0_6C2(): pass

    label("Function_0_6C2")

    Return()

    # Function_0_6C2 end

    def Function_1_6C3(): pass

    label("Function_1_6C3")

    Return()

    # Function_1_6C3 end

    def Function_2_6C4(): pass

    label("Function_2_6C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6C4")

    label("loc_6D9")

    Return()

    # Function_2_6C4 end

    def Function_3_6DA(): pass

    label("Function_3_6DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EF")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_6DA")

    label("loc_6EF")

    Return()

    # Function_3_6DA end

    def Function_4_6F0(): pass

    label("Function_4_6F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_705")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_4_6F0")

    label("loc_705")

    Return()

    # Function_4_6F0 end

    def Function_5_706(): pass

    label("Function_5_706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_729")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_5_706")

    label("loc_729")

    Return()

    # Function_5_706 end

    def Function_6_72A(): pass

    label("Function_6_72A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74D")
    OP_8D(0xFE, 22000, 20000, 42000, 30000, 1500)
    Jump("Function_6_72A")

    label("loc_74D")

    Return()

    # Function_6_72A end

    def Function_7_74E(): pass

    label("Function_7_74E")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "はにゃ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_74E end

    def Function_8_763(): pass

    label("Function_8_763")

    TalkBegin(0xFE)
    OP_1D(0x4)

    ChrTalk(    #1
        0xFE,
        "ＢＧＭかえるにゃ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_763 end

    def Function_9_784(): pass

    label("Function_9_784")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "ＢＧＭさげるにょ。\x02",
    )

    OP_1F(0x5A, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "ＢＧＭもっとさげるにょ。\x02",
    )

    OP_1F(0x46, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "ＢＧＭもどすにょ。\x02",
    )

    OP_1F(0x64, 0x7D0)
    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_784 end

    def Function_10_7EB(): pass

    label("Function_10_7EB")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#000F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#001F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#002F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#003F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#004F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "#005F怒り１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#006F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "#007F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "#008F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "#009F怒り２（ムッ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "#500F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "#501Fのんき\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "#502Fえっへん\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "#503F照れ２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "#504F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#505Fん～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "#506F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "#507F挑発\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "#508F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "#509Fジト目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_7EB end

    def Function_11_942(): pass

    label("Function_11_942")

    TalkBegin(0xFE)

    ChrTalk(    #25
        0xFE,
        "#010F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "#011F笑顔１（企み）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "#012F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#013F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "#014F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#015F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "#016F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "#017F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "#018F照れ（ぼやき）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "#019F笑顔２（怒り）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "#510F殺意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "#511Fマジ照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "#512F笑顔３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "#513F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "#514F暗示解除\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "#515F暗示解除後叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "#516F暗示解除後怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "#517FED笑顔４\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "#518FED通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "#519FED俯き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "#590FED俯き驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "#591F暗示解除後叫び２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "#592FED笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "#593FED瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_942 end

    def Function_12_B0B(): pass

    label("Function_12_B0B")

    TalkBegin(0xFE)

    ChrTalk(    #49
        0xFE,
        "#020F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "#021F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#022F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#023F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "#024F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#025F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "#026F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "#027F誘惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "#028F酔っ払い（いい気分）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "#029F酔っ払い（不機嫌）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_B0B end

    def Function_13_BC6(): pass

    label("Function_13_BC6")

    TalkBegin(0xFE)
    OP_62(0xB, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(    #59
        0xFE,
        "#030F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "#031F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "#032F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "#033F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "#034F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "#035F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "#036F慌て\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#037F酔っ払い\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "#038F酔いつぶれ\x02",
    )

    CloseMessageWindow()
    OP_63(0xB)
    TalkEnd(0xFE)
    Return()

    # Function_13_BC6 end

    def Function_14_C73(): pass

    label("Function_14_C73")

    TalkBegin(0xFE)

    ChrTalk(    #68
        0xFE,
        "#040F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "#041F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "#042F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "#043F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "#044F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "#045F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "#046F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "#047F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "#048F笑顔２（お嬢様ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "#049F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_C73 end

    def Function_15_D2D(): pass

    label("Function_15_D2D")

    TalkBegin(0xFE)

    ChrTalk(    #78
        0xFE,
        "#050F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "#051F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "#052F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "#053F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "#054F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "#055F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "#056Fイタッ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "#057F殺意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "#058F毒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#059F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "#550Fくっそー！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "#551F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "#552F悲哀\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_D2D end

    def Function_16_DFF(): pass

    label("Function_16_DFF")

    TalkBegin(0xFE)

    ChrTalk(    #91
        0xFE,
        "#060F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "#061F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "#062F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "#063F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "#064F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "#065F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#066F笑顔２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "#067F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#068F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "#069F泣き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "#560F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "#561F溜息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_DFF end

    def Function_17_EC2(): pass

    label("Function_17_EC2")

    TalkBegin(0xFE)

    ChrTalk(    #103
        0xFE,
        "#070F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "#071F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#072F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "#073F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "#074F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_EC2 end

    def Function_18_F14(): pass

    label("Function_18_F14")

    TalkBegin(0xFE)

    ChrTalk(    #108
        0xFE,
        "#080F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "#081F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "#082F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#083F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "#084F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "#085F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "#086F怒り\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_F14 end

    def Function_19_F84(): pass

    label("Function_19_F84")

    TalkBegin(0xFE)

    ChrTalk(    #115
        0xFE,
        "#090F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "#091F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "#092F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "#093F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "#094F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_F84 end

    def Function_20_FD6(): pass

    label("Function_20_FD6")

    TalkBegin(0xFE)

    ChrTalk(    #120
        0xFE,
        "#100F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "#101F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "#102F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "#103F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "#104F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#105F笑顔2\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_FD6 end

    def Function_21_1038(): pass

    label("Function_21_1038")

    TalkBegin(0xFE)

    ChrTalk(    #126
        0xFE,
        "#110F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "#111F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "#112F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "#113F驚き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "#114F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#115F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1038 end

    def Function_22_1099(): pass

    label("Function_22_1099")

    TalkBegin(0xFE)

    ChrTalk(    #132
        0xFE,
        "#120F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "#121F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "#122F振り向き\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "#123F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "#124F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "#280Fロランスバージョン通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "#281Fロランスバージョン口閉じ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "#282Fロランス（メットなし）通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "#283Fロランス（メットなし）通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "#284Fロランス（メットなし）笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "#285Fロランス（メットなし）瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1099 end

    def Function_23_11CF(): pass

    label("Function_23_11CF")

    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        "#130F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "#131F慌て\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "#132F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "#133FED用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "#134FED用笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "#135FED用真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "#136FED用瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_11CF end

    def Function_24_124F(): pass

    label("Function_24_124F")

    TalkBegin(0xFE)

    ChrTalk(    #150
        0xFE,
        "#140F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "#141F笑顔１（ニヤリ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "#142F疑い\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "#143F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "#144F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "#145F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "#146F酔っ払い\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "#147F笑顔２（満面）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_124F end

    def Function_25_12E8(): pass

    label("Function_25_12E8")

    TalkBegin(0xFE)

    ChrTalk(    #158
        0xFE,
        "#150F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "#151F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "#152Fウルウル\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "#153F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "#154F困惑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_12E8 end

    def Function_26_133E(): pass

    label("Function_26_133E")

    TalkBegin(0xFE)

    ChrTalk(    #163
        0xFE,
        "#160F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "#161F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "#162F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "#163F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_133E end

    def Function_27_1381(): pass

    label("Function_27_1381")

    TalkBegin(0xFE)

    ChrTalk(    #167
        0xFE,
        "#170F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "#171F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "#172F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "#173F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "#174F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "#175F憂鬱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "#176F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_1381 end

    def Function_28_13F1(): pass

    label("Function_28_13F1")

    TalkBegin(0xFE)

    ChrTalk(    #174
        0xFE,
        "#180F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "#181F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "#182F通常２（優しげ）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_13F1 end

    def Function_29_1431(): pass

    label("Function_29_1431")

    TalkBegin(0xFE)

    ChrTalk(    #177
        0xFE,
        "#190F通常（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "#191F笑顔（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "#192F驚愕（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "#193F通常（狂気）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "#194F笑顔（狂気）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "#195F怒り（狂気）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_1431 end

    def Function_30_14C2(): pass

    label("Function_30_14C2")

    TalkBegin(0xFE)

    ChrTalk(    #183
        0xFE,
        "#200F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "#201F真剣\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_14C2 end

    def Function_31_14E7(): pass

    label("Function_31_14E7")

    TalkBegin(0xFE)

    ChrTalk(    #185
        0xFE,
        "#210F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "#211F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "#212F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "#213F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "#214F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "#215F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "#216F慌て\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "#217F変装通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "#218F変装笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "#219F変装空賊顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "#410F変装バカ笑い\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_14E7 end

    def Function_32_15A9(): pass

    label("Function_32_15A9")

    TalkBegin(0xFE)

    ChrTalk(    #196
        0xFE,
        "#290F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "#291F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "#292F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "#293F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "#294F怒り\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_15A9 end

    def Function_33_15FB(): pass

    label("Function_33_15FB")

    TalkBegin(0xFE)

    ChrTalk(    #201
        0xFE,
        "#300F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "#301F無表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "#302F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "#303Fいたっ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "#304Fあっけらかん\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "#305F寝顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "#306F寝顔（お目覚め）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_15FB end

    def Function_34_1683(): pass

    label("Function_34_1683")

    TalkBegin(0xFE)

    ChrTalk(    #208
        0xFE,
        "#220F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "#221F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "#222F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "#223F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "#224F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "#225F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "#226F慌て\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "#227F酔っ払い\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        "#228F気絶\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_1683 end

    def Function_35_1715(): pass

    label("Function_35_1715")

    TalkBegin(0xFE)

    ChrTalk(    #217
        0xFE,
        "#310F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "#311F笑顔\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1715 end

    def Function_36_173A(): pass

    label("Function_36_173A")

    TalkBegin(0xFE)

    ChrTalk(    #219
        0xFE,
        "#270F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "#271F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "#272F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_173A end

    def Function_37_176E(): pass

    label("Function_37_176E")

    TalkBegin(0xFE)

    ChrTalk(    #222
        0xFE,
        "#280Fロランスバージョン\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_176E end

    def Function_38_1792(): pass

    label("Function_38_1792")

    TalkBegin(0xFE)

    ChrTalk(    #223
        0xFE,
        "#320F通常1（のんき）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "#321F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "#322F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "#323F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "#324F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        "#325F通常2（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "#326F怒り２（ムッ）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_1792 end

    def Function_39_1820(): pass

    label("Function_39_1820")

    TalkBegin(0xFE)

    ChrTalk(    #230
        0xFE,
        "#330F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "#331F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "#332F真剣 \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "#333F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "#334F溜息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_1820 end

    def Function_40_1873(): pass

    label("Function_40_1873")

    TalkBegin(0xFE)

    ChrTalk(    #235
        0xFE,
        "#340F通常（のんき） \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        "#341F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "#342F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "#343F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "#344F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "#345F怒り１（叫び）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#346F通常（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "#347F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "#348F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        "#349F怒り２（ムッ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "#840F劇用通常 \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "#841F劇用真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "#842F劇用驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "#843F劇用叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "#844F劇用瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_1873 end

    def Function_41_1997(): pass

    label("Function_41_1997")

    TalkBegin(0xFE)

    ChrTalk(    #250
        0xFE,
        "#350F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "#351F笑顔１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "#352F真剣・劇用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "#353F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "#354F驚愕・劇用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "#355F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "#356F怒り・劇用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "#357F瞑目・劇用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "#358F笑顔２（お嬢様ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "#359F悲哀２（深刻）・劇用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "#850F劇用苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1997 end

    def Function_42_1A86(): pass

    label("Function_42_1A86")

    TalkBegin(0xFE)

    ChrTalk(    #261
        0xFE,
        "#360F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "#361F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        "#362F真剣 \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "#363F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        "#364F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "#365F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "#366F叫び\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "#367F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        "#368F照れ（ぼやき）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_1A86 end

    def Function_43_1B1F(): pass

    label("Function_43_1B1F")

    TalkBegin(0xFE)

    ChrTalk(    #270
        0xFE,
        "#370F通常１（のんき） \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "#371F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "#372F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "#373F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "#374F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "#375F怒り１（叫び）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "#376F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        "#377F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "#378F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "#379F怒り２（ムッ）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "#440F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "#441F赤面\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1B1F end

    def Function_44_1C05(): pass

    label("Function_44_1C05")

    TalkBegin(0xFE)

    ChrTalk(    #282
        0xFE,
        "#380F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "#381F笑顔１（企み）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "#382F真剣 \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "#383F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "#384F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "#385F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "#386F怒り\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "#387F溜息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "#388F照れ（ぼやき）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "#389F笑顔２（怒り）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_1C05 end

    def Function_45_1CC1(): pass

    label("Function_45_1CC1")

    TalkBegin(0xFE)

    ChrTalk(    #292
        0xFE,
        "#390F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "#391F笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "#392F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "#393F驚愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "#394F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "#395F照れ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "#396F通常２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_1CC1 end

    def Function_46_1D33(): pass

    label("Function_46_1D33")

    TalkBegin(0xFE)

    ChrTalk(    #299
        0xFE,
        "#217F変装通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "#218F変装笑顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "#219F変装空賊顔\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "#410F変装バカ笑い\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_1D33 end

    def Function_47_1D8C(): pass

    label("Function_47_1D8C")

    TalkBegin(0xFE)

    ChrTalk(    #303
        0xFE,
        "#400F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "#401F笑顔（お嬢様ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "#402F真剣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        "#403F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "#404F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "#405Fえへへ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "#406F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        "#407F怒り\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_1D8C end

    def Function_48_1E26(): pass

    label("Function_48_1E26")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_251A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "エモーションテスト\x01",      # 0
            "ルビ表示テスト\x01",          # 1
            "音量テスト\x01",              # 2
            "キャンセル\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EAE"),
        (1, "loc_21B9"),
        (2, "loc_24A7"),
        (SWITCH_DEFAULT, "loc_250A"),
    )


    label("loc_1EAE")

    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    AnonymousTalk(    #311
        "\x07\x00#020F？\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    AnonymousTalk(    #312
        "\x07\x00#020F！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    AnonymousTalk(    #313
        "\x07\x00#020F♪\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    AnonymousTalk(    #314
        "\x07\x00#020F㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #315
        "\x07\x00#020Fムカ\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #316
        "\x07\x00#020Fモヤモヤ\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #317
        "\x07\x00#020F冷汗\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #318
        "\x07\x00#020F青ざめ\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    AnonymousTalk(    #319
        "\x07\x00#020F…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)

    AnonymousTalk(    #320
        "\x07\x00#020FＺｚｚ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)

    AnonymousTalk(    #321
        "\x07\x00#020F閃き\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    AnonymousTalk(    #322
        "\x07\x00#020Fワイワイ\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    AnonymousTalk(    #323
        "\x07\x00#020Fパッ\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    AnonymousTalk(    #324
        "\x07\x00#020Fアセアセ\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)

    AnonymousTalk(    #325
        "\x07\x00#020Fドカン！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)

    AnonymousTalk(    #326
        "\x07\x00#020Fピヨリ\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    AnonymousTalk(    #327
        "\x07\x00#020Fキラキラ\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 1900, 0x33, 0x35, 0xC8, 0x0)

    AnonymousTalk(    #328
        "\x07\x00#020Fグルグル\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x3B, 0x3C, 0xFA, 0x2)

    AnonymousTalk(    #329
        "\x07\x00#020F話しかける\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x3D, 0x3E, 0xFA, 0x2)

    AnonymousTalk(    #330
        "\x07\x00#020Fルックポイント\x02",
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_21B9")


    ChrTalk(    #331
        0xFE,
        "#040Fルビのテスト。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "#040F導力器#6Rオーブメント#。遊撃士#6R ブレイサー#。\x01",
            "拓#2Rひら#かれし時代の物語。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "#040F導力機関#8Rオーバルエンジン#、導力砲#8R　 オーバルカノン#（←文中限定）。\x01",
            "遊撃士協会#10R　ブレイサーギルド#、七耀石#6R セプチウム#、身喰らう蛇#10R ウ　ロ　ボ　ロ　ス　#。\x01",
            "七の至宝#8Rセプト＝テリオン#、“七至宝”#10R　セプト＝テリオン　#、七 至 宝#8Rセプト＝テリオン#（←保留中）。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "#040F『銀閃#4Rぎんせん#のシェラザード』、女神#4Rエイドス#。\x01",
            "養父#4R と　う #さん、王都#6R　 グランセル#（←文中限定）。\x01",
            "導力魔法#8R オーバルアーツ #、結晶回路#8R ク　オ　ー　ツ #、翠耀石#6R エスメラス#。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "#040F文中限定を行頭で使うと以下のような悲劇が。\x01",
            "王都#6R　 グランセル#（←文中限定）。\x01",
            "導力砲#8R　 オーバルカノン#（←文中限定）。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_24A7")


    ChrTalk(    #336
        0xFE,
        "ＢＧＭさげるにょ。\x02",
    )

    OP_1F(0x5A, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "ＢＧＭもっとさげるにょ。\x02",
    )

    OP_1F(0x46, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        "ＢＧＭもどすにょ。\x02",
    )

    OP_1F(0x64, 0x7D0)
    CloseMessageWindow()
    Jump("loc_2517")

    label("loc_250A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2517")

    label("loc_2517")

    Jump("loc_1E33")

    label("loc_251A")

    TalkEnd(0xFE)
    Return()

    # Function_48_1E26 end

    SaveToFile()

Try(main)
