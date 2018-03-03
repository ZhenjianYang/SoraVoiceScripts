from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0022   ._SN',
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
        '00130シェラ待機',                      # 9
        '00131シェラ移動',                      # 10
        '00132シェラ攻撃',                      # 11
        '00133シェラ弾かれ',                    # 12
        '00134シェラ倒れ',                      # 13
        '00135シェラ魔法詠唱',                  # 14
        '00136シェラ魔法発射',                  # 15
        '00137シェラ勝利',                      # 16
        '00160ティータ待機',                    # 17
        '00161ティータ移動',                    # 18
        '00162ティータ攻撃',                    # 19
        '00163ティータ弾かれ',                  # 20
        '00164ティータ倒れ',                    # 21
        '00165ティータ魔法詠唱',                # 22
        '00166ティータ魔法発射',                # 23
        '00167ティータ勝利',                    # 24
        '00140クローゼ待機',                    # 25
        '00141クローゼ移動',                    # 26
        '00142クローゼ攻撃',                    # 27
        '00143クローゼ弾かれ',                  # 28
        '00144クローゼ倒れ',                    # 29
        '00145クローゼ魔法詠唱',                # 30
        '00146クローゼ魔法発射',                # 31
        '00147クローゼ勝利',                    # 32
        '04210クローゼ待機',                    # 33
        '04211クローゼ移動',                    # 34
        '04212クローゼ攻撃',                    # 35
        '04213クローゼ弾かれ',                  # 36
        '04214クローゼ倒れ',                    # 37
        '04215クローゼ魔法詠唱',                # 38
        '04216クローゼ魔法発射',                # 39
        '04217クローゼ勝利',                    # 40
        '00110ヨシュア待機',                    # 41
        '00111ヨシュア移動',                    # 42
        '00112ヨシュア攻撃',                    # 43
        '00113ヨシュア弾かれ',                  # 44
        '00114ヨシュア倒れ',                    # 45
        '00115ヨシュア魔法詠唱',                # 46
        '00116ヨシュア魔法発射',                # 47
        '00117ヨシュア勝利',                    # 48
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
        'ED6_DT07/CH00110 ._CH',             # 00
        'ED6_DT07/CH00111 ._CH',             # 01
        'ED6_DT07/CH00112 ._CH',             # 02
        'ED6_DT07/CH00113 ._CH',             # 03
        'ED6_DT07/CH00114 ._CH',             # 04
        'ED6_DT07/CH00115 ._CH',             # 05
        'ED6_DT07/CH00116 ._CH',             # 06
        'ED6_DT07/CH00117 ._CH',             # 07
        'ED6_DT07/CH00113 ._CH',             # 08
        'ED6_DT07/CH00113 ._CH',             # 09
        'ED6_DT07/CH00113 ._CH',             # 0A
        'ED6_DT07/CH00113 ._CH',             # 0B
        'ED6_DT07/CH00120 ._CH',             # 0C
        'ED6_DT07/CH00121 ._CH',             # 0D
        'ED6_DT07/CH00122 ._CH',             # 0E
        'ED6_DT07/CH00123 ._CH',             # 0F
        'ED6_DT07/CH00124 ._CH',             # 10
        'ED6_DT07/CH00125 ._CH',             # 11
        'ED6_DT07/CH00126 ._CH',             # 12
        'ED6_DT07/CH00127 ._CH',             # 13
        'ED6_DT07/CH00123 ._CH',             # 14
        'ED6_DT07/CH00123 ._CH',             # 15
        'ED6_DT07/CH00123 ._CH',             # 16
        'ED6_DT07/CH00123 ._CH',             # 17
        'ED6_DT07/CH00160 ._CH',             # 18
        'ED6_DT07/CH00161 ._CH',             # 19
        'ED6_DT07/CH00162 ._CH',             # 1A
        'ED6_DT07/CH00163 ._CH',             # 1B
        'ED6_DT07/CH00164 ._CH',             # 1C
        'ED6_DT07/CH00165 ._CH',             # 1D
        'ED6_DT07/CH00166 ._CH',             # 1E
        'ED6_DT07/CH00167 ._CH',             # 1F
        'ED6_DT07/CH00163 ._CH',             # 20
        'ED6_DT07/CH00163 ._CH',             # 21
        'ED6_DT07/CH00163 ._CH',             # 22
        'ED6_DT07/CH00163 ._CH',             # 23
        'ED6_DT07/CH00140 ._CH',             # 24
        'ED6_DT07/CH00141 ._CH',             # 25
        'ED6_DT07/CH00142 ._CH',             # 26
        'ED6_DT07/CH00143 ._CH',             # 27
        'ED6_DT07/CH00144 ._CH',             # 28
        'ED6_DT07/CH00145 ._CH',             # 29
        'ED6_DT07/CH00146 ._CH',             # 2A
        'ED6_DT07/CH00147 ._CH',             # 2B
        'ED6_DT07/CH00143 ._CH',             # 2C
        'ED6_DT07/CH00143 ._CH',             # 2D
        'ED6_DT07/CH00143 ._CH',             # 2E
        'ED6_DT07/CH00143 ._CH',             # 2F
        'ED6_DT27/CH04210 ._CH',             # 30
        'ED6_DT27/CH04211 ._CH',             # 31
        'ED6_DT27/CH04212 ._CH',             # 32
        'ED6_DT27/CH04213 ._CH',             # 33
        'ED6_DT27/CH04214 ._CH',             # 34
        'ED6_DT27/CH04215 ._CH',             # 35
        'ED6_DT27/CH04216 ._CH',             # 36
        'ED6_DT27/CH04217 ._CH',             # 37
        'ED6_DT27/CH04213 ._CH',             # 38
        'ED6_DT27/CH04213 ._CH',             # 39
        'ED6_DT27/CH04213 ._CH',             # 3A
        'ED6_DT27/CH04213 ._CH',             # 3B
    )

    AddCharChipPat(
        'ED6_DT07/CH00110P._CP',             # 00
        'ED6_DT07/CH00111P._CP',             # 01
        'ED6_DT07/CH00112P._CP',             # 02
        'ED6_DT07/CH00113P._CP',             # 03
        'ED6_DT07/CH00114P._CP',             # 04
        'ED6_DT07/CH00115P._CP',             # 05
        'ED6_DT07/CH00116P._CP',             # 06
        'ED6_DT07/CH00117P._CP',             # 07
        'ED6_DT07/CH00113P._CP',             # 08
        'ED6_DT07/CH00113P._CP',             # 09
        'ED6_DT07/CH00113P._CP',             # 0A
        'ED6_DT07/CH00113P._CP',             # 0B
        'ED6_DT07/CH00120P._CP',             # 0C
        'ED6_DT07/CH00121P._CP',             # 0D
        'ED6_DT07/CH00122P._CP',             # 0E
        'ED6_DT07/CH00123P._CP',             # 0F
        'ED6_DT07/CH00124P._CP',             # 10
        'ED6_DT07/CH00125P._CP',             # 11
        'ED6_DT07/CH00126P._CP',             # 12
        'ED6_DT07/CH00127P._CP',             # 13
        'ED6_DT07/CH00123P._CP',             # 14
        'ED6_DT07/CH00123P._CP',             # 15
        'ED6_DT07/CH00123P._CP',             # 16
        'ED6_DT07/CH00123P._CP',             # 17
        'ED6_DT07/CH00160P._CP',             # 18
        'ED6_DT07/CH00161P._CP',             # 19
        'ED6_DT07/CH00162P._CP',             # 1A
        'ED6_DT07/CH00163P._CP',             # 1B
        'ED6_DT07/CH00164P._CP',             # 1C
        'ED6_DT07/CH00165P._CP',             # 1D
        'ED6_DT07/CH00166P._CP',             # 1E
        'ED6_DT07/CH00167P._CP',             # 1F
        'ED6_DT07/CH00163P._CP',             # 20
        'ED6_DT07/CH00163P._CP',             # 21
        'ED6_DT07/CH00163P._CP',             # 22
        'ED6_DT07/CH00163P._CP',             # 23
        'ED6_DT07/CH00140P._CP',             # 24
        'ED6_DT07/CH00141P._CP',             # 25
        'ED6_DT07/CH00142P._CP',             # 26
        'ED6_DT07/CH00143P._CP',             # 27
        'ED6_DT07/CH00144P._CP',             # 28
        'ED6_DT07/CH00145P._CP',             # 29
        'ED6_DT07/CH00146P._CP',             # 2A
        'ED6_DT07/CH00147P._CP',             # 2B
        'ED6_DT07/CH00143P._CP',             # 2C
        'ED6_DT07/CH00143P._CP',             # 2D
        'ED6_DT07/CH00143P._CP',             # 2E
        'ED6_DT07/CH00143P._CP',             # 2F
        'ED6_DT27/CH04210P._CP',             # 30
        'ED6_DT27/CH04211P._CP',             # 31
        'ED6_DT27/CH04212P._CP',             # 32
        'ED6_DT27/CH04213P._CP',             # 33
        'ED6_DT27/CH04214P._CP',             # 34
        'ED6_DT27/CH04215P._CP',             # 35
        'ED6_DT27/CH04216P._CP',             # 36
        'ED6_DT27/CH04217P._CP',             # 37
        'ED6_DT27/CH04213P._CP',             # 38
        'ED6_DT27/CH04213P._CP',             # 39
        'ED6_DT27/CH04213P._CP',             # 3A
        'ED6_DT27/CH04213P._CP',             # 3B
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 16,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 17,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
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
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 19,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 21,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 22,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 23,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 53,
        ChipIndex           = 0x35,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 24,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 25,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 26,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
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
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 27,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
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
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 28,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 29,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 30,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )


    ScpFunction(
        "Function_0_78A",          # 00, 0
        "Function_1_78B",          # 01, 1
        "Function_2_78C",          # 02, 2
        "Function_3_7A2",          # 03, 3
        "Function_4_7B8",          # 04, 4
        "Function_5_7D3",          # 05, 5
        "Function_6_7EE",          # 06, 6
        "Function_7_809",          # 07, 7
        "Function_8_824",          # 08, 8
        "Function_9_83A",          # 09, 9
        "Function_10_871",         # 0A, 10
        "Function_11_88C",         # 0B, 11
        "Function_12_8A7",         # 0C, 12
        "Function_13_8BD",         # 0D, 13
        "Function_14_8F4",         # 0E, 14
        "Function_15_90F",         # 0F, 15
        "Function_16_92A",         # 10, 16
        "Function_17_940",         # 11, 17
        "Function_18_977",         # 12, 18
        "Function_19_992",         # 13, 19
        "Function_20_9AD",         # 14, 20
        "Function_21_9C3",         # 15, 21
        "Function_22_9FA",         # 16, 22
        "Function_23_A15",         # 17, 23
        "Function_24_A30",         # 18, 24
        "Function_25_A46",         # 19, 25
        "Function_26_A7D",         # 1A, 26
        "Function_27_A9D",         # 1B, 27
        "Function_28_AB8",         # 1C, 28
        "Function_29_ACE",         # 1D, 29
        "Function_30_B05",         # 1E, 30
        "Function_31_B20",         # 1F, 31
        "Function_32_B3B",         # 20, 32
    )


    def Function_0_78A(): pass

    label("Function_0_78A")

    Return()

    # Function_0_78A end

    def Function_1_78B(): pass

    label("Function_1_78B")

    Return()

    # Function_1_78B end

    def Function_2_78C(): pass

    label("Function_2_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A1")
    OP_99(0xFE, 0x0, 0x7, 0x708)
    Jump("Function_2_78C")

    label("loc_7A1")

    Return()

    # Function_2_78C end

    def Function_3_7A2(): pass

    label("Function_3_7A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B7")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_7A2")

    label("loc_7B7")

    Return()

    # Function_3_7A2 end

    def Function_4_7B8(): pass

    label("Function_4_7B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D2")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_4_7B8")

    label("loc_7D2")

    Return()

    # Function_4_7B8 end

    def Function_5_7D3(): pass

    label("Function_5_7D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7ED")
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Sleep(500)
    Jump("Function_5_7D3")

    label("loc_7ED")

    Return()

    # Function_5_7D3 end

    def Function_6_7EE(): pass

    label("Function_6_7EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_808")
    OP_99(0xFE, 0x0, 0x3, 0x7D0)
    Sleep(500)
    Jump("Function_6_7EE")

    label("loc_808")

    Return()

    # Function_6_7EE end

    def Function_7_809(): pass

    label("Function_7_809")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_823")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_7_809")

    label("loc_823")

    Return()

    # Function_7_809 end

    def Function_8_824(): pass

    label("Function_8_824")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_839")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_8_824")

    label("loc_839")

    Return()

    # Function_8_824 end

    def Function_9_83A(): pass

    label("Function_9_83A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_870")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_9_83A")

    label("loc_870")

    Return()

    # Function_9_83A end

    def Function_10_871(): pass

    label("Function_10_871")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88B")
    OP_99(0xFE, 0x0, 0xE, 0x7D0)
    Sleep(500)
    Jump("Function_10_871")

    label("loc_88B")

    Return()

    # Function_10_871 end

    def Function_11_88C(): pass

    label("Function_11_88C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A6")
    OP_99(0xFE, 0x0, 0x9, 0x7D0)
    Sleep(500)
    Jump("Function_11_88C")

    label("loc_8A6")

    Return()

    # Function_11_88C end

    def Function_12_8A7(): pass

    label("Function_12_8A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BC")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_12_8A7")

    label("loc_8BC")

    Return()

    # Function_12_8A7 end

    def Function_13_8BD(): pass

    label("Function_13_8BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F3")
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 18)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_13_8BD")

    label("loc_8F3")

    Return()

    # Function_13_8BD end

    def Function_14_8F4(): pass

    label("Function_14_8F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90E")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("Function_14_8F4")

    label("loc_90E")

    Return()

    # Function_14_8F4 end

    def Function_15_90F(): pass

    label("Function_15_90F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_929")
    OP_99(0xFE, 0x0, 0xD, 0x7D0)
    Sleep(500)
    Jump("Function_15_90F")

    label("loc_929")

    Return()

    # Function_15_90F end

    def Function_16_92A(): pass

    label("Function_16_92A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93F")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_16_92A")

    label("loc_93F")

    Return()

    # Function_16_92A end

    def Function_17_940(): pass

    label("Function_17_940")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_976")
    SetChrChipByIndex(0xFE, 29)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 30)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_17_940")

    label("loc_976")

    Return()

    # Function_17_940 end

    def Function_18_977(): pass

    label("Function_18_977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_991")
    OP_99(0xFE, 0x0, 0xE, 0x3E8)
    Sleep(1000)
    Jump("Function_18_977")

    label("loc_991")

    Return()

    # Function_18_977 end

    def Function_19_992(): pass

    label("Function_19_992")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9AC")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_19_992")

    label("loc_9AC")

    Return()

    # Function_19_992 end

    def Function_20_9AD(): pass

    label("Function_20_9AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C2")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_20_9AD")

    label("loc_9C2")

    Return()

    # Function_20_9AD end

    def Function_21_9C3(): pass

    label("Function_21_9C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F9")
    SetChrChipByIndex(0xFE, 41)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 42)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_21_9C3")

    label("loc_9F9")

    Return()

    # Function_21_9C3 end

    def Function_22_9FA(): pass

    label("Function_22_9FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A14")
    OP_99(0xFE, 0x0, 0x14, 0x7D0)
    Sleep(500)
    Jump("Function_22_9FA")

    label("loc_A14")

    Return()

    # Function_22_9FA end

    def Function_23_A15(): pass

    label("Function_23_A15")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2F")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_23_A15")

    label("loc_A2F")

    Return()

    # Function_23_A15 end

    def Function_24_A30(): pass

    label("Function_24_A30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A45")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_24_A30")

    label("loc_A45")

    Return()

    # Function_24_A30 end

    def Function_25_A46(): pass

    label("Function_25_A46")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7C")
    SetChrChipByIndex(0xFE, 53)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 54)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_25_A46")

    label("loc_A7C")

    Return()

    # Function_25_A46 end

    def Function_26_A7D(): pass

    label("Function_26_A7D")

    SetChrFlags(0xFE, 0x2)

    label("loc_A82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9C")
    OP_99(0xFE, 0x0, 0x14, 0x7D0)
    Sleep(500)
    Jump("loc_A82")

    label("loc_A9C")

    Return()

    # Function_26_A7D end

    def Function_27_A9D(): pass

    label("Function_27_A9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB7")
    OP_99(0xFE, 0x0, 0xC, 0x7D0)
    Sleep(500)
    Jump("Function_27_A9D")

    label("loc_AB7")

    Return()

    # Function_27_A9D end

    def Function_28_AB8(): pass

    label("Function_28_AB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ACD")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_28_AB8")

    label("loc_ACD")

    Return()

    # Function_28_AB8 end

    def Function_29_ACE(): pass

    label("Function_29_ACE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B04")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_29_ACE")

    label("loc_B04")

    Return()

    # Function_29_ACE end

    def Function_30_B05(): pass

    label("Function_30_B05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1F")
    OP_99(0xFE, 0x0, 0x21, 0x7D0)
    Sleep(500)
    Jump("Function_30_B05")

    label("loc_B1F")

    Return()

    # Function_30_B05 end

    def Function_31_B20(): pass

    label("Function_31_B20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3A")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_31_B20")

    label("loc_B3A")

    Return()

    # Function_31_B20 end

    def Function_32_B3B(): pass

    label("Function_32_B3B")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "はにゃ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_B3B end

    SaveToFile()

Try(main)
