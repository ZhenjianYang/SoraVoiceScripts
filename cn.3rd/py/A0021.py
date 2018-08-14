from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0021   ._SN',
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
        '00100艾丝蒂尔待机',                    # 9
        '00101艾丝蒂尔移动',                    # 10
        '00102艾丝蒂尔攻击',                    # 11
        '00103艾丝蒂尔被弹开',                  # 12
        '00104艾丝蒂尔倒下',                    # 13
        '00105艾丝蒂尔魔法咏唱',                # 14
        '00106艾丝蒂尔魔法发动',                # 15
        '00107艾丝蒂尔胜利',                    # 16
        '00110约修亚待机',                      # 17
        '00111约修亚移动',                      # 18
        '00112约修亚攻击',                      # 19
        '00113约修亚被弹开',                    # 20
        '00114约修亚倒下',                      # 21
        '00115约修亚魔法咏唱',                  # 22
        '00116约修亚魔法发动',                  # 23
        '00117约修亚胜利',                      # 24
        '00170金待机',                          # 25
        '00171金移动',                          # 26
        '00172金攻击',                          # 27
        '00173金被弹开',                        # 28
        '00174金倒下',                          # 29
        '00175金魔法咏唱',                      # 30
        '00176金魔法发动',                      # 31
        '00177金胜利',                          # 32
        '00150阿加特待机',                      # 33
        '00151阿加特移动',                      # 34
        '00152阿加特攻击',                      # 35
        '00153阿加特被弹开',                    # 36
        '00154阿加特倒下',                      # 37
        '00155阿加特魔法咏唱',                  # 38
        '00156阿加特魔法发动',                  # 39
        '00157阿加特胜利',                      # 40
        '00130奥利维尔待机',                    # 41
        '00131奥利维尔移动',                    # 42
        '00132奥利维尔攻击',                    # 43
        '00133奥利维尔被弹开',                  # 44
        '00134奥利维尔倒下',                    # 45
        '00135奥利维尔魔法咏唱',                # 46
        '00136奥利维尔魔法发动',                # 47
        '00137奥利维尔胜利',                    # 48
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
        'ED6_DT27/CH04000 ._CH',             # 00
        'ED6_DT27/CH04001 ._CH',             # 01
        'ED6_DT27/CH04002 ._CH',             # 02
        'ED6_DT27/CH04003 ._CH',             # 03
        'ED6_DT27/CH04004 ._CH',             # 04
        'ED6_DT27/CH04005 ._CH',             # 05
        'ED6_DT27/CH04006 ._CH',             # 06
        'ED6_DT27/CH04007 ._CH',             # 07
        'ED6_DT27/CH04004 ._CH',             # 08
        'ED6_DT27/CH04004 ._CH',             # 09
        'ED6_DT27/CH04004 ._CH',             # 0A
        'ED6_DT27/CH04004 ._CH',             # 0B
        'ED6_DT27/CH04010 ._CH',             # 0C
        'ED6_DT27/CH04011 ._CH',             # 0D
        'ED6_DT27/CH04012 ._CH',             # 0E
        'ED6_DT27/CH04013 ._CH',             # 0F
        'ED6_DT27/CH04014 ._CH',             # 10
        'ED6_DT27/CH04015 ._CH',             # 11
        'ED6_DT27/CH04016 ._CH',             # 12
        'ED6_DT27/CH04017 ._CH',             # 13
        'ED6_DT27/CH04014 ._CH',             # 14
        'ED6_DT27/CH04014 ._CH',             # 15
        'ED6_DT27/CH04014 ._CH',             # 16
        'ED6_DT27/CH04014 ._CH',             # 17
        'ED6_DT07/CH00170 ._CH',             # 18
        'ED6_DT07/CH00171 ._CH',             # 19
        'ED6_DT07/CH00172 ._CH',             # 1A
        'ED6_DT07/CH00173 ._CH',             # 1B
        'ED6_DT07/CH00174 ._CH',             # 1C
        'ED6_DT07/CH00175 ._CH',             # 1D
        'ED6_DT07/CH00176 ._CH',             # 1E
        'ED6_DT07/CH00177 ._CH',             # 1F
        'ED6_DT07/CH00170 ._CH',             # 20
        'ED6_DT07/CH00170 ._CH',             # 21
        'ED6_DT07/CH00170 ._CH',             # 22
        'ED6_DT07/CH00170 ._CH',             # 23
        'ED6_DT07/CH00150 ._CH',             # 24
        'ED6_DT07/CH00151 ._CH',             # 25
        'ED6_DT07/CH00152 ._CH',             # 26
        'ED6_DT07/CH00153 ._CH',             # 27
        'ED6_DT07/CH00154 ._CH',             # 28
        'ED6_DT07/CH00155 ._CH',             # 29
        'ED6_DT07/CH00156 ._CH',             # 2A
        'ED6_DT07/CH00157 ._CH',             # 2B
        'ED6_DT07/CH00150 ._CH',             # 2C
        'ED6_DT07/CH00150 ._CH',             # 2D
        'ED6_DT07/CH00150 ._CH',             # 2E
        'ED6_DT07/CH00150 ._CH',             # 2F
        'ED6_DT07/CH00130 ._CH',             # 30
        'ED6_DT07/CH00131 ._CH',             # 31
        'ED6_DT07/CH00132 ._CH',             # 32
        'ED6_DT07/CH00133 ._CH',             # 33
        'ED6_DT07/CH00134 ._CH',             # 34
        'ED6_DT07/CH00135 ._CH',             # 35
        'ED6_DT07/CH00136 ._CH',             # 36
        'ED6_DT07/CH00137 ._CH',             # 37
        'ED6_DT07/CH00130 ._CH',             # 38
        'ED6_DT07/CH00130 ._CH',             # 39
        'ED6_DT07/CH00130 ._CH',             # 3A
        'ED6_DT07/CH00130 ._CH',             # 3B
    )

    AddCharChipPat(
        'ED6_DT27/CH04000P._CP',             # 00
        'ED6_DT27/CH04001P._CP',             # 01
        'ED6_DT27/CH04002P._CP',             # 02
        'ED6_DT27/CH04003P._CP',             # 03
        'ED6_DT27/CH04004P._CP',             # 04
        'ED6_DT27/CH04005P._CP',             # 05
        'ED6_DT27/CH04006P._CP',             # 06
        'ED6_DT27/CH04007P._CP',             # 07
        'ED6_DT27/CH04000P._CP',             # 08
        'ED6_DT27/CH04000P._CP',             # 09
        'ED6_DT27/CH04000P._CP',             # 0A
        'ED6_DT27/CH04000P._CP',             # 0B
        'ED6_DT27/CH04010P._CP',             # 0C
        'ED6_DT27/CH04011P._CP',             # 0D
        'ED6_DT27/CH04012P._CP',             # 0E
        'ED6_DT27/CH04013P._CP',             # 0F
        'ED6_DT27/CH04014P._CP',             # 10
        'ED6_DT27/CH04015P._CP',             # 11
        'ED6_DT27/CH04016P._CP',             # 12
        'ED6_DT27/CH04017P._CP',             # 13
        'ED6_DT27/CH04010P._CP',             # 14
        'ED6_DT27/CH04010P._CP',             # 15
        'ED6_DT27/CH04010P._CP',             # 16
        'ED6_DT27/CH04010P._CP',             # 17
        'ED6_DT07/CH00170P._CP',             # 18
        'ED6_DT07/CH00171P._CP',             # 19
        'ED6_DT07/CH00172P._CP',             # 1A
        'ED6_DT07/CH00173P._CP',             # 1B
        'ED6_DT07/CH00174P._CP',             # 1C
        'ED6_DT07/CH00175P._CP',             # 1D
        'ED6_DT07/CH00176P._CP',             # 1E
        'ED6_DT07/CH00177P._CP',             # 1F
        'ED6_DT07/CH00170P._CP',             # 20
        'ED6_DT07/CH00170P._CP',             # 21
        'ED6_DT07/CH00170P._CP',             # 22
        'ED6_DT07/CH00170P._CP',             # 23
        'ED6_DT07/CH00150P._CP',             # 24
        'ED6_DT07/CH00151P._CP',             # 25
        'ED6_DT07/CH00152P._CP',             # 26
        'ED6_DT07/CH00153P._CP',             # 27
        'ED6_DT07/CH00154P._CP',             # 28
        'ED6_DT07/CH00155P._CP',             # 29
        'ED6_DT07/CH00156P._CP',             # 2A
        'ED6_DT07/CH00157P._CP',             # 2B
        'ED6_DT07/CH00150P._CP',             # 2C
        'ED6_DT07/CH00150P._CP',             # 2D
        'ED6_DT07/CH00150P._CP',             # 2E
        'ED6_DT07/CH00150P._CP',             # 2F
        'ED6_DT07/CH00130P._CP',             # 30
        'ED6_DT07/CH00131P._CP',             # 31
        'ED6_DT07/CH00132P._CP',             # 32
        'ED6_DT07/CH00133P._CP',             # 33
        'ED6_DT07/CH00134P._CP',             # 34
        'ED6_DT07/CH00135P._CP',             # 35
        'ED6_DT07/CH00136P._CP',             # 36
        'ED6_DT07/CH00137P._CP',             # 37
        'ED6_DT07/CH00130P._CP',             # 38
        'ED6_DT07/CH00130P._CP',             # 39
        'ED6_DT07/CH00130P._CP',             # 3A
        'ED6_DT07/CH00130P._CP',             # 3B
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 16,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 17,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 19,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 21,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 22,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 23,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 24,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 25,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 26,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        InitScenaIndex      = 27,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
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
        "Function_8_82D",          # 08, 8
        "Function_9_90A",          # 09, 9
        "Function_10_920",         # 0A, 10
        "Function_11_957",         # 0B, 11
        "Function_12_977",         # 0C, 12
        "Function_13_992",         # 0D, 13
        "Function_14_9A8",         # 0E, 14
        "Function_15_9DF",         # 0F, 15
        "Function_16_9FF",         # 10, 16
        "Function_17_A1A",         # 11, 17
        "Function_18_A30",         # 12, 18
        "Function_19_A67",         # 13, 19
        "Function_20_A82",         # 14, 20
        "Function_21_A9D",         # 15, 21
        "Function_22_AB3",         # 16, 22
        "Function_23_AEA",         # 17, 23
        "Function_24_B05",         # 18, 24
        "Function_25_B20",         # 19, 25
        "Function_26_B36",         # 1A, 26
        "Function_27_B6D",         # 1B, 27
        "Function_28_B88",         # 1C, 28
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
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_6_7EE")

    label("loc_808")

    Return()

    # Function_6_7EE end

    def Function_7_809(): pass

    label("Function_7_809")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_82C")
    OP_8D(0xFE, 4000, 20000, 24000, 28000, 1500)
    Jump("Function_7_809")

    label("loc_82C")

    Return()

    # Function_7_809 end

    def Function_8_82D(): pass

    label("Function_8_82D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_909")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(90)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(40)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(70)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Jump("Function_8_82D")

    label("loc_909")

    Return()

    # Function_8_82D end

    def Function_9_90A(): pass

    label("Function_9_90A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91F")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_9_90A")

    label("loc_91F")

    Return()

    # Function_9_90A end

    def Function_10_920(): pass

    label("Function_10_920")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_956")
    SetChrChipByIndex(0xFE, 5)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_10_920")

    label("loc_956")

    Return()

    # Function_10_920 end

    def Function_11_957(): pass

    label("Function_11_957")

    SetChrFlags(0xFE, 0x2)

    label("loc_95C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_976")
    OP_99(0xFE, 0x0, 0x13, 0x7D0)
    Sleep(500)
    Jump("loc_95C")

    label("loc_976")

    Return()

    # Function_11_957 end

    def Function_12_977(): pass

    label("Function_12_977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_991")
    OP_99(0xFE, 0x0, 0xC, 0x7D0)
    Sleep(500)
    Jump("Function_12_977")

    label("loc_991")

    Return()

    # Function_12_977 end

    def Function_13_992(): pass

    label("Function_13_992")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A7")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_13_992")

    label("loc_9A7")

    Return()

    # Function_13_992 end

    def Function_14_9A8(): pass

    label("Function_14_9A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DE")
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 18)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_14_9A8")

    label("loc_9DE")

    Return()

    # Function_14_9A8 end

    def Function_15_9DF(): pass

    label("Function_15_9DF")

    SetChrFlags(0xFE, 0x2)

    label("loc_9E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9FE")
    OP_99(0xFE, 0x0, 0x21, 0x7D0)
    Sleep(500)
    Jump("loc_9E4")

    label("loc_9FE")

    Return()

    # Function_15_9DF end

    def Function_16_9FF(): pass

    label("Function_16_9FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A19")
    OP_99(0xFE, 0x0, 0x7, 0x9C4)
    Sleep(500)
    Jump("Function_16_9FF")

    label("loc_A19")

    Return()

    # Function_16_9FF end

    def Function_17_A1A(): pass

    label("Function_17_A1A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A2F")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_17_A1A")

    label("loc_A2F")

    Return()

    # Function_17_A1A end

    def Function_18_A30(): pass

    label("Function_18_A30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A66")
    SetChrChipByIndex(0xFE, 29)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 30)
    OP_99(0xFE, 0x0, 0x0, 0x3E8)
    Sleep(1000)
    Jump("Function_18_A30")

    label("loc_A66")

    Return()

    # Function_18_A30 end

    def Function_19_A67(): pass

    label("Function_19_A67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A81")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_19_A67")

    label("loc_A81")

    Return()

    # Function_19_A67 end

    def Function_20_A82(): pass

    label("Function_20_A82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9C")
    OP_99(0xFE, 0x0, 0x7, 0x9C4)
    Sleep(500)
    Jump("Function_20_A82")

    label("loc_A9C")

    Return()

    # Function_20_A82 end

    def Function_21_A9D(): pass

    label("Function_21_A9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB2")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_21_A9D")

    label("loc_AB2")

    Return()

    # Function_21_A9D end

    def Function_22_AB3(): pass

    label("Function_22_AB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE9")
    SetChrChipByIndex(0xFE, 41)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 42)
    OP_99(0xFE, 0x0, 0x0, 0x3E8)
    Sleep(1000)
    Jump("Function_22_AB3")

    label("loc_AE9")

    Return()

    # Function_22_AB3 end

    def Function_23_AEA(): pass

    label("Function_23_AEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B04")
    OP_99(0xFE, 0x0, 0xA, 0x7D0)
    Sleep(500)
    Jump("Function_23_AEA")

    label("loc_B04")

    Return()

    # Function_23_AEA end

    def Function_24_B05(): pass

    label("Function_24_B05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1F")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Sleep(500)
    Jump("Function_24_B05")

    label("loc_B1F")

    Return()

    # Function_24_B05 end

    def Function_25_B20(): pass

    label("Function_25_B20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B35")
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    Jump("Function_25_B20")

    label("loc_B35")

    Return()

    # Function_25_B20 end

    def Function_26_B36(): pass

    label("Function_26_B36")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6C")
    SetChrChipByIndex(0xFE, 53)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    OP_99(0xFE, 0x0, 0x3, 0x4B0)
    SetChrChipByIndex(0xFE, 54)
    OP_99(0xFE, 0x0, 0x1, 0x4B0)
    Sleep(1000)
    Jump("Function_26_B36")

    label("loc_B6C")

    Return()

    # Function_26_B36 end

    def Function_27_B6D(): pass

    label("Function_27_B6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B87")
    OP_99(0xFE, 0x0, 0xE, 0x7D0)
    Sleep(500)
    Jump("Function_27_B6D")

    label("loc_B87")

    Return()

    # Function_27_B6D end

    def Function_28_B88(): pass

    label("Function_28_B88")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "你好。\x02",
    )

    Jump("loc_BA1")

    label("loc_BA1")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_B88 end

    SaveToFile()

Try(main)
