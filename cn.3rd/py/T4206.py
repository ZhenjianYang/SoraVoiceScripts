from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4206   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4206.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '凯文神父',                             # 9
        '艾丝蒂尔',                             # 10
        '约修亚',                               # 11
        '雪拉扎德',                             # 12
        '奥利维尔',                             # 13
        '科洛蒂娅公主',                         # 14
        '阿加特',                               # 15
        '提妲',                                 # 16
        '金',                                   # 17
        '亚妮拉丝',                             # 18
        '乔丝特',                               # 19
        '尤莉亚上尉',                           # 20
        '穆拉少校',                             # 21
        '理查德',                               # 22
        '希德中校',                             # 23
        '凯诺娜',                               # 24
        '克劳斯市长',                           # 25
        '梅贝尔市长',                           # 26
        '科林兹校长',                           # 27
        '玛多克工房长',                         # 28
        '莉拉',                                 # 29
        '艾莉茜雅女王',                         # 30
        '杜南公爵',                             # 31
        '达维尔大使',                           # 32
        '管家菲利普',                           # 33
        '希尔丹夫人',                           # 34
        '基库',                                 # 35
        '爱尔莎大使',                           # 36
        '艾南',                                 # 37
        '克鲁茨',                               # 38
        '库拉茨',                               # 39
        '卡露娜',                               # 40
        '摩尔根将军',                           # 41
        '卡西乌斯',                             # 42
        '多伦',                                 # 43
        '吉尔',                                 # 44
        '拉赛尔博士',                           # 45
        '奈尔',                                 # 46
        '朵洛希',                               # 47
        '吉尔维厨师长',                         # 48
        '福卢克',                               # 49
        '里吉斯',                               # 50
        '桑吉特',                               # 51
        '茜亚',                                 # 52
        '索蕾拉',                               # 53
        '妮舒',                                 # 54
        '潘娜',                                 # 55
        '布莉姆',                               # 56
        '艾科尔',                               # 57
        '亲卫队员',                             # 58
        '亲卫队员',                             # 59
        '亲卫队员',                             # 60
        '亲卫队员',                             # 61
        '诺曼市长',                             # 62
        '酒杯',                                 # 63
        '目标用照相机',                         # 64
        '',                                     # 65
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03000 ._CH',             # 01
        'ED6_DT27/CH03200 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT27/CH03960 ._CH',             # 05
        'ED6_DT07/CH00050 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
        'ED6_DT07/CH00070 ._CH',             # 08
        'ED6_DT07/CH01630 ._CH',             # 09
        'ED6_DT27/CH03270 ._CH',             # 0A
        'ED6_DT07/CH02090 ._CH',             # 0B
        'ED6_DT27/CH03570 ._CH',             # 0C
        'ED6_DT07/CH02030 ._CH',             # 0D
        'ED6_DT27/CH03590 ._CH',             # 0E
        'ED6_DT07/CH02100 ._CH',             # 0F
        'ED6_DT07/CH02350 ._CH',             # 10
        'ED6_DT07/CH02360 ._CH',             # 11
        'ED6_DT07/CH02600 ._CH',             # 12
        'ED6_DT07/CH02620 ._CH',             # 13
        'ED6_DT07/CH02370 ._CH',             # 14
        'ED6_DT07/CH02010 ._CH',             # 15
        'ED6_DT07/CH02140 ._CH',             # 16
        'ED6_DT27/CH03710 ._CH',             # 17
        'ED6_DT07/CH02470 ._CH',             # 18
        'ED6_DT07/CH02460 ._CH',             # 19
        'ED6_DT07/CH02323 ._CH',             # 1A
        'ED6_DT27/CH03720 ._CH',             # 1B
        'ED6_DT07/CH02610 ._CH',             # 1C
        'ED6_DT07/CH02560 ._CH',             # 1D
        'ED6_DT07/CH02380 ._CH',             # 1E
        'ED6_DT07/CH02400 ._CH',             # 1F
        'ED6_DT07/CH02580 ._CH',             # 20
        'ED6_DT07/CH01620 ._CH',             # 21
        'ED6_DT07/CH01260 ._CH',             # 22
        'ED6_DT07/CH01240 ._CH',             # 23
        'ED6_DT07/CH02080 ._CH',             # 24
        'ED6_DT27/CH03670 ._CH',             # 25
        'ED6_DT07/CH02110 ._CH',             # 26
        'ED6_DT07/CH02120 ._CH',             # 27
        'ED6_DT07/CH02020 ._CH',             # 28
        'ED6_DT07/CH02440 ._CH',             # 29
        'ED6_DT07/CH02060 ._CH',             # 2A
        'ED6_DT06/CH20063 ._CH',             # 2B
        'ED6_DT07/CH01280 ._CH',             # 2C
        'ED6_DT07/CH01520 ._CH',             # 2D
        'ED6_DT07/CH01350 ._CH',             # 2E
        'ED6_DT07/CH02540 ._CH',             # 2F
        'ED6_DT07/CH01320 ._CH',             # 30
        'ED6_DT06/CH20127 ._CH',             # 31
        'ED6_DT06/CH20064 ._CH',             # 32
        'ED6_DT07/CH01200 ._CH',             # 33
        'ED6_DT06/CH20021 ._CH',             # 34
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03000P._CP',             # 01
        'ED6_DT27/CH03200P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT27/CH03960P._CP',             # 05
        'ED6_DT07/CH00050P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
        'ED6_DT07/CH00070P._CP',             # 08
        'ED6_DT07/CH01630P._CP',             # 09
        'ED6_DT27/CH03270P._CP',             # 0A
        'ED6_DT07/CH02090P._CP',             # 0B
        'ED6_DT27/CH03570P._CP',             # 0C
        'ED6_DT07/CH02030P._CP',             # 0D
        'ED6_DT27/CH03590P._CP',             # 0E
        'ED6_DT07/CH02100P._CP',             # 0F
        'ED6_DT07/CH02350P._CP',             # 10
        'ED6_DT07/CH02360P._CP',             # 11
        'ED6_DT07/CH02600P._CP',             # 12
        'ED6_DT07/CH02620P._CP',             # 13
        'ED6_DT07/CH02370P._CP',             # 14
        'ED6_DT07/CH02010P._CP',             # 15
        'ED6_DT07/CH02140P._CP',             # 16
        'ED6_DT27/CH03710P._CP',             # 17
        'ED6_DT07/CH02470P._CP',             # 18
        'ED6_DT07/CH02460P._CP',             # 19
        'ED6_DT07/CH02323P._CP',             # 1A
        'ED6_DT27/CH03720P._CP',             # 1B
        'ED6_DT07/CH02610P._CP',             # 1C
        'ED6_DT07/CH02560P._CP',             # 1D
        'ED6_DT07/CH02380P._CP',             # 1E
        'ED6_DT07/CH02400P._CP',             # 1F
        'ED6_DT07/CH02580P._CP',             # 20
        'ED6_DT07/CH01620P._CP',             # 21
        'ED6_DT07/CH01260P._CP',             # 22
        'ED6_DT07/CH01240P._CP',             # 23
        'ED6_DT07/CH02080P._CP',             # 24
        'ED6_DT27/CH03670P._CP',             # 25
        'ED6_DT07/CH02110P._CP',             # 26
        'ED6_DT07/CH02120P._CP',             # 27
        'ED6_DT07/CH02020P._CP',             # 28
        'ED6_DT07/CH02440P._CP',             # 29
        'ED6_DT07/CH02060P._CP',             # 2A
        'ED6_DT06/CH20063P._CP',             # 2B
        'ED6_DT07/CH01280P._CP',             # 2C
        'ED6_DT07/CH01520P._CP',             # 2D
        'ED6_DT07/CH01350P._CP',             # 2E
        'ED6_DT07/CH02540P._CP',             # 2F
        'ED6_DT07/CH01320P._CP',             # 30
        'ED6_DT06/CH20127P._CP',             # 31
        'ED6_DT06/CH20064P._CP',             # 32
        'ED6_DT07/CH01200P._CP',             # 33
        'ED6_DT06/CH20021P._CP',             # 34
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkScenaIndex      = 29,
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
        TalkScenaIndex      = 30,
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
        TalkScenaIndex      = 45,
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
        TalkScenaIndex      = 27,
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
        TalkScenaIndex      = 26,
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
        TalkScenaIndex      = 35,
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
        TalkScenaIndex      = 66,
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
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 71,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 60,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 72,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 69,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 70,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 73,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 67,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 62,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 63,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 64,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 65,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 61,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 74,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 75,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 76,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 77,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 78,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 79,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 80,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 81,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 82,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 83,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 84,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 85,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 86,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 87,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 59,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327732,
        ChipIndex           = 0x34,
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


    DeclEvent(
        X                   = -3700,
        Y                   = 10000,
        Z                   = 83810,
        Range               = 4050,
        Unknown_10          = 0x4E20,
        Unknown_14          = 0x127C8,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    DeclActor(
        TriggerX            = 12130,
        TriggerZ            = 12000,
        TriggerY            = 53740,
        TriggerRange        = 1000,
        ActorX              = 12130,
        ActorZ              = 14000,
        ActorY              = 53740,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 73,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_996",          # 00, 0
        "Function_1_9E9",          # 01, 1
        "Function_2_CAC",          # 02, 2
        "Function_3_E29",          # 03, 3
        "Function_4_F66",          # 04, 4
        "Function_5_108D",         # 05, 5
        "Function_6_11AD",         # 06, 6
        "Function_7_12AB",         # 07, 7
        "Function_8_12E8",         # 08, 8
        "Function_9_1451",         # 09, 9
        "Function_10_1959",        # 0A, 10
        "Function_11_1E2F",        # 0B, 11
        "Function_12_1FB8",        # 0C, 12
        "Function_13_2005",        # 0D, 13
        "Function_14_204E",        # 0E, 14
        "Function_15_2091",        # 0F, 15
        "Function_16_2266",        # 10, 16
        "Function_17_2552",        # 11, 17
        "Function_18_418D",        # 12, 18
        "Function_19_41D5",        # 13, 19
        "Function_20_4216",        # 14, 20
        "Function_21_8DEA",        # 15, 21
        "Function_22_8E2C",        # 16, 22
        "Function_23_8E6E",        # 17, 23
        "Function_24_8E97",        # 18, 24
        "Function_25_8EC0",        # 19, 25
        "Function_26_939C",        # 1A, 26
        "Function_27_9435",        # 1B, 27
        "Function_28_9563",        # 1C, 28
        "Function_29_9B48",        # 1D, 29
        "Function_30_9C88",        # 1E, 30
        "Function_31_9E52",        # 1F, 31
        "Function_32_A16C",        # 20, 32
        "Function_33_A1D0",        # 21, 33
        "Function_34_A23B",        # 22, 34
        "Function_35_A457",        # 23, 35
        "Function_36_A532",        # 24, 36
        "Function_37_A8B2",        # 25, 37
        "Function_38_A954",        # 26, 38
        "Function_39_AA3B",        # 27, 39
        "Function_40_AD58",        # 28, 40
        "Function_41_AE04",        # 29, 41
        "Function_42_AEB5",        # 2A, 42
        "Function_43_B280",        # 2B, 43
        "Function_44_B2EF",        # 2C, 44
        "Function_45_B456",        # 2D, 45
        "Function_46_B4C9",        # 2E, 46
        "Function_47_B8C3",        # 2F, 47
        "Function_48_B937",        # 30, 48
        "Function_49_BDF5",        # 31, 49
        "Function_50_BE93",        # 32, 50
        "Function_51_BF5E",        # 33, 51
        "Function_52_C1A3",        # 34, 52
        "Function_53_C40D",        # 35, 53
        "Function_54_C640",        # 36, 54
        "Function_55_C736",        # 37, 55
        "Function_56_C79F",        # 38, 56
        "Function_57_C811",        # 39, 57
        "Function_58_CA23",        # 3A, 58
        "Function_59_CBAE",        # 3B, 59
        "Function_60_CCEA",        # 3C, 60
        "Function_61_CF50",        # 3D, 61
        "Function_62_D077",        # 3E, 62
        "Function_63_D242",        # 3F, 63
        "Function_64_D689",        # 40, 64
        "Function_65_D764",        # 41, 65
        "Function_66_D7CF",        # 42, 66
        "Function_67_D9D7",        # 43, 67
        "Function_68_DB6C",        # 44, 68
        "Function_69_DE01",        # 45, 69
        "Function_70_DE56",        # 46, 70
        "Function_71_DEFE",        # 47, 71
        "Function_72_E1C1",        # 48, 72
        "Function_73_E316",        # 49, 73
        "Function_74_E3EC",        # 4A, 74
        "Function_75_E441",        # 4B, 75
        "Function_76_E494",        # 4C, 76
        "Function_77_E4DC",        # 4D, 77
        "Function_78_E5E3",        # 4E, 78
        "Function_79_E722",        # 4F, 79
        "Function_80_E828",        # 50, 80
        "Function_81_E902",        # 51, 81
        "Function_82_E958",        # 52, 82
        "Function_83_EA23",        # 53, 83
        "Function_84_EA7C",        # 54, 84
        "Function_85_EAE5",        # 55, 85
        "Function_86_EB44",        # 56, 86
        "Function_87_EB70",        # 57, 87
    )


    def Function_0_996(): pass

    label("Function_0_996")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_9C1")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_9DD")

    label("loc_9C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_9DD")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_9DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 2)), scpexpr(EXPR_END)), "loc_9E8")
    Call(0, 9)

    label("loc_9E8")

    Return()

    # Function_0_996 end

    def Function_1_9E9(): pass

    label("Function_1_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 2)), scpexpr(EXPR_END)), "loc_9F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F9")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_A4E")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_A4E")

    OP_51(0x102, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x30, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x31, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x32, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x33, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x35, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x39, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x40, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x41, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x42, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x43, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x44, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x45, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_9E9 end

    def Function_2_CAC(): pass

    label("Function_2_CAC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E13")

    label("loc_CD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E13")

    label("loc_CEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D03")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E13")

    label("loc_D03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E13")

    label("loc_D1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E13")

    label("loc_D35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E13")

    label("loc_D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E13")

    label("loc_D67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D80")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E13")

    label("loc_D80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D99")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E13")

    label("loc_D99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E13")

    label("loc_DB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E13")

    label("loc_DCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E13")

    label("loc_DE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFD")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E13")

    label("loc_DFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E13")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E28")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E13")

    label("loc_E28")

    Return()

    # Function_2_CAC end

    def Function_3_E29(): pass

    label("Function_3_E29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F65")
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFB776, 0x36B0, 0x1228C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC964, 0x36B0, 0x1214C, 0x7D0, 0x0)
    Sleep(2000)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFC93C, 0x36B0, 0x12B2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x36B0, 0x12D0E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE124, 0x36B0, 0x13696, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFE124, 0x36B0, 0x13696, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE0C0, 0x36B0, 0x12D0E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC93C, 0x36B0, 0x12B2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC964, 0x36B0, 0x1214C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFB776, 0x36B0, 0x1228C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB7BC, 0x36B0, 0x11A3A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Jump("Function_3_E29")

    label("loc_F65")

    Return()

    # Function_3_E29 end

    def Function_4_F66(): pass

    label("Function_4_F66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_108C")
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0x2EA4, 0x36B0, 0x11954, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2E72, 0x36B0, 0x13042, 0x7D0, 0x0)
    Sleep(2500)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x44FC, 0x36B0, 0x12EA8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x639C, 0x2EE0, 0x14BF4, 0x7D0, 0x0)
    Sleep(3000)
    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8E(0xFE, 0x4B14, 0x36B0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4B5A, 0x36B0, 0x11B20, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0x4AA6, 0x36B0, 0x10C8E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x39DA, 0x36B0, 0x10AFE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3386, 0x36B0, 0x11058, 0x7D0, 0x0)
    OP_8E(0xFE, 0x33A4, 0x36B0, 0x11990, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    Jump("Function_4_F66")

    label("loc_108C")

    Return()

    # Function_4_F66 end

    def Function_5_108D(): pass

    label("Function_5_108D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11AC")
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFF1A0, 0x2EE0, 0xD4E4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE908, 0x2EE0, 0xCBCA, 0x7D0, 0x0)
    Sleep(3000)
    OP_8C(0xFE, 90, 400)
    Sleep(300)
    OP_8E(0xFE, 0xB9A, 0x2EE0, 0xCB70, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x1090, 0x2EE0, 0xC8AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x17DE, 0x2EE0, 0xC256, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(3000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFFA9C, 0x2EE0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFBF0, 0x2EE0, 0xD430, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(2000)
    Jump("Function_5_108D")

    label("loc_11AC")

    Return()

    # Function_5_108D end

    def Function_6_11AD(): pass

    label("Function_6_11AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12AA")
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0x5BE, 0x2EE0, 0xF7F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x28, 0x2EE0, 0xF85C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE8D6, 0x2EE0, 0xFBA4, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(2500)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE872, 0x2EE0, 0xF190, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(3500)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFE890, 0x2EE0, 0xF8D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3FC, 0x2EE0, 0xF636, 0x7D0, 0x0)
    OP_8E(0xFE, 0x456, 0x2EE0, 0xE9FC, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2500)
    Jump("Function_6_11AD")

    label("loc_12AA")

    Return()

    # Function_6_11AD end

    def Function_7_12AB(): pass

    label("Function_7_12AB")

    OP_8E(0xFE, 0x1B30, 0x36B0, 0x13BB4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1EA, 0x33C2, 0x122DC, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFE480, 0x2EE0, 0xF21C, 0xFA0, 0x0)
    Return()

    # Function_7_12AB end

    def Function_8_12E8(): pass

    label("Function_8_12E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1450")
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(600)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(100)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(100, 16777215, 50)
    PlayEffect(0x0, 0xFF, 0x36, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    FadeToBright(100, 16777215)
    Sleep(800)
    Jump("Function_8_12E8")

    label("loc_1450")

    Return()

    # Function_8_12E8 end

    def Function_9_1451(): pass

    label("Function_9_1451")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x25, 11100, 12000, 55420, 270)
    SetChrPos(0x15, 11100, 12000, 57370, 90)
    SetChrPos(0x2A, 12190, 13600, 53700, 270)
    SetChrPos(0x31, -43010, 16000, 80590, 270)
    SetChrPos(0x30, -15740, 14000, 71720, 270)
    SetChrPos(0x1E, -12600, 14000, 75360, 180)
    SetChrPos(0x1D, 28180, 12000, 86160, 270)
    SetChrPos(0x1F, 31990, 12000, 90520, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160D")
    SetChrPos(0x11, 10730, 14000, 80650, 270)
    Jump("loc_161E")

    label("loc_160D")

    SetChrPos(0x11, -8100, 12000, 58540, 180)

    label("loc_161E")

    SetChrPos(0x10, 1640, 12000, 64860, 270)
    SetChrPos(0x13, -24430, 12000, 86170, 270)
    SetChrPos(0x14, -25960, 12000, 87460, 180)
    SetChrPos(0x20, -11680, 14000, 77850, 0)
    SetChrPos(0x22, -9630, 14000, 81250, 270)
    SetChrPos(0x23, -9930, 14000, 77850, 0)
    SetChrPos(0x21, -11540, 14000, 81250, 90)
    SetChrPos(0x24, -12720, 14000, 81970, 90)
    SetChrPos(0x45, -13460, 14000, 79230, 90)
    SetChrPos(0x46, -25100, 12540, 86150, 0)
    OP_51(0x46, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x18, 8580, 12000, 65660, 270)
    SetChrPos(0x2B, 7080, 12000, 66950, 180)
    SetChrPos(0x2C, -4950, 12000, 54140, 45)
    SetChrPos(0x19, -5220, 12000, 57140, 270)
    SetChrPos(0x2D, -3420, 12000, 55740, 225)
    SetChrPos(0x2E, -5950, 12000, 59520, 225)
    SetChrPos(0x2F, -6530, 12000, 60440, 225)
    SetChrPos(0x32, -7010, 12000, 66950, 180)
    SetChrPos(0x33, -5490, 12000, 65800, 270)
    SetChrPos(0x1A, -8100, 12000, 57040, 0)
    SetChrPos(0x16, 15630, 14000, 70450, 0)
    SetChrPos(0x17, 15640, 14000, 71750, 180)
    SetChrPos(0x34, 18430, 14000, 70910, 270)
    SetChrPos(0x26, 6410, 12000, 56280, 180)
    SetChrPos(0x27, 6320, 12000, 54850, 0)
    SetChrPos(0x28, 5680, 12000, 57010, 180)
    SetChrPos(0x1B, 7900, 12000, 52560, 270)
    SetChrPos(0x1C, 6050, 12000, 52380, 90)
    SetChrPos(0x29, 13170, 12000, 60300, 270)
    SetChrPos(0x3B, 14190, 12000, 59700, 270)
    SetChrPos(0x3C, 14190, 12000, 58700, 270)
    SetChrPos(0x3D, -1040, 12000, 54320, 90)
    SetChrPos(0x3E, 1110, 12000, 59900, 270)
    SetChrPos(0x3F, 13220, 14000, 72080, 0)
    SetChrPos(0x40, -18500, 14000, 72250, 90)
    OP_43(0x3D, 0x0, 0x0, 0x5)
    OP_43(0x3E, 0x0, 0x0, 0x6)
    OP_43(0x3F, 0x0, 0x0, 0x4)
    OP_43(0x40, 0x0, 0x0, 0x3)
    SetChrPos(0x35, 12210, 12000, 57070, 270)
    SetChrPos(0x36, 6500, 12000, 60670, 270)
    SetChrPos(0x37, -9900, 12000, 53370, 90)
    SetChrPos(0x38, -12590, 14000, 73030, 0)
    SetChrPos(0x39, -8189, 12000, 60260, 180)
    SetChrPos(0x3A, -140, 12000, 58190, 0)
    SetChrPos(0x41, 3100, 14000, 82400, 180)
    SetChrPos(0x42, -3100, 14000, 82400, 180)
    SetChrPos(0x43, 2900, 18000, 102900, 180)
    SetChrPos(0x44, -2900, 18000, 102900, 180)
    Return()

    # Function_9_1451 end

    def Function_10_1959(): pass

    label("Function_10_1959")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x25, 11100, 12000, 57370, 270)
    SetChrPos(0x15, 11100, 12000, 55420, 270)
    SetChrPos(0x2A, 12190, 13600, 53700, 270)
    SetChrPos(0x31, -15750, 14000, 70680, 270)
    SetChrPos(0x30, -15740, 14000, 72330, 270)
    SetChrPos(0x1E, -18510, 14000, 71980, 90)
    SetChrPos(0x1D, 28180, 12000, 86160, 270)
    SetChrPos(0x1F, 31990, 12000, 90520, 225)
    SetChrPos(0x11, 10730, 14000, 80650, 270)
    SetChrPos(0x10, -8560, 12000, 50990, 72)
    SetChrPos(0x13, 5400, 12000, 65540, 90)
    SetChrPos(0x14, 3300, 12000, 55670, 90)
    SetChrPos(0x18, 6930, 12000, 66970, 180)
    SetChrPos(0x20, -11680, 14000, 77850, 0)
    SetChrPos(0x22, -9600, 14000, 80610, 180)
    SetChrPos(0x23, -9930, 14000, 77850, 0)
    SetChrPos(0x21, -11440, 14000, 80600, 180)
    SetChrPos(0x24, -12300, 14000, 81520, 180)
    SetChrPos(0x45, -13460, 14000, 79230, 90)
    SetChrPos(0x46, -25080, 12540, 86200, 0)
    OP_51(0x46, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x488), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x488), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x46, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x488), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x2B, 4960, 12000, 59240, 0)
    SetChrPos(0x2C, -4950, 12000, 54140, 0)
    SetChrPos(0x19, -3410, 12000, 60630, 271)
    SetChrPos(0x2D, -4900, 12000, 59240, 347)
    SetChrPos(0x2E, -6590, 12000, 60600, 83)
    SetChrPos(0x2F, -4990, 12000, 62170, 180)
    SetChrPos(0x32, -7010, 12000, 66950, 180)
    SetChrPos(0x33, -5490, 12000, 65800, 270)
    SetChrPos(0x1A, -6910, 12000, 64040, 0)
    SetChrPos(0x16, 8460, 12000, 65500, 270)
    SetChrPos(0x17, 15650, 14000, 72520, 90)
    SetChrPos(0x34, 18400, 14000, 72340, 270)
    SetChrPos(0x26, 6410, 12000, 56280, 180)
    SetChrPos(0x27, 5060, 12000, 54150, 0)
    SetChrPos(0x28, 5680, 12000, 57010, 180)
    SetChrPos(0x1B, 7900, 12000, 52560, 270)
    SetChrPos(0x1C, 4980, 12000, 57050, 180)
    SetChrPos(0x3B, 4500, 12000, 69580, 270)
    SetChrPos(0x3C, 4500, 12000, 68580, 270)
    SetChrPos(0x3D, 4550, 12000, 67550, 270)
    SetChrPos(0x3E, 5740, 12000, 69730, 270)
    SetChrPos(0x3F, 5690, 12000, 68690, 270)
    SetChrPos(0x40, 5640, 12000, 67650, 270)
    OP_43(0x3D, 0x0, 0x0, 0x2)
    OP_43(0x3E, 0x0, 0x0, 0x2)
    OP_43(0x3F, 0x0, 0x0, 0x2)
    OP_43(0x40, 0x0, 0x0, 0x2)
    SetChrPos(0x35, -5470, 14000, 76850, 45)
    SetChrPos(0x36, -4230, 14000, 76860, 45)
    SetChrPos(0x37, -4780, 12000, 69830, 90)
    SetChrPos(0x38, -4780, 12000, 68730, 90)
    SetChrPos(0x39, -6010, 12000, 69770, 90)
    SetChrPos(0x3A, -6010, 12000, 68730, 90)
    SetChrPos(0x41, 2900, 18000, 102900, 180)
    SetChrPos(0x42, -2900, 18000, 102900, 180)
    SetChrPos(0x43, 3100, 14000, 82400, 180)
    SetChrPos(0x44, -3100, 14000, 82400, 180)
    Return()

    # Function_10_1959 end

    def Function_11_1E2F(): pass

    label("Function_11_1E2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FB7")
    PlayEffect(0x0, 0x0, 0xFF, 50930, 45000, 99710, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(1500)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x1, 0xFF, 60300, 35000, 90770, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(3000)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 48640, 37000, 115840, 0, 0, 0, 3500, 2000, 3500, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(1500)
    OP_82(0x2, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 55640, 42000, 100840, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(2500)
    OP_82(0x2, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 50640, 40000, 115840, 0, 0, 0, 2500, 4500, 2500, 0xFF, 0, 0, 0, 0)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0x19B, 0x0, 0x64)
    OP_22(0x1D7, 0x0, 0x64)
    Sleep(3000)
    OP_82(0x2, 0x2)
    Jump("Function_11_1E2F")

    label("loc_1FB7")

    Return()

    # Function_11_1E2F end

    def Function_12_1FB8(): pass

    label("Function_12_1FB8")

    OP_8C(0xFE, 225, 400)
    Sleep(300)
    OP_8E(0xFE, 0x9682, 0x3E80, 0x1333A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x712A, 0x36B0, 0x10DF6, 0x7D0, 0x0)
    SetChrPos(0xFE, 11100, 12000, 57370, 270)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_12_1FB8 end

    def Function_13_2005(): pass

    label("Function_13_2005")

    OP_8C(0xFE, 45, 400)
    Sleep(300)
    OP_8E(0xFE, 0x2E72, 0x2EE0, 0xE33A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2DAA, 0x2EE0, 0xEB28, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1144, 0x2EE0, 0xFC39, 0x7D0, 0x0)
    Return()

    # Function_13_2005 end

    def Function_14_204E(): pass

    label("Function_14_204E")


    def lambda_2054():

        label("loc_2054")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_2054")

    QueueWorkItem2(0xFE, 3, lambda_2054)
    Sleep(2500)
    OP_44(0xFE, 0x3)
    OP_8E(0xFE, 0x2B2A, 0x2EE0, 0xE614, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1144, 0x2EE0, 0xFC39, 0x7D0, 0x0)
    Return()

    # Function_14_204E end

    def Function_15_2091(): pass

    label("Function_15_2091")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2265")
    OP_22(0x183, 0x0, 0x64)
    PlayEffect(0x3, 0x0, 0xFF, 0, -12000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x1, 0xFF, 9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x2, 0xFF, -11000, -13000, -1560, 45, 50, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1500)
    PlayEffect(0x7, 0x3, 0xFF, 7000, -20000, -2560, 0, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x7, 0x4, 0xFF, -6000, -21000, -2560, 0, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x5, 0xFF, -9000, -10000, -1560, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x167, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x0, 0xFF, 11000, -16000, -1560, -45, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x182, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x183, 0x0, 0x64)
    Sleep(1000)
    Jump("Function_15_2091")

    label("loc_2265")

    Return()

    # Function_15_2091 end

    def Function_16_2266(): pass

    label("Function_16_2266")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    LoadEffect(0x0, "map\\mp288_00.eff")
    LoadEffect(0x1, "map\\mp288_01.eff")
    LoadEffect(0x2, "map\\mp288_02.eff")
    LoadEffect(0x3, "map\\mp288_04.eff")
    LoadEffect(0x4, "map\\mp289_00.eff")
    LoadEffect(0x5, "map\\mp289_01.eff")
    LoadEffect(0x6, "map\\mp290_00.eff")
    LoadEffect(0x7, "map\\mp293_00.eff")
    OP_4A(0x11, 255)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x102, 40040, 16000, 78780, 315)
    SetChrPos(0x11, 39300, 16000, 78000, 315)
    OP_6D(39860, 18000, 79820, 0)
    OP_67(0, 8320, -10000, 0)
    OP_6B(1920, 0)
    OP_6C(5000, 0)
    OP_6E(381, 0)
    OP_43(0x102, 0x3, 0x0, 0xF)

    def lambda_2389():
        OP_6D(39860, 16000, 79820, 3000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2389)

    def lambda_23A1():
        OP_67(0, 6320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23A1)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    Sleep(2000)

    def lambda_23D2():
        OP_6B(1500, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23D2)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_44(0x102, 0x0)
    OP_44(0x102, 0x3)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x18\x07\x0C#40W听我说，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Sleep(3000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x00Episode『庆功宴之夜』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2543")
    Sleep(1000)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x4, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_24C9")
    Jump("loc_2504")

    label("loc_24C9")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "\x06\x07\x02雅餐『喜悦』\x07\x00的制作方法已经记下了。\x02",
    )

    CloseMessageWindow()

    label("loc_2504")

    AddMira(3500)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02３５００米拉\x07\x00。\x02",
    )

    Jump("loc_2537")

    label("loc_2537")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2543")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4204   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_16_2266 end

    def Function_17_2552(): pass

    label("Function_17_2552")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(191)
    SetChrPos(0x102, 10620, 14000, 77890, 270)
    Call(0, 10)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x28, 0x40)
    OP_4A(0x41, 0)
    OP_4A(0x42, 0)
    SetChrChipByIndex(0x41, 49)
    SetChrChipByIndex(0x42, 49)
    SetChrSubChip(0x41, 0)
    SetChrSubChip(0x42, 0)
    OP_4A(0x43, 0)
    OP_4A(0x44, 0)
    SetChrChipByIndex(0x43, 49)
    SetChrChipByIndex(0x44, 49)
    SetChrSubChip(0x43, 0)
    SetChrSubChip(0x44, 0)
    SetChrPos(0x25, 570, 14000, 79770, 180)
    SetChrPos(0x15, -550, 14000, 80170, 180)
    SetChrPos(0x26, 1010, 14000, 81490, 180)
    SetChrPos(0x1B, 10, 14000, 83200, 180)
    SetChrPos(0x29, -1420, 14000, 83200, 180)
    SetChrPos(0x28, 1350, 14000, 83200, 180)
    OP_4A(0x25, 0)
    OP_4A(0x15, 0)
    OP_4A(0x26, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x29, 0)
    OP_4A(0x28, 0)
    OP_8C(0x10, 0, 0)
    OP_8C(0x13, 0, 0)
    OP_8C(0x14, 0, 0)
    OP_8C(0x16, 0, 0)
    OP_8C(0x18, 0, 0)
    OP_8C(0x19, 0, 0)
    OP_8C(0x1A, 0, 0)
    OP_8C(0x2E, 0, 0)
    OP_8C(0x2F, 0, 0)
    OP_8C(0x32, 0, 0)
    OP_8C(0x33, 0, 0)
    OP_8C(0x1C, 0, 0)
    OP_8C(0x20, 90, 0)
    OP_8C(0x21, 90, 0)
    OP_8C(0x22, 90, 0)
    OP_8C(0x23, 90, 0)
    OP_8C(0x24, 90, 0)
    OP_8C(0x30, 90, 0)
    OP_8C(0x31, 90, 0)
    OP_8C(0x17, 315, 0)
    OP_8C(0x34, 315, 0)
    OP_4A(0x10, 0)
    OP_4A(0x11, 0)
    OP_4A(0x13, 0)
    OP_4A(0x14, 0)
    OP_4A(0x15, 0)
    OP_4A(0x16, 0)
    OP_4A(0x17, 0)
    OP_4A(0x18, 0)
    OP_4A(0x19, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    OP_4A(0x28, 0)
    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    OP_4A(0x2D, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x30, 0)
    OP_4A(0x31, 0)
    OP_4A(0x32, 0)
    OP_4A(0x33, 0)
    OP_4A(0x34, 0)
    OP_4A(0x35, 0)
    OP_4A(0x36, 0)
    OP_4A(0x37, 0)
    OP_4A(0x38, 0)
    OP_4A(0x39, 0)
    OP_4A(0x3A, 0)
    OP_4A(0x3B, 0)
    OP_4A(0x3C, 0)
    OP_4A(0x3D, 0)
    OP_4A(0x3E, 0)
    OP_4A(0x3F, 0)
    OP_4A(0x40, 0)
    OP_4A(0x45, 0)
    OP_4A(0x41, 0)
    OP_4A(0x42, 0)
    OP_4A(0x43, 0)
    OP_4A(0x44, 0)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    Sleep(1500)
    OP_6D(-840, 14000, 79350, 0)
    OP_67(0, 4120, -10000, 0)
    OP_6B(3210, 0)
    OP_6C(60000, 0)
    OP_6E(334, 0)

    def lambda_2839():
        OP_6D(-9700, 14000, 74820, 8000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_2839)

    def lambda_2851():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_2851)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("艾莉茜雅女王")

    AnonymousTalk(    #4 op#A op#5
        (
            "\x07\x00#55A…………我们的王都\x01",
            "虽然遭受了危机……\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    Fade(1000)
    OP_44(0x47, 0xFF)
    OP_6D(500, 12000, 56180, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(36000, 0)
    OP_6E(262, 0)

    def lambda_290C():
        OP_6D(-500, 12000, 68180, 9000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_290C)

    def lambda_2924():
        OP_6C(53000, 9000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_2924)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("艾利茜雅女王")

    AnonymousTalk(    #5 op#A op#5
        (
            "\x07\x00#50A…………但是托各位的福，\x01",
            "使『异变』得以终结。\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    LoadEffect(0x0, "map\\mp032_00.eff")
    Fade(1000)
    OP_44(0x47, 0xFF)
    OP_6D(0, 14000, 83260, 0)
    OP_67(0, 2810, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(0, 0)
    OP_6E(368, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #6
        0x25,
        (
            "#094F#5P……为此，\x01",
            "今天在这里开办了\x01",
            "一个小规模的庆祝会。\x02\x03",

            "#090F好了，科洛蒂娅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x15,
        "#1873F#5P是。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2A82():
        OP_8E(0xFE, 0xFFFFFDDA, 0x36B0, 0x13542, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2A82)
    WaitChrThread(0x15, 0x1)
    Sleep(500)

    ChrTalk(    #8
        0x15,
        (
            "#1810F#5P……本日的宴会\x01",
            "邀请的都是为这次事件\x01",
            "贡献力量的人。\x02\x03",

            "#1817F向苦难的人们伸出温暖的援助之手，\x01",
            "将人们从不安的每一天中\x01",
            "解救出来的各位……\x02\x03",

            "我作为利贝尔的王太女\x01",
            "向你们表示由衷的感谢。\x02\x03",

            "#1818F真的非常感谢你们。\x02\x03",

            "今天的宴会\x01",
            "虽然规模不大……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x35, 0x80)
    SetChrFlags(0x35, 0x40)
    SetChrPos(0x35, 9720, 14000, 76650, 270)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x40)
    SetChrPos(0x36, 8750, 14000, 77790, 270)

    ChrTalk(    #9
        0x35,
        "#1P……安全上垒！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x36,
        (
            "#1P总、总算赶到了……\x02\x03",

            "那、那我就不客气了～……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C5C():
        OP_8E(0xFE, 0xFBE, 0x36B0, 0x12B6A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_2C5C)
    WaitChrThread(0x35, 0x1)
    Sleep(150)

    def lambda_2C81():

        label("loc_2C81")

        TurnDirection(0xFE, 0x36, 400)
        OP_48()
        Jump("loc_2C81")

    QueueWorkItem2(0x35, 2, lambda_2C81)
    Sleep(500)

    ChrTalk(    #11
        0x35,
        (
            "#142F#3P朵洛希，你在干什么！！\x01",
            "赶快准备好相机！！\x02\x03",

            "#144F讲话马上\x01",
            "就要结束了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x36,
        "#1P呜呜，是吗……\x02",
    )

    CloseMessageWindow()

    def lambda_2D18():
        OP_8E(0xFE, 0x1388, 0x36B0, 0x12FDE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_2D18)
    WaitChrThread(0x36, 0x1)
    OP_44(0x35, 0x2)

    def lambda_2D3C():
        OP_8C(0xFE, 315, 500)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_2D3C)
    OP_8C(0x36, 315, 500)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x36, 50)
    SetChrSubChip(0x36, 0)
    OP_0D()
    OP_43(0x36, 0x1, 0x0, 0x8)
    Sleep(2000)

    ChrTalk(    #13
        0x15,
        (
            "#1815F#5P哎…………\x02\x03",

            "请、请各位\x01",
            "尽情享受这一刻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x26,
        (
            "#225F#5P聚集在这里的每一位\x01",
            "都肩负着各种各样的责任，\x01",
            "每天的工作都很忙碌。\x02\x03",

            "#220F就请你们在今晚忘掉平日的劳累，\x01",
            "充分地放松一下。\x02\x03",

            "我们为大家准备了美味佳肴。\x01",
            "请尽情享用！\x02\x03",

            "#221F愿女神赐福于利贝尔！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xBF, 0x0, 0x64)
    OP_20(0x7D0)
    Sleep(2000)
    OP_21()
    OP_44(0x36, 0x1)
    FadeToBright(100, 16777215)
    OP_1D(0x4B)
    Sleep(500)

    def lambda_2EBE():

        label("loc_2EBE")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_2EBE")

    QueueWorkItem2(0x36, 2, lambda_2EBE)

    def lambda_2ECF():

        label("loc_2ECF")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_2ECF")

    QueueWorkItem2(0x35, 2, lambda_2ECF)

    def lambda_2EE0():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_2EE0)
    Sleep(100)

    def lambda_2F00():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F00)
    Sleep(100)

    def lambda_2F20():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_2F20)
    Sleep(100)

    def lambda_2F40():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2F40)
    Sleep(100)

    def lambda_2F60():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2F60)
    Sleep(100)

    def lambda_2F80():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_2F80)
    Sleep(3000)
    Fade(1000)
    OP_6D(12000, 14000, 80820, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    OP_44(0x25, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x29, 0x1)
    OP_44(0x28, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x36, 0x2)
    OP_44(0x35, 0x2)
    OP_4B(0x25, 0)
    OP_4B(0x15, 0)
    OP_4B(0x26, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x29, 0)
    OP_4B(0x28, 0)
    SetChrChipByIndex(0x36, 43)
    SetChrSubChip(0x36, 0)
    OP_4B(0x41, 0)
    OP_4B(0x42, 0)
    SetChrChipByIndex(0x41, 48)
    SetChrChipByIndex(0x42, 48)
    SetChrSubChip(0x41, 0)
    SetChrSubChip(0x42, 0)
    OP_4B(0x43, 0)
    OP_4B(0x44, 0)
    SetChrChipByIndex(0x43, 48)
    SetChrChipByIndex(0x44, 48)
    SetChrSubChip(0x43, 0)
    SetChrSubChip(0x44, 0)
    ClearChrFlags(0x25, 0x40)
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x26, 0x40)
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x29, 0x40)
    ClearChrFlags(0x28, 0x40)
    Call(0, 9)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x405, 0x0)
    ExitThread()
    OP_4A(0x3D, 0)
    OP_4A(0x3E, 0)
    OP_4A(0x3F, 0)
    OP_4A(0x40, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x11,
        (
            "#1017F#5P……嗯～\x01",
            "科洛丝真的好厉害呢。\x02\x03",

            "穿着那样的礼裙\x01",
            "在大家的面前\x01",
            "光明正大地讲话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1053F#11P嗯，之前遇到她的时候\x01",
            "还说自己没有什么自信的……\x02\x03",

            "#1041F身为王太女，\x01",
            "真的做得很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#1008F#5P哇，真好……\x02\x03",

            "#1016F要是我穿上那样的礼裙\x01",
            "也很合适的话就好了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x11, 400)
    Sleep(300)

    ChrTalk(    #18
        0x102,
        "#1044F#12P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #19
        0x11,
        "#1019F#5P……嗯？怎么沉默了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1053F#12P没什么，该怎么说呢……\x02\x03",

            "#1041F……我再次确认了\x01",
            "艾丝蒂尔是个女孩子\x01",
            "这个事实而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "#1013F#5P什、什么嘛……！\x02\x03",

            "#1007F那是因为最近在这里\x01",
            "忙于复兴王都的事情，\x01",
            "连家都没能回一次。\x02\x03",

            "#1019F……我当然也偶尔\x01",
            "会想要穿上美丽的衣服\x01",
            "看看嘛！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1049F#12P好～好。\x02\x03",

            "#1054F……不过，在这几周里\x01",
            "艾丝蒂尔也成长了许多呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x11,
        "#1004F#5P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#1053F#12P在利贝尔四处奔走，\x01",
            "可不是一件\x01",
            "简单的任务……\x02\x03",

            "艾丝蒂尔作为游击士的判断力\x01",
            "已经变得很值得信赖了……\x02\x03",

            "#1041F说实话，就算是我来评价，\x01",
            "也可以称得上是很可靠的了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1008F#5P啊、啊哈哈……\x02\x03",

            "#1016F被约修亚这么一夸，\x01",
            "总觉得很不好意思……\x02\x03",

            "#1017F……好在这几天\x01",
            "事情总算告一段落了。\x02\x03",

            "王都的复兴也在顺利进行中……\x02\x03",

            "终于，可以平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1053F#12P…………嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x11, 225, 500)
    Sleep(300)

    ChrTalk(    #27
        0x11,
        "#1004F#5P啊…………\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_3628():
        OP_8C(0x102, 225, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3628)
    SetChrPos(0x39, -9350, 12000, 61660, 180)
    SetChrPos(0x2E, -3880, 12000, 59720, 315)
    SetChrPos(0x2F, -3900, 12000, 61790, 225)
    SetChrPos(0x1A, -8100, 12000, 57040, 270)
    SetChrPos(0x19, -8100, 12000, 58540, 270)

    def lambda_368B():
        OP_6D(-7020, 12000, 59000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_368B)

    def lambda_36A3():
        OP_6C(40000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_36A3)

    def lambda_36B3():
        OP_6B(2720, 2500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_36B3)

    def lambda_36C3():
        OP_67(0, 6700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_36C3)
    WaitChrThread(0x47, 0x0)
    Sleep(500)

    ChrTalk(    #28
        0x11,
        (
            "#1008F#6P啊啊……\x01",
            "好丰盛的料理……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1040F#12P好像是格兰赛尔城的厨师们\x01",
            "正在帮大家送分好的料理吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(800)
    OP_6D(12000, 14000, 80820, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x11,
        (
            "#1006F#5P嗯，绝对不能错过这样的机会。\x02\x03",

            "上次的女王诞辰庆典\x01",
            "都没有好好吃够呢……\x02\x03",

            "#1001F…………这次\x01",
            "我一定不能客气了……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(400)

    ChrTalk(    #31
        0x11,
        (
            "#1018F#5P约修亚，你在这里等一下！\x01",
            "我去看看情况！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3886():

        label("loc_3886")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_3886")

    QueueWorkItem2(0x102, 1, lambda_3886)
    OP_8C(0x11, 270, 400)
    Sleep(300)
    OP_43(0x11, 0x1, 0x0, 0x7)

    def lambda_38AA():
        OP_6D(7900, 14000, 79710, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_38AA)

    def lambda_38C2():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_38C2)
    WaitChrThread(0x47, 0x0)
    Sleep(3000)
    OP_44(0x102, 0x1)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(11610, 14000, 78880, 1500)
    OP_44(0x11, 0x1)
    SetChrPos(0x39, -8189, 12000, 60260, 180)
    SetChrPos(0x2E, -5950, 12000, 59520, 225)
    SetChrPos(0x2F, -6530, 12000, 60440, 225)
    SetChrPos(0x1A, -8100, 12000, 57040, 0)
    SetChrPos(0x19, -5220, 12000, 57140, 270)
    SetChrPos(0x11, -8100, 12000, 58540, 180)
    SetChrSubChip(0x11, 0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #32
        0x102,
        (
            "#1054F#5P……这种方面\x01",
            "倒是毫无长进…………\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x35, 800, 14000, 77890, 90)
    SetChrPos(0x36, 800, 14000, 78900, 90)

    def lambda_39D8():
        OP_8E(0xFE, 0x221A, 0x36B0, 0x13042, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_39D8)
    Sleep(600)

    def lambda_39F8():
        OP_8E(0xFE, 0x17D4, 0x36B0, 0x13434, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_39F8)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3A2F():

        label("loc_3A2F")

        TurnDirection(0xFE, 0x35, 400)
        OP_48()
        Jump("loc_3A2F")

    QueueWorkItem2(0x102, 2, lambda_3A2F)
    WaitChrThread(0x35, 0x1)

    ChrTalk(    #33
        0x35,
        (
            "#141F#6P哦，这不是约修亚吗。\x02\x03",

            "艾丝蒂尔那家伙怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#1053F#11P……嗯，去取料理了。\x02\x03",

            "#1040F奈尔先生，\x01",
            "你们正在进行工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x35,
        (
            "#147F#6P是啊，\x01",
            "难得聚集了这么多人。\x02\x03",

            "我得趁这个机会\x01",
            "好好让大家发表感想啊！\x02\x03",

            "#141F……当然，\x01",
            "待会儿还要找你们取材。\x02\x03",

            "可别随便回去啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1054F#11P呵呵……明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x35,
        (
            "#147F#6P好，接下来是\x01",
            "对科洛蒂娅公主进行采访！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x35, 0x36, 500)
    Sleep(300)

    ChrTalk(    #38
        0x35,
        "#144F#11P…………朵洛希！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x36,
        "#154F#6P#40W不、不行了，我要晕倒了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_9E(0x36, 0x14, 0x0, 0x190, 0x9C4)
    Sleep(800)

    ChrTalk(    #40
        0x36,
        "#152F#6P#40W给我一点吃的吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x35,
        "#144F#11P喂，别磨磨蹭蹭了！\x02",
    )

    CloseMessageWindow()
    OP_43(0x35, 0x3, 0x0, 0x12)

    def lambda_3CCF():

        label("loc_3CCF")

        TurnDirection(0xFE, 0x35, 1000)
        OP_48()
        Jump("loc_3CCF")

    QueueWorkItem2(0x36, 2, lambda_3CCF)
    Sleep(200)
    OP_62(0x36, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    OP_44(0x36, 0x2)

    ChrTalk(    #42 op#A op#5
        0x36,
        (
            "#152F#5P#39A呜～\x01",
            "奈尔前辈欺负人……！\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x36, 0x3, 0x0, 0x13)
    WaitChrThread(0x36, 0x3)

    ChrTalk(    #43
        0x102,
        (
            "#1053F#5P奈尔先生今天可是\x01",
            "全神贯注啊……\x02\x03",

            "#1044F哎，艾丝蒂尔呢……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x36, 0x3)
    OP_44(0x102, 0x2)
    ClearChrFlags(0x35, 0x40)
    ClearChrFlags(0x36, 0x40)
    OP_4B(0x35, 0)
    OP_4B(0x36, 0)
    SetChrPos(0x35, 12210, 12000, 57070, 270)
    SetChrPos(0x36, 6500, 12000, 60670, 270)

    def lambda_3DD2():
        OP_6D(-7020, 12000, 59000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_3DD2)

    def lambda_3DEA():
        OP_6C(40000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_3DEA)

    def lambda_3DFA():
        OP_6B(2720, 2500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_3DFA)

    def lambda_3E0A():
        OP_67(0, 6700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_3E0A)
    WaitChrThread(0x47, 0x0)
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_3E3E():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3E3E)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_3E78():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3E78)
    Sleep(1000)
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_3EB2():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3EB2)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    def lambda_3EEC():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3EEC)
    Sleep(2000)
    Fade(800)
    OP_6D(11640, 14000, 79050, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x102,
        (
            "#1052F#5P呼，\x01",
            "又干什么去了……\x02\x03",

            "#1043F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(500)
    OP_8C(0x102, 270, 300)
    Sleep(400)

    ChrTalk(    #45
        0x102,
        (
            "#1035F#11P（……也好。）\x02\x03",

            "（聚集到这里来的人\x01",
            "　都曾给了我不少关照……）\x02\x03",

            "#1041F（……趁这个机会和他们打个招呼吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(10620, 14000, 77890, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4B(0x10, 0)
    OP_4B(0x11, 0)
    OP_4B(0x13, 0)
    OP_4B(0x14, 0)
    OP_4B(0x15, 0)
    OP_4B(0x16, 0)
    OP_4B(0x17, 0)
    OP_4B(0x18, 0)
    OP_4B(0x19, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x20, 0)
    OP_4B(0x21, 0)
    OP_4B(0x22, 0)
    OP_4B(0x23, 0)
    OP_4B(0x24, 0)
    OP_4B(0x25, 0)
    OP_4B(0x26, 0)
    OP_4B(0x27, 0)
    OP_4B(0x28, 0)
    OP_4B(0x29, 0)
    OP_4B(0x2A, 0)
    OP_4B(0x2B, 0)
    OP_4B(0x2C, 0)
    OP_4B(0x2D, 0)
    OP_4B(0x2E, 0)
    OP_4B(0x2F, 0)
    OP_4B(0x30, 0)
    OP_4B(0x31, 0)
    OP_4B(0x32, 0)
    OP_4B(0x33, 0)
    OP_4B(0x34, 0)
    OP_4B(0x35, 0)
    OP_4B(0x36, 0)
    OP_4B(0x37, 0)
    OP_4B(0x38, 0)
    OP_4B(0x39, 0)
    OP_4B(0x3A, 0)
    OP_4B(0x3B, 0)
    OP_4B(0x3C, 0)
    OP_4B(0x3D, 0)
    OP_4B(0x3E, 0)
    OP_4B(0x3F, 0)
    OP_4B(0x40, 0)
    OP_4B(0x45, 0)
    OP_4B(0x41, 0)
    OP_4B(0x42, 0)
    OP_4B(0x43, 0)
    OP_4B(0x44, 0)
    OP_4B(0x3D, 0)
    OP_4B(0x3F, 0)
    OP_4B(0x3E, 0)
    OP_4B(0x40, 0)
    OP_A2(0x2F9A)
    EventEnd(0x0)
    Return()

    # Function_17_2552 end

    def Function_18_418D(): pass

    label("Function_18_418D")

    OP_8C(0x35, 270, 500)

    def lambda_419A():
        OP_8E(0xFE, 0xC6C, 0x36B0, 0x13042, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_419A)
    WaitChrThread(0x35, 0x1)

    def lambda_41BA():
        OP_8E(0xFE, 0xC6C, 0x2EE0, 0x10194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_41BA)
    WaitChrThread(0x35, 0x1)
    Return()

    # Function_18_418D end

    def Function_19_41D5(): pass

    label("Function_19_41D5")


    def lambda_41DB():
        OP_8E(0xFE, 0xC6C, 0x36B0, 0x129A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_41DB)
    WaitChrThread(0x36, 0x1)

    def lambda_41FB():
        OP_8E(0xFE, 0xC6C, 0x36B0, 0x11170, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_41FB)
    WaitChrThread(0x36, 0x1)
    Return()

    # Function_19_41D5 end

    def Function_20_4216(): pass

    label("Function_20_4216")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_6D(-130, 14000, 78620, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrPos(0x102, -130, 14000, 78620, 0)
    OP_4A(0x40, 255)
    SetChrPos(0x40, -13960, 14000, 73930, 90)
    Sleep(1000)
    FadeToBright(2000, 0)

    def lambda_42A6():
        OP_6D(500, 14000, 82000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_42A6)
    OP_8E(0x102, 0x0, 0x36B0, 0x13E20, 0x5DC, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #46
        0x102,
        (
            "#1053F#6P……差不多已经转遍了。\x02\x03",

            "有些人刚才正在忙，\x01",
            "一会儿再去\x01",
            "向他们打个招呼吧…………\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x35, 255)
    SetChrPos(0x35, -1780, 12000, 70020, 0)
    SetChrFlags(0x35, 0x40)

    def lambda_435D():
        OP_6D(500, 14000, 78700, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_435D)

    def lambda_4375():
        OP_8E(0xFE, 0xFFFFF90C, 0x36B0, 0x12EBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_4375)
    WaitChrThread(0x35, 0x1)
    OP_8C(0x35, 270, 400)
    Sleep(300)
    OP_62(0x35, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #47
        0x35,
        (
            "#141F#11P哦，有了有了。\x02\x03",

            "朵洛希，接下来是军队的人！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43FF():

        label("loc_43FF")

        TurnDirection(0xFE, 0x35, 500)
        OP_48()
        Jump("loc_43FF")

    QueueWorkItem2(0x102, 2, lambda_43FF)
    OP_4A(0x36, 255)
    SetChrFlags(0x36, 0x40)
    SetChrPos(0x36, -840, 12000, 70900, 0)

    def lambda_442A():

        label("loc_442A")

        TurnDirection(0xFE, 0x36, 500)
        OP_48()
        Jump("loc_442A")

    QueueWorkItem2(0x35, 2, lambda_442A)
    Sleep(300)

    ChrTalk(    #48
        0x35,
        "#144F#5P……喂，赶快！\x02",
    )

    CloseMessageWindow()

    def lambda_4463():
        OP_8E(0xFE, 0xFFFFFCB8, 0x36B0, 0x12AFC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_4463)
    WaitChrThread(0x36, 0x1)
    OP_8C(0x36, 315, 400)
    Sleep(500)

    ChrTalk(    #49
        0x36,
        (
            "#154F#11P#40W前～辈……\x02\x03",

            "总觉得……\x01",
            "肚子里咕噜咕噜的～……\x02\x03",

            "#152F呜呜，好不舒服啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x35,
        (
            "#145F#5P……是你刚才\x01",
            "喝太多了吧。\x02\x03",

            "#142F喂，别在那里磨蹭了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x36,
        "#154F#11P好、好的…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x36, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_44(0x35, 0x2)
    OP_8C(0x35, 270, 500)

    def lambda_4592():
        OP_8E(0xFE, 0xFFFFDCD8, 0x36B0, 0x12EBC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_4592)
    Sleep(500)

    def lambda_45B2():
        OP_8E(0xFE, 0xFFFFF90C, 0x36B0, 0x12EBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_45B2)
    WaitChrThread(0x36, 0x1)

    def lambda_45D2():
        OP_8E(0xFE, 0xFFFFDCD8, 0x36B0, 0x12EBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_45D2)
    Sleep(1000)
    OP_44(0x102, 0x2)
    OP_8C(0x102, 270, 400)
    WaitChrThread(0x36, 0x1)
    OP_63(0x36)
    OP_4A(0x15, 255)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 0, 12000, 70340, 0)

    NpcTalk(    #52
        0x15,
        "少女的声音",
        "#1P……约修亚。\x02",
    )

    CloseMessageWindow()

    def lambda_4646():
        OP_8E(0xFE, 0x0, 0x36B0, 0x13650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4646)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_4678():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4678)

    def lambda_4686():
        OP_6D(1250, 14000, 81260, 4000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_4686)

    def lambda_469E():
        OP_67(0, 5540, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_469E)

    def lambda_46B6():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_46B6)

    def lambda_46C6():
        OP_6C(55000, 4000)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_46C6)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x47, 0x0)

    ChrTalk(    #53
        0x102,
        (
            "#1054F#5P……科洛丝。\x01",
            "你真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x15,
        (
            "#1814F#12P……啊…………\x02\x03",

            "#1815F嗯，有一点吧……\x02\x03",

            "#1872F自从成了王太女，\x01",
            "就有越来越多的记者\x01",
            "来找我采访……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1053F#5P嗯。\x02\x03",

            "#1041F最近，在许多的杂志上\x01",
            "都可以看到科洛丝的照片。\x02\x03",

            "感觉和以前简直\x01",
            "就是判若两人哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x15,
        "#1815F#12P啊、啊哈哈…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        (
            "#1053F#5P再过不久，\x01",
            "这股热潮应该就会退去了。\x02\x03",

            "#1040F最近这段时间之内\x01",
            "可能还是比较辛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x15,
        (
            "#1873F#12P……嗯，我明白。\x02\x03",

            "#1810F我已经下定决心了。\x01",
            "一定要守护大家……\x02\x03",

            "所以，我是绝对不会\x01",
            "因为这点事情而受挫的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        (
            "#1035F#5P是吗……\x02\x03",

            "#1054F……你果然很坚强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x15,
        (
            "#1815F#12P没有啦。\x02\x03",

            "其实我总是\x01",
            "没有什么自信的。\x02\x03",

            "而且还经常\x01",
            "做些傻事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#1053F#5P唔，不过……\x02\x03",

            "我们初次见面时，\x01",
            "你就在孤儿院里保护着\x01",
            "克拉姆不被艾丝蒂尔欺负对吧。\x02\x03",

            "#1041F……科洛丝，\x01",
            "我觉得你才是真正的坚强呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x15,
        (
            "#1815F#12P啊、啊哈哈……\x01",
            "谢谢。\x02\x03",

            "#1870F……说、说起来，\x01",
            "是有这么一回事。\x02\x03",

            "……………………………………\x02\x03",

            "#1873F（就趁现在，可以吗…………？）\x02",
        )
    )

    Jump("loc_4B2C")

    label("loc_4B2C")

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x102,
        "#1040F#5P…………科洛丝？\x02",
    )

    CloseMessageWindow()
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #64
        0x15,
        "科洛丝",
        (
            "#1817F#12P…………那个，约修亚。\x02\x03",

            "#1812F…………能不能\x01",
            "占用你一点时间呢？\x02\x03",

            "我有些话想对你说。\x02",
        )
    )

    Jump("loc_4C15")

    label("loc_4C15")

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1044F#5P这……这个…………\x02\x03",

            "嗯，好的…………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #66
        0x15,
        "科洛丝",
        "#1817F#12P………这边……………\x02",
    )

    Jump("loc_4C91")

    label("loc_4C91")

    CloseMessageWindow()

    def lambda_4C98():

        label("loc_4C98")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_4C98")

    QueueWorkItem2(0x102, 2, lambda_4C98)
    OP_8C(0x15, 90, 300)
    Sleep(300)

    def lambda_4CB5():
        OP_6D(4320, 14000, 81910, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_4CB5)
    OP_43(0x15, 0x0, 0x0, 0x18)
    Sleep(2000)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x47, 0x0)
    Sleep(2000)

    def lambda_4CF5():
        OP_6D(890, 14000, 82020, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_4CF5)
    WaitChrThread(0x47, 0x0)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #67
        0x102,
        (
            "#1043F（……是我的错觉吗……\x01",
            "  感觉好像惹她生气了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    OP_8C(0x102, 225, 400)
    Sleep(300)

    ChrTalk(    #68
        0x102,
        "#1044F#5P（唔，艾丝蒂尔呢……）\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_4A(0x11, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x33, 0)
    OP_4A(0x32, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x19, 0)
    OP_4A(0x39, 0)
    SetChrPos(0x33, -5960, 12000, 58200, 270)
    SetChrPos(0x32, -7250, 12000, 55970, 315)
    OP_8C(0x11, 270, 0)
    OP_8C(0x1A, 270, 0)
    Fade(1000)
    OP_6D(-7020, 12000, 59000, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(40000, 0)
    OP_6E(285, 0)
    OP_43(0x11, 0x3, 0x0, 0x15)
    Sleep(500)
    OP_43(0x1A, 0x3, 0x0, 0x16)
    OP_0D()

    ChrTalk(    #69
        0x1A,
        "#11P嚼嚼嚼嚼……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        "#5P咕嘟咕嘟…………咕嘟。\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x3)

    ChrTalk(    #71
        0x11,
        "#5P#1005F#3S还没完呢～！！#2S\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x11, 0x3, 0x0, 0x15)

    ChrTalk(    #72
        0x33,
        (
            "#202F哦哦……\x01",
            "这位小姑娘开始发力了！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x1A, 0x3)
    TurnDirection(0x1A, 0x33, 1000)
    Sleep(500)

    ChrTalk(    #73
        0x1A,
        (
            "#1564F#6P大、大哥！！\x01",
            "你敌我不分了啦！！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(1300, 14000, 82260, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x102,
        (
            "#1052F#5P（……算了。\x01",
            "  好像玩得很尽兴嘛。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #75
        0x102,
        (
            "#1043F#6P（……科洛丝………）\x02\x03",

            "（我说了什么\x01",
            "  让她生气的话吗………）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5052():
        OP_8E(0xFE, 0x19C8, 0x36B0, 0x13E20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5052)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(31990, 14000, 73090, 0)
    OP_67(0, 7190, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(45000, 0)
    OP_6E(368, 0)
    OP_22(0x1CC, 0x1, 0x46)
    OP_44(0x102, 0xFF)
    SetChrPos(0x15, 42860, 16000, 80150, 90)
    SetChrPos(0x102, 30240, 14000, 70320, 45)
    OP_43(0x102, 0x0, 0x0, 0x17)
    FadeToBright(2000, 0)

    def lambda_50F0():
        OP_6D(45090, 14000, 82890, 7000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_50F0)
    Sleep(5000)
    OP_20(0x1388)
    WaitChrThread(0x47, 0x0)

    def lambda_5117():
        OP_6D(43080, 16000, 80470, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_5117)

    def lambda_512F():
        OP_67(0, 6450, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_512F)

    def lambda_5147():
        OP_6B(2090, 3000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_5147)

    def lambda_5157():
        OP_6E(332, 3000)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_5157)
    WaitChrThread(0x47, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(500)

    ChrTalk(    #76
        0x102,
        (
            "#1043F#6P……请问，科洛丝。\x02\x03",

            "#1040F你要说的话是……？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0x15,
        "科洛丝",
        "#1817F#5P#40W………………………………\x02",
    )

    Jump("loc_51FA")

    label("loc_51FA")

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#1052F#6P那、那个…………\x02\x03",

            "#1043F要是有什么惹你生气的，\x01",
            "我在这里先向你道歉…………\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #79
        0x15,
        "科洛丝",
        "#1870F#5P……我…………\x02",
    )

    Jump("loc_52B4")

    label("loc_52B4")

    CloseMessageWindow()
    OP_59()
    Fade(500)

    def lambda_52C1():
        OP_6D(42650, 16000, 80970, 1500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_52C1)

    def lambda_52D9():
        OP_67(0, 6460, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_52D9)

    def lambda_52F1():
        OP_6B(1900, 1500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_52F1)

    def lambda_5301():
        OP_6C(21000, 1500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_5301)

    def lambda_5311():
        OP_6E(385, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_5311)
    OP_8C(0x15, 250, 300)
    WaitChrThread(0x47, 0x0)
    Sleep(500)

    NpcTalk(    #80
        0x15,
        "科洛丝",
        "#1812F#11P我喜欢你。\x02",
    )

    Jump("loc_535C")

    label("loc_535C")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(500)

    ChrTalk(    #81
        0x102,
        "#1044F#6P#3S哎……？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_1D(0x75)
    Sleep(1000)

    NpcTalk(    #82
        0x15,
        "科洛丝",
        "#1810F#11P…………………………\x02",
    )

    Jump("loc_53F0")

    label("loc_53F0")

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        "#1042F#6P这、这…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x15,
        "科洛丝",
        "#1812F#11P…………………………\x02",
    )

    Jump("loc_544F")

    label("loc_544F")

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1054F#6P#40W那……那………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #86
        0x15,
        "科洛丝",
        "#1817F#11P…………………………\x02",
    )

    Jump("loc_54B2")

    label("loc_54B2")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #87
        0x102,
        (
            "#1052F#6P#40W对、对不起…………\x02\x03",

            "#1056F……你的情意我……\x01",
            "我……我很高兴，但是………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0x15,
        "科洛丝",
        (
            "#1873F#11P呵呵…………\x02\x03",

            "……好了，\x01",
            "你什么也不用说。\x02\x03",

            "#1818F我只是为了转换心情\x01",
            "才会这么说出来的。\x02",
        )
    )

    Jump("loc_55C4")

    label("loc_55C4")

    CloseMessageWindow()
    OP_8C(0x15, 60, 400)
    Sleep(500)

    NpcTalk(    #89
        0x15,
        "科洛丝",
        "#1872F#5P好美的星空啊……\x02",
    )

    Jump("loc_5606")

    label("loc_5606")

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#1044F#6P那个，我说…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #91
        0x102,
        (
            "#1043F#6P#40W你从什么时候开始……\x01",
            "………那个……………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #92
        0x15,
        "科洛丝",
        (
            "#1817F#5P…………约修亚。\x02\x03",

            "如果，\x01",
            "你遇见我\x01",
            "比遇见艾丝蒂尔早的话……\x02\x03",

            "#1819F就不会是艾丝蒂尔\x01",
            "…………而是………我吗？\x02",
        )
    )

    Jump("loc_5744")

    label("loc_5744")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #93
        0x102,
        (
            "#1035F#6P不……\x02\x03",

            "……我想不会的。\x02\x03",

            "#1043F……对不起，科洛丝。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #94
        0x15,
        "科洛丝",
        (
            "#1815F#5P……这样就好了。\x02\x03",

            "#1872F想独占约修亚的心情\x01",
            "虽然不是假的……\x02\x03",

            "可是如果真的变成那样，\x01",
            "却不是我所希望的事情。\x02\x03",

            "#1873F……艾丝蒂尔和约修亚……\x01",
            "你们两个……\x02\x03",

            "#1818F……我都喜欢。\x02",
        )
    )

    Jump("loc_58AA")

    label("loc_58AA")

    CloseMessageWindow()
    OP_8C(0x15, 250, 400)
    Sleep(300)

    NpcTalk(    #95
        0x15,
        "科洛丝",
        (
            "#1872F#11P所以最后，\x01",
            "我想见识一下你为难时的表情。\x02\x03",

            "#1815F呵呵……\x01",
            "刚才约修亚的表情啊……\x02\x03",

            "#1818F可是我见过最有趣的呢。\x02",
        )
    )

    Jump("loc_5957")

    label("loc_5957")

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#1044F#6P啊…………\x02\x03",

            "#1052F……这个…………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #97
        0x102,
        (
            "#1048F#6P……科洛丝，\x01",
            "你还真会捉弄人啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #98
        0x15,
        "科洛丝",
        (
            "#1815F#11P呵呵，\x01",
            "已经很久没有\x01",
            "像现在这样热闹了。\x02",
        )
    )

    Jump("loc_5A35")

    label("loc_5A35")

    CloseMessageWindow()
    Sleep(300)

    def lambda_5A41():
        OP_6D(42000, 16000, 80640, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_5A41)

    def lambda_5A59():
        OP_67(0, 6930, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_5A59)

    def lambda_5A71():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_5A71)

    def lambda_5A81():
        OP_8E(0xFE, 0xA08C, 0x3E80, 0x13A56, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5A81)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x47, 0x0)
    Sleep(500)

    NpcTalk(    #99
        0x15,
        "科洛丝",
        (
            "#1817F#5P……好了…………\x02\x03",

            "#1812F约修亚，\x01",
            "你到底在烦恼什么呢？\x02",
        )
    )

    Jump("loc_5B06")

    label("loc_5B06")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 0, 500)
    Sleep(300)

    ChrTalk(    #100
        0x102,
        "#1044F#12P#3S咦……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 180, 400)
    Sleep(300)

    NpcTalk(    #101
        0x15,
        "科洛丝",
        (
            "#1815F#5P呵呵…………\x01",
            "这点事情我还是能看出来的。\x02\x03",

            "我本来感觉就比较敏锐，\x01",
            "刚才也……\x02\x03",

            "#1870F……在接受采访期间，\x01",
            "我一直在注视着\x01",
            "你的身影呢。\x02",
        )
    )

    Jump("loc_5C14")

    label("loc_5C14")

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#1056F#12P…………这个。\x02\x03",

            "#1052F这还真是\x01",
            "不好意思啊……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #103
        0x15,
        "科洛丝",
        "#1815F#5P啊、啊哈哈……\x02",
    )

    Jump("loc_5C93")

    label("loc_5C93")

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #104
        0x15,
        "科洛丝",
        (
            "#1817F#5P……约修亚，\x01",
            "你有事情在瞒着大家吧。\x02\x03",

            "#1812F你又打算一个人\x01",
            "去做什么事情了？\x02",
        )
    )

    Jump("loc_5D0F")

    label("loc_5D0F")

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1043F#12P…………………………\x02\x03",

            "#1052F唉，你真是太敏锐了……\x02\x03",

            "#1054F艾丝蒂尔也时常这样……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #106
        0x15,
        "科洛丝",
        (
            "#1873F#5P呵呵，因为是女孩子嘛。\x02\x03",

            "#1812F好了，\x01",
            "请老实交代吧。\x02",
        )
    )

    Jump("loc_5DE4")

    label("loc_5DE4")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #107
        0x102,
        (
            "#1035F#12P那倒不是能够\x01",
            "称得上烦恼的事……\x02\x03",

            "#1040F我……这么说吧。\x01",
            "我打算下个月之前\x01",
            "离开利贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #108
        0x15,
        "科洛丝",
        (
            "#1814F#5P啊……！？\x02\x03",

            "#1813F为、为什么……呢？\x01",
            "明明已经恢复和平了啊……\x02",
        )
    )

    Jump("loc_5EFC")

    label("loc_5EFC")

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1053F#12P嗯，已经和平了呢。\x02\x03",

            "结社似乎也已经\x01",
            "完全撤离了利贝尔，\x01",
            "各地的重建工作也很顺利。\x02\x03",

            "#1041F……所以，\x01",
            "我想出去旅行。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    OP_8C(0x102, 90, 400)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    def lambda_5FC6():
        OP_6B(1800, 30000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_5FC6)

    ChrTalk(    #110
        0x102,
        (
            "#1053F#6P我…………\x01",
            "现在我已经可以把自己\x01",
            "当作一个人来对待了。\x02\x03",

            "不再是坏掉的人偶。\x02\x03",

            "艾丝蒂尔，以及大家，\x01",
            "也都希望我能这样……\x02\x03",

            "#1043F……可是，\x01",
            "一旦成为了一个人，\x01",
            "我的心却隐隐作痛了。\x02\x03",

            "因为我曾经\x01",
            "犯下了那样多\x01",
            "惨不忍睹的罪行。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #111
        0x15,
        "科洛丝",
        "#1813F#5P……啊………………\x02",
    )

    Jump("loc_6110")

    label("loc_6110")

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1053F#6P……所以，我要偿还这一切。\x02\x03",

            "而且，为了能够真正意义上的坚强起来。\x02\x03",

            "#1041F我决定接下来\x01",
            "到大陆各地去旅行。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #113
        0x15,
        "科洛丝",
        (
            "#1819F#5P是、是这样啊……\x02\x03",

            "#1813F但是这样的话，\x01",
            "你和艾丝蒂尔……\x02",
        )
    )

    Jump("loc_621E")

    label("loc_621E")

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#1043F#6P嗯，短时间内……\x02\x03",

            "#1035F不……应该是很长时间\x01",
            "都无法见面了。\x02\x03",

            "……所以我正在苦恼……\x01",
            "该以怎样的形式将这件事转告给艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #115
        0x15,
        "科洛丝",
        (
            "#1817F#5P………………唉。\x02\x03",

            "#1810F约修亚……\x01",
            "你还是一点都没变呢。\x02",
        )
    )

    Jump("loc_6322")

    label("loc_6322")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #116
        0x102,
        "#1044F#12P哎……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #117
        0x15,
        "科洛丝",
        (
            "#1812F#5P……这种事情，\x01",
            "只能用自己的语言传达吧。\x02\x03",

            "你既然信任着艾丝蒂尔，\x01",
            "那就全部告诉她吧。\x02",
        )
    )

    Jump("loc_63E3")

    label("loc_63E3")

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #118
        0x15,
        "科洛丝",
        (
            "#1816F#5P#3S无论怎么说都可以！\x01",
            "……请亲口向她说明！\x02",
        )
    )

    Jump("loc_6438")

    label("loc_6438")

    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1044F#12P#40W啊………\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #120
        0x15,
        "科洛丝",
        (
            "#1873F#5P……这样…………\x02\x01",

            "#1818F才是男孩子对喜欢的人\x01",
            "应该尽的义务吧？\x02",
        )
    )

    Jump("loc_64F5")

    label("loc_64F5")

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        "#1043F#12P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #122
        0x102,
        (
            "#1053F#12P嗯……\x01",
            "你说的对。\x02\x03",

            "我……\x01",
            "………真没用。\x02\x03",

            "#1054F连这种理所当然的事\x01",
            "都没有注意到……\x02",
        )
    )

    Jump("loc_65C4")

    label("loc_65C4")

    CloseMessageWindow()

    NpcTalk(    #123
        0x15,
        "科洛丝",
        (
            "#1815F#5P呵呵，\x01",
            "这才像约修亚的风格嘛。\x02\x03",

            "#1870F……连你的这一点\x01",
            "我也非常欣赏呢………………\x02",
        )
    )

    Jump("loc_6641")

    label("loc_6641")

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        (
            "#1056F#12P………………\x02\x01",

            "#1048F拜托，饶过我吧……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #125
        0x15,
        "科洛丝",
        (
            "#1818F#5P呵呵……\x02\x03",

            "#1873F没事的，\x01",
            "艾丝蒂尔一定能明白你的用心。\x02\x03",

            "#1873F而且……\x01",
            "我想艾丝蒂尔一定会……\x02",
        )
    )

    Jump("loc_6715")

    label("loc_6715")

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x11, 21600, 14000, 70600, 90)
    OP_44(0x11, 0xFF)

    NpcTalk(    #126
        0x11,
        "活泼的声音",
        "约修亚～！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x11, 0x4)

    def lambda_678D():

        label("loc_678D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_678D")

    QueueWorkItem2(0x102, 2, lambda_678D)

    def lambda_679E():

        label("loc_679E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_679E")

    QueueWorkItem2(0x15, 2, lambda_679E)

    def lambda_67AF():
        OP_6D(31740, 14500, 71820, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_67AF)
    Sleep(1000)

    def lambda_67CC():
        OP_8E(0xFE, 0x7724, 0x36B0, 0x113C8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_67CC)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x47, 0x0)
    OP_8C(0x11, 45, 500)
    SetChrPos(0x15, 40010, 16000, 80500, 225)
    SetChrPos(0x102, 40620, 16000, 79280, 225)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #127
        0x11,
        (
            "#1001F啊，在这里呢。\x02\x03",

            "#1018F约修亚，看！\x01",
            "乔丝特的护目镜。\x02\x03",

            "#1029F嘿嘿，\x01",
            "这是我的战利品！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_68A6():
        OP_6D(39340, 16000, 80650, 2500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_68A6)

    def lambda_68BE():
        OP_67(0, 6320, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_68BE)

    def lambda_68D6():
        OP_6B(1920, 2500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_68D6)

    def lambda_68E6():
        OP_6C(353000, 2500)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_68E6)

    def lambda_68F6():
        OP_6E(375, 2500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_68F6)

    def lambda_6906():
        OP_8E(0xFE, 0x961E, 0x3E80, 0x12E8A, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6906)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x47, 0x0)
    OP_44(0x102, 0x2)
    OP_44(0x15, 0x2)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #128
        0x15,
        "科洛丝",
        (
            "#1872F#5P那个…………\x02\x03",

            "#1815F你能玩的这么开心，\x01",
            "真是太好了。\x02",
        )
    )

    Jump("loc_69C4")

    label("loc_69C4")

    CloseMessageWindow()

    ChrTalk(    #129
        0x102,
        (
            "#1052F#11P艾丝蒂尔，\x01",
            "一会儿可要还给人家哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        (
            "#1029F#6P嘿嘿～～～～………\x01",
            "要不要还呢～……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #131
        0x11,
        (
            "#1004F#6P……唔………\x01",
            "啊……哎………？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #132
        0x11,
        (
            "#1008F#6P那、那个……\x02\x03",

            "#1013F我、我说…………\x01",
            "科……科洛丝……？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #133
        0x15,
        "科洛丝",
        (
            "#1818F#5P嘻嘻……\x02\x03",

            "#1873F我差不多该回去了。\x02\x03",

            "#1872F……艾丝蒂尔。\x01",
            "我把约修亚还给你。\x02",
        )
    )

    Jump("loc_6B6B")

    label("loc_6B6B")

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        "#1004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_6B90():
        OP_6D(37990, 16000, 79260, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_6B90)

    def lambda_6BA8():
        OP_6C(5000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 3, lambda_6BA8)

    def lambda_6BB8():
        OP_6E(381, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_6BB8)

    def lambda_6BC8():

        label("loc_6BC8")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_6BC8")

    QueueWorkItem2(0x102, 2, lambda_6BC8)

    def lambda_6BD9():

        label("loc_6BD9")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_6BD9")

    QueueWorkItem2(0x11, 2, lambda_6BD9)

    def lambda_6BEA():
        OP_8E(0xFE, 0x8C78, 0x3E80, 0x12930, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6BEA)
    Sleep(3000)

    ChrTalk(    #135
        0x102,
        "#1035F#11P科洛丝……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x47, 0x0)
    OP_44(0x102, 0x2)
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x15, 45, 400)
    Sleep(300)

    ChrTalk(    #136
        0x102,
        (
            "#1043F#11P那个……\x02\x03",

            "我不知道\x01",
            "在这种场合下\x01",
            "该说些什么好……\x02",
        )
    )

    Jump("loc_6CB4")

    label("loc_6CB4")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #137
        0x102,
        (
            "#1053F#11P……不过还是要谢谢你。\x02\x03",

            "今天晚上，\x01",
            "能在这里和你谈话……\x02\x03",

            "#1041F……真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #138
        0x15,
        "科洛丝",
        "#1814F#6P………啊……………\x02",
    )

    Jump("loc_6D7F")

    label("loc_6D7F")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #139
        0x15,
        (
            "#1815F#6P呵呵……\x01",
            "不用客气。\x02\x03",

            "#1818F那么……\x01",
            "愿你们今晚玩的愉快。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 225, 400)
    Sleep(300)

    def lambda_6DEC():
        OP_6D(36090, 16000, 77140, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_6DEC)

    def lambda_6E04():
        OP_8E(0xFE, 0x6ACC, 0x36B0, 0x10734, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6E04)
    WaitChrThread(0x47, 0x0)
    Sleep(1500)

    def lambda_6E29():
        OP_6D(39790, 16000, 79910, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_6E29)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_44(0x11, 0x2)
    WaitChrThread(0x47, 0x0)
    OP_63(0x11)
    Sleep(300)

    ChrTalk(    #140
        0x11,
        (
            "#1008F#5P哎…………\x01",
            "………我、我说……………\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #141
        0x11,
        (
            "#1016F#6P喂，约修亚……\x02\x03",

            "#1013F你、你和科洛丝……\x01",
            "……那、那个…………………\x02\x03",

            "都、都说了些什么啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#1053F#11P嗯，有些事情……\x02\x03",

            "#1054F应该说，她是在给我打气吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x11,
        (
            "#1013F#6P是、是这样吗。\x01",
            "呼………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 500)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #144
        0x102,
        (
            "#1053F#11P（……这五年来，\x01",
            "  艾丝蒂尔一直相信着我。）\x02\x03",

            "（我也……………）\x02\x03",

            "#1041F（我也同样\x01",
            "  相信艾丝蒂尔……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #145
        0x11,
        "#1004F#5P#3S……打气？？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #146
        0x102,
        (
            "#1053F#11P……艾丝蒂尔。\x02\x03",

            "#1040F有件事……\x01",
            "我想告诉你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        "#1004F#6P………哎………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #148
        0x11,
        "#1006F#6P…………嗯，是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        "#1053F#11P嗯……其实呢………\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x7D0)
    OP_22(0x183, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_71DA():
        OP_8C(0xFE, 315, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_71DA)
    Sleep(100)
    OP_8C(0x11, 315, 500)

    ChrTalk(    #150
        0x11,
        "#1004F#12P啊………………\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_721A():
        OP_6D(39790, 21000, 79910, 3000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_721A)

    def lambda_7232():
        OP_67(0, 6570, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7232)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x47, 0x1)
    OP_44(0x47, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    OP_6D(33340, 15750, 73420, 0)
    OP_67(0, 8300, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x102, 0xFF)
    SetChrPos(0x15, 37740, 16000, 77820, 45)
    SetChrPos(0x102, 30240, 14000, 70320, 45)

    def lambda_72CC():
        OP_8E(0xFE, 0x8E58, 0x3E80, 0x12AE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72CC)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_72F1():
        OP_6D(37740, 16000, 77820, 4300)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_72F1)

    def lambda_7309():
        OP_67(0, 7300, -10000, 4300)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7309)
    WaitChrThread(0x102, 0x1)
    Sleep(300)

    ChrTalk(    #151
        0x102,
        (
            "#1043F……我说，科洛丝。\x02\x03",

            "你要和我说什么呢…………？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    NpcTalk(    #152
        0x15,
        "科洛丝",
        "#1817F………………………………\x02",
    )

    Jump("loc_739D")

    label("loc_739D")

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        (
            "#1043F那、那个…………\x02\x03",

            "要是有什么惹你生气的，\x01",
            "我向你道歉……\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)
    OP_8C(0x15, 225, 400)
    Sleep(500)

    NpcTalk(    #154
        0x15,
        "科洛丝",
        "#1817F……我…………\x02",
    )

    Jump("loc_743C")

    label("loc_743C")

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6B(2500, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #155
        0x15,
        "科洛丝",
        "#1812F我喜欢你。\x02",
    )

    Jump("loc_7479")

    label("loc_7479")

    CloseMessageWindow()
    OP_59()
    OP_1D(0x75)
    Sleep(500)

    ChrTalk(    #156
        0x102,
        (
            "#1042F…………………………\x02\x03",

            "#1044F哎……………？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_74C2():
        OP_6D(37600, 16000, 76620, 6000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_74C2)

    def lambda_74DA():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_74DA)

    def lambda_74F2():
        OP_6C(135000, 6000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_74F2)
    WaitChrThread(0x47, 0x0)

    NpcTalk(    #157
        0x15,
        "科洛丝",
        "#1812F…………………………\x02",
    )

    Jump("loc_7532")

    label("loc_7532")

    CloseMessageWindow()

    ChrTalk(    #158
        0x102,
        "#1044F那、那个…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #159
        0x15,
        "科洛丝",
        "#1812F…………………………\x02",
    )

    Jump("loc_7582")

    label("loc_7582")

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#1043F科洛……丝…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #161
        0x15,
        "科洛丝",
        "#1817F…………………………\x02",
    )

    Jump("loc_75D4")

    label("loc_75D4")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #162
        0x102,
        "#1035F对、对不起…………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #163
        0x15,
        "科洛丝",
        (
            "#1873F呵呵…………\x02\x03",

            "……好了，\x01",
            "你什么也不用说。\x02\x03",

            "#1815F我只是为了转换心情\x01",
            "才会这么说出来的。\x02",
        )
    )

    Jump("loc_7690")

    label("loc_7690")

    CloseMessageWindow()

    def lambda_7697():

        label("loc_7697")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_7697")

    QueueWorkItem2(0x102, 2, lambda_7697)
    OP_8C(0x15, 90, 400)
    Sleep(300)

    def lambda_76B4():
        OP_8E(0xFE, 0x9FEC, 0x3E80, 0x12FFC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_76B4)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    NpcTalk(    #164
        0x15,
        "科洛丝",
        "#1818F多美丽的星空啊……\x02",
    )

    Jump("loc_7702")

    label("loc_7702")

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        "#1057F那，这个…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #166
        0x102,
        (
            "#1043F你从何时开始……\x01",
            "……那个………………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #167
        0x15,
        "科洛丝",
        (
            "#1817F…………约修亚。\x02\x03",

            "如果，\x01",
            "比起艾丝蒂尔来，\x01",
            "你先遇到我的话……\x02\x03",

            "#1819F就不会和艾丝蒂尔……\x01",
            "……而是和我…………吗？\x02",
        )
    )

    Jump("loc_7813")

    label("loc_7813")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #168
        0x102,
        (
            "#1035F唔，那个嘛……\x02\x03",

            "#1043F…………我想不会的。\x02\x03",

            "……对不起，科洛丝。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #169
        0x15,
        "科洛丝",
        (
            "#1873F……这样就好了。\x02\x03",

            "想独占约修亚的心情\x01",
            "虽然不是假的……\x02\x03",

            "可是如果真的变成那样，\x01",
            "却不是我所希望的事情。\x02\x03",

            "#1815F……艾丝蒂尔和约修亚……\x01",
            "我果然还是……\x02\x03",

            "……喜欢你们两个人……\x02",
        )
    )

    Jump("loc_795A")

    label("loc_795A")

    CloseMessageWindow()
    OP_8C(0x15, 270, 400)
    Sleep(500)

    NpcTalk(    #170
        0x15,
        "科洛丝",
        (
            "#1810F……所以最后，\x01",
            "我想见识一下你为难时的表情。\x02\x03",

            "#1818F呵呵……………\x01",
            "刚才你的表情……\x02\x03",

            "……是至今为止最有趣的呢。\x02",
        )
    )

    Jump("loc_79F6")

    label("loc_79F6")

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#1044F#40W啊…………#500W\x01",
            "#40W……那个…………\x02\x03",

            "#1048F#20W……科洛丝，\x01",
            "你还真会捉弄人啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #172
        0x15,
        "科洛丝",
        (
            "#1811F呵呵，\x01",
            "已经很久没有\x01",
            "像现在这样热闹了。\x02",
        )
    )

    Jump("loc_7A9D")

    label("loc_7A9D")

    CloseMessageWindow()

    def lambda_7AA4():
        OP_6D(37960, 16000, 77020, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_7AA4)

    def lambda_7ABC():
        OP_67(0, 7300, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7ABC)

    def lambda_7AD4():
        OP_6C(90000, 2000)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_7AD4)

    def lambda_7AE4():
        OP_8E(0xFE, 0x936C, 0x3E80, 0x12FFC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7AE4)
    WaitChrThread(0x15, 0x1)
    OP_8C(0x15, 225, 300)
    Sleep(300)

    NpcTalk(    #173
        0x15,
        "科洛丝",
        (
            "#1817F#1P………………好了…………\x02\x03",

            "#1812F约修亚，\x01",
            "你到底在烦恼什么呢？\x02",
        )
    )

    Jump("loc_7B73")

    label("loc_7B73")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #174
        0x102,
        "#1044F…………哎！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #175
        0x15,
        "科洛丝",
        (
            "#1815F呼…………\x01",
            "这点事情我还是能看出来的。\x02\x03",

            "我本来感觉就比较敏锐，\x01",
            "刚才也……\x02\x03",

            "#1870F……在接受采访期间，\x01",
            "我一直在注视着\x01",
            "你的身影呢。\x02",
        )
    )

    Jump("loc_7C57")

    label("loc_7C57")

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        (
            "#1048F…………这个。\x02\x03",

            "#1056F那还真是\x01",
            "不好意思啊……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #177
        0x15,
        "科洛丝",
        (
            "#1815F啊、啊哈哈……\x02\x03",

            "#1812F……约修亚，\x01",
            "你有事情在瞒着大家吧。\x02\x03",

            "#1812F你又打算一个人\x01",
            "去做什么事情了？\x02",
        )
    )

    Jump("loc_7D1B")

    label("loc_7D1B")

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        (
            "#1035F…………………………\x02\x03",

            "#1052F唉，你真是太敏锐了……\x02\x03",

            "虽然艾丝蒂尔\x01",
            "有时也是这个样子…………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #179
        0x15,
        "科洛丝",
        (
            "#1818F呵呵，因为是女孩子嘛。\x02\x03",

            "#1812F……那么，\x01",
            "就赶快从实招来吧！\x02",
        )
    )

    Jump("loc_7DEB")

    label("loc_7DEB")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #180
        0x102,
        (
            "#1035F那倒不是能够\x01",
            "称得上烦恼的事……\x02\x03",

            "#1041F我…………这么说吧。\x01",
            "我打算下个月之前\x01",
            "离开利贝尔。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #181
        0x15,
        "科洛丝",
        (
            "#1814F哎…………！？\x02\x03",

            "#1812F为、为什么……呢？\x01",
            "明明已经恢复和平了啊……\x02",
        )
    )

    Jump("loc_7EF5")

    label("loc_7EF5")

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#1053F嗯，已经和平了呢。\x02\x03",

            "结社似乎也已经\x01",
            "完全撤离了利贝尔，\x01",
            "各地的重建工作也很顺利。\x02\x03",

            "#1041F……所以，\x01",
            "我想出去旅行。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0x2)
    OP_8C(0x102, 315, 200)
    Sleep(500)

    ChrTalk(    #183
        0x102,
        (
            "#1035F我…………\x01",
            "现在我已经可以把自己\x01",
            "当作一个真正的人来对待了。\x02\x03",

            "不再是坏掉的人偶。\x02\x03",

            "艾丝蒂尔，还有大家，\x01",
            "也都希望我能这样……\x02\x03",

            "#1041F……可是，\x01",
            "一旦成为了一个人，\x01",
            "我的心却隐隐作痛了。\x02\x03",

            "因为我曾经\x01",
            "犯下了那样多\x01",
            "惨不忍睹的罪行。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #184
        0x15,
        "科洛丝",
        "#1813F……啊………………\x02",
    )

    Jump("loc_80B8")

    label("loc_80B8")

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        (
            "#1035F……所以，为了偿还这一切。\x02\x03",

            "而且，为了真正意义上能够坚强起来。\x02\x03",

            "#1042F我决定接下来\x01",
            "到大陆各地去旅行。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #186
        0x15,
        "科洛丝",
        (
            "#1819F是、是这样啊……\x02\x03",

            "#1813F但是这样的话，\x01",
            "你和艾丝蒂尔……\x02",
        )
    )

    Jump("loc_81AF")

    label("loc_81AF")

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#1043F嗯，一段时间内…………\x02\x03",

            "不，应该是很长时间\x01",
            "都无法见面了。\x02\x03",

            "#1035F所以……………\x01",
            "……我不知道该怎么和艾丝蒂尔说………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)

    NpcTalk(    #188
        0x15,
        "科洛丝",
        (
            "#1817F………………唉。\x02\x03",

            "约修亚真是的……\x01",
            "你还是一点都没变呢。\x02",
        )
    )

    Jump("loc_82A3")

    label("loc_82A3")

    CloseMessageWindow()
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #189
        0x102,
        "#1044F哎…………？\x02",
    )

    CloseMessageWindow()

    def lambda_82CC():
        OP_8C(0xFE, 45, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_82CC)

    def lambda_82DA():
        OP_8E(0xFE, 0x91DC, 0x3E80, 0x12E6C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_82DA)
    WaitChrThread(0x15, 0x1)
    Fade(800)
    OP_6D(37740, 16000, 77820, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(800)

    NpcTalk(    #190
        0x15,
        "科洛丝",
        (
            "#1812F#5P……这种事情，\x01",
            "只能用自己的语言传达吧。\x02\x03",

            "你既然信任着艾丝蒂尔，\x01",
            "那就全部告诉她吧。\x02",
        )
    )

    Jump("loc_83B5")

    label("loc_83B5")

    CloseMessageWindow()

    NpcTalk(    #191
        0x15,
        "科洛丝",
        (
            "#1816F#5P无论怎么说都可以！\x01",
            "……请亲口向她说明！\x02",
        )
    )

    Jump("loc_83FD")

    label("loc_83FD")

    OP_7C(0x0, 0x96, 0xBB8, 0x96)
    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x15)
    Sleep(500)

    NpcTalk(    #192
        0x15,
        "科洛丝",
        (
            "#1812F#5P……这样…………\x01",
            "才是男孩子对喜欢的人\x01",
            "应该尽的义务吧？\x02",
        )
    )

    Jump("loc_8489")

    label("loc_8489")

    CloseMessageWindow()

    ChrTalk(    #193
        0x102,
        (
            "#1044F………………………………\x02\x03",

            "#1043F………………但是……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #194
        0x15,
        "科洛丝",
        (
            "#1873F#5P呵呵…………没关系的。\x01",
            "她一定会接受的。\x02\x03",

            "#1815F…………而且，\x01",
            "我想艾丝蒂尔一定会……\x02",
        )
    )

    Jump("loc_854E")

    label("loc_854E")

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x11, 21600, 14000, 70600, 90)
    OP_44(0x11, 0xFF)

    NpcTalk(    #195
        0x11,
        "活泼的声音",
        "约修亚～！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_85AA():

        label("loc_85AA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_85AA")

    QueueWorkItem2(0x102, 2, lambda_85AA)

    def lambda_85BB():
        OP_6D(31740, 14500, 71820, 2000)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_85BB)
    Sleep(1000)

    def lambda_85D8():
        OP_8E(0xFE, 0x7724, 0x3E80, 0x113C8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_85D8)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 45, 500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #196
        0x11,
        (
            "#1001F啊，在这里呢。\x02\x03",

            "#1018F……约修亚，看这个！\x01",
            "乔丝特的护目镜。\x02\x03",

            "#1029F嘿嘿，\x01",
            "这是我的战利品！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x15, 36500, 16000, 77620, 225)

    def lambda_869A():
        OP_6D(36900, 16000, 75800, 1500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_869A)

    def lambda_86B2():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_86B2)

    def lambda_86C2():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x47, 2, lambda_86C2)

    def lambda_86D2():
        OP_8E(0xFE, 0x8854, 0x3E80, 0x124F8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_86D2)
    WaitChrThread(0x11, 0x1)
    OP_44(0x102, 0x2)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #197
        0x15,
        "科洛丝",
        (
            "#1872F#1P那个…………\x02\x03",

            "#1815F艾丝蒂尔，\x01",
            "你也还是老样子啊。\x02",
        )
    )

    Jump("loc_8785")

    label("loc_8785")

    CloseMessageWindow()

    ChrTalk(    #198
        0x102,
        (
            "#1052F#1P艾丝蒂尔，\x01",
            "一会儿可要还给人家哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x11,
        (
            "#1029F嘿嘿～～～～………\x01",
            "要不要还呢～……？\x02\x03",

            "#1004F………………唔……\x01",
            "啊……哎………………？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #200
        0x11,
        (
            "#1008F那、那个……\x02\x03",

            "#1013F我、我说…………\x01",
            "科……科洛丝……？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #201
        0x15,
        "科洛丝",
        (
            "#1818F#1P呵呵…………\x02\x03",

            "……我差不多该回去了。\x02",
        )
    )

    Jump("loc_88C7")

    label("loc_88C7")

    CloseMessageWindow()

    def lambda_88CE():

        label("loc_88CE")

        TurnDirection(0xFE, 0x15, 500)
        OP_48()
        Jump("loc_88CE")

    QueueWorkItem2(0x11, 2, lambda_88CE)

    def lambda_88DF():
        OP_8E(0xFE, 0x878C, 0x3E80, 0x1282C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_88DF)
    WaitChrThread(0x15, 0x1)
    TurnDirection(0x102, 0x15, 500)

    ChrTalk(    #202
        0x102,
        "#1044F#1P啊，科洛丝……\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x15, 45, 400)
    Sleep(700)

    ChrTalk(    #203
        0x102,
        "#1041F#1P……谢谢你。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #204
        0x15,
        "科洛丝",
        "#1814F#4P……啊………………\x02",
    )

    Jump("loc_8996")

    label("loc_8996")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #205
        0x15,
        "#1873F#4P…………好的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 225, 400)
    Sleep(300)

    def lambda_89D2():
        OP_8E(0xFE, 0x701C, 0x36B0, 0x110BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_89D2)
    Sleep(2000)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x15, 0x1)
    OP_44(0x11, 0x2)
    SetChrPos(0x15, 11100, 12000, 57370, 270)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #206
        0x11,
        (
            "#1008F我、我说…………\x01",
            "………我、我说……………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #207
        0x11,
        (
            "#1008F喂，约修亚……\x02\x03",

            "#1013F你、你和科洛丝……\x01",
            "……那、那个…………………\x02\x03",

            "都、都说了些什么啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#1053F#1P嗯，有些事情……\x02\x03",

            "#1054F应该说是在给我打气吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        (
            "#1008F是、是这样吗。\x01",
            "呼………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 500)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #210
        0x102,
        (
            "#1035F#1P（……这五年来，\x01",
            "  艾丝蒂尔一直相信着我。）\x02\x03",

            "（我也……………）\x02\x03",

            "#1041F（我也同样\x01",
            "  相信艾丝蒂尔……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #211
        0x11,
        "#1004F哎？　……打气？？\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    ChrTalk(    #212
        0x102,
        (
            "#1040F#1P…………艾丝蒂尔。\x02\x03",

            "有件事我想告诉你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x11,
        "#1004F………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #214
        0x11,
        (
            "#1017F啊，嗯…………！\x02\x03",

            "………是……是什么呢…………？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x102,
        "#1053F#1P嗯，其实呢…………\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_22(0x183, 0x0, 0x64)
    Sleep(500)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(150)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_8D84():
        OP_8C(0xFE, 315, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D84)
    Sleep(150)
    OP_8C(0x11, 315, 300)
    Sleep(400)

    ChrTalk(    #216
        0x11,
        "#1011F啊………………\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_8DC0():
        OP_6D(36900, 17000, 75800, 1500)
        ExitThread()

    QueueWorkItem(0x47, 0, lambda_8DC0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4216 end

    def Function_21_8DEA(): pass

    label("Function_21_8DEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E2B")

    def lambda_8DF9():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DF9)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    Jump("Function_21_8DEA")

    label("loc_8E2B")

    Return()

    # Function_21_8DEA end

    def Function_22_8E2C(): pass

    label("Function_22_8E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E6D")

    def lambda_8E3B():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_8E3B)
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    Jump("Function_22_8E2C")

    label("loc_8E6D")

    Return()

    # Function_22_8E2C end

    def Function_23_8E6E(): pass

    label("Function_23_8E6E")

    OP_8E(0xFE, 0x965A, 0x3E80, 0x1331C, 0x5DC, 0x0)
    OP_8E(0xFE, 0xA122, 0x3E80, 0x13600, 0x5DC, 0x0)
    Return()

    # Function_23_8E6E end

    def Function_24_8E97(): pass

    label("Function_24_8E97")

    OP_8E(0xFE, 0x1BF8, 0x36B0, 0x13B82, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3D2C, 0x36B0, 0x13E70, 0x7D0, 0x0)
    Return()

    # Function_24_8E97 end

    def Function_25_8EC0(): pass

    label("Function_25_8EC0")

    EventBegin(0x0)
    OP_4A(0x17, 0)
    OP_4A(0x16, 0)
    OP_8C(0x17, 180, 0)
    OP_8C(0x16, 0, 0)
    Fade(1000)
    OP_6D(15940, 14000, 71760, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(268, 0)
    SetChrPos(0x102, 14110, 14000, 70910, 90)
    OP_0D()
    Sleep(300)

    ChrTalk(    #217
        0x17,
        (
            "#061F……那么，阿加特大哥哥\x01",
            "打算什么时候来呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x16,
        "#555F哎呀，那个嘛……\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_8FC2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8FC2)
    Sleep(150)
    OP_8C(0x16, 270, 400)
    Sleep(300)

    ChrTalk(    #219
        0x17,
        "#064F啊，是约修亚哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x16,
        (
            "#051F哟，约修亚，\x01",
            "你正在跟大家打招呼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        (
            "#1040F嗯，是啊。\x02\x03",

            "你们呢…………？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x17,
        (
            "#560F哎，那个…………\x02\x03",

            "我邀请了阿加特大哥哥\x01",
            "下次有机会到我家\x01",
            "来吃晚饭…………\x02\x03",

            "#067F到底定什么时候好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        (
            "#1040F对了……\x02\x03",

            "从埃尔赛尤号下来的时候\x01",
            "你们两个就在谈这个吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x16,
        (
            "#552F那、那个……\x01",
            "算是告别时的寒暄吧。\x02\x03",

            "……游击士可是很忙的。\x02\x03",

            "#053F还不知道实际上\x01",
            "有没有时间去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x17,
        (
            "#060F………………………………\x02\x03",

            "#562F我会一直等着的…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)
    OP_8C(0x16, 0, 500)
    Sleep(300)

    ChrTalk(    #226
        0x16,
        (
            "#055F呜………………\x02\x03",

            "我、我知道啦！\x01",
            "……啊，这个嘛…………\x02\x03",

            "#552F如果是月末的话……\x02\x03",

            "……我想星期五\x01",
            "应该能抽出空闲来……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x17, 180, 500)
    Sleep(300)

    ChrTalk(    #227
        0x17,
        (
            "#067F是真的吗？\x02\x03",

            "嘿嘿，那就说定了哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x16,
        "#555F哦，好………………\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 0)
    OP_4B(0x16, 0)
    OP_A2(0x2F9B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_9399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_9399")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_9399")

    EventEnd(0x0)
    Return()

    # Function_25_8EC0 end

    def Function_26_939C(): pass

    label("Function_26_939C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_942D")
    OP_8C(0x17, 180, 0)

    ChrTalk(    #229
        0x17,
        "#067F………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #230
        (
            "\x07\x05提妲拿出了小小的记事本，\x01",
            "在上面写着什么。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_9431")

    label("loc_942D")

    Call(0, 25)

    label("loc_9431")

    TalkEnd(0xFE)
    Return()

    # Function_26_939C end

    def Function_27_9435(): pass

    label("Function_27_9435")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_955B")
    OP_8C(0x16, 0, 0)
    OP_4A(0x17, 255)

    ChrTalk(    #231
        0x17,
        (
            "#061F对了，\x01",
            "阿加特大哥哥都喜欢吃什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x16,
        "#053F……能吃的东西都行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x17,
        "#065F………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #234
        0x16,
        "#551F啊～哎～对了…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x102,
        (
            "#1040F（……好像在商量事情。）\x02\x03",

            "（还是不要打扰了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x17, 255)
    Jump("loc_955F")

    label("loc_955B")

    Call(0, 25)

    label("loc_955F")

    TalkEnd(0xFE)
    Return()

    # Function_27_9435 end

    def Function_28_9563(): pass

    label("Function_28_9563")

    EventBegin(0x0)
    OP_4A(0x14, 0)
    OP_4A(0x13, 0)
    OP_8C(0x14, 180, 0)
    OP_8C(0x13, 270, 0)
    Fade(1000)
    OP_6D(-23910, 12000, 88040, 0)
    OP_67(0, 7210, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(276, 0)
    SetChrPos(0x102, -24200, 12000, 87770, 225)
    OP_0D()
    Sleep(300)

    ChrTalk(    #236
        0x102,
        (
            "#1040F#5P雪拉姐姐，奥利维尔。\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9611():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9611)
    Sleep(150)
    TurnDirection(0x14, 0x102, 400)
    Sleep(300)

    ChrTalk(    #237
        0x13,
        (
            "#027F……嗯？是约修亚啊。\x02\x03",

            "怎么样，要不要一起喝酒？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x14,
        (
            "#031F呵呵，\x01",
            "一起来举起这甜美的酒杯吧。\x02\x03",

            "今晚我会一直\x01",
            "陪着你到最后的。\x02\x03",

            "#037F直到你的眼眸摇动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        "#1048F#5P……抱歉，还是算了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x13,
        (
            "#025F什么啊，\x01",
            "今晚就陪我们一次吧。\x02\x03",

            "#021F……啊，对了。\x01",
            "就当成是为你祝贺\x01",
            "升任正游击士吧。\x02\x03",

            "因为上次\x01",
            "你都不在呢。\x02",
        )
    )

    Jump("loc_97AE")

    label("loc_97AE")

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #241
        0x102,
        (
            "#1035F#5P那个，雪拉姐姐……\x02\x03",

            "#1043F关于露茜奥拉的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x13,
        (
            "#524F呵呵………………\x02\x03",

            "#021F约修亚，\x01",
            "你怎么担心起\x01",
            "姐姐我来了。\x02\x03",

            "不用为此在意啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x14,
        (
            "#035F呵，雪拉君说的没错。\x02\x03",

            "大家在这次的事件中\x01",
            "都抱持着各种各样的想法。\x02\x03",

            "#030F不过，\x01",
            "至少今晚大家应该\x01",
            "痛痛快快地尽情享乐！\x02\x03",

            "#031F玩个尽兴吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x102,
        "#1054F#5P哈、哈啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x13,
        (
            "#025F……你不是一向\x01",
            "痛痛快快地尽情享乐吗。\x02\x03",

            "#027F不过说的也没错。\x02\x03",

            "#026F……对了，约修亚。\x01",
            "你可不要再一个人\x01",
            "独自行动了。\x02\x03",

            "#524F你不在的时候，\x01",
            "艾丝蒂尔的样子真的\x01",
            "很让人看不下去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x102,
        (
            "#1035F#5P………………是。\x02\x03",

            "#1040F别担心，\x01",
            "我不会再做那样的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x13,
        "#021F……是吗，那就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x14,
        (
            "#037F哦呵呵，约修亚君。\x01",
            "你那顺从的表情也很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 0)
    OP_8C(0x14, 180, 0)
    OP_4B(0x13, 0)
    OP_4B(0x14, 0)
    OP_A2(0x2F9C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_9B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_9B45")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_9B45")

    EventEnd(0x0)
    Return()

    # Function_28_9563 end

    def Function_29_9B48(): pass

    label("Function_29_9B48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_9C80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9BB5")

    ChrTalk(    #249
        0x13,
        (
            "#027F我也差不多该回\x01",
            "洛连特了。\x02\x03",

            "呵呵，下次说不定\x01",
            "就能把爱娜给灌醉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C7D")

    label("loc_9BB5")


    ChrTalk(    #250
        0x13,
        (
            "#522F……最近我不管喝多少\x01",
            "都不会感觉到醉。\x02\x03",

            "………………………………\x02\x03",

            "#520F嘿嘿，这样的话\x01",
            "说不定就能赢过爱娜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        (
            "#1048F（……雪拉姐姐，\x01",
            "  显然搞错了方针吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_9C7D")

    Jump("loc_9C84")

    label("loc_9C80")

    Call(0, 28)

    label("loc_9C84")

    TalkEnd(0xFE)
    Return()

    # Function_29_9B48 end

    def Function_30_9C88(): pass

    label("Function_30_9C88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_9E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9D7C")
    OP_8C(0x14, 180, 0)
    OP_4A(0x13, 255)

    ChrTalk(    #252
        0x14,
        (
            "#035F对了，雪拉君，\x01",
            "也许这是我神经过敏……\x02\x03",

            "#037F……不过你不觉得\x01",
            "喝得太快了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x13,
        "#026F……………………嗝……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #254
        0x14,
        (
            "#036F啊，哎……！？\x01",
            "比平时更厉害……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    Jump("loc_9E47")

    label("loc_9D7C")


    ChrTalk(    #255
        0x102,
        (
            "#1044F哎，奥利维尔，\x01",
            "你不回帝国没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x14,
        (
            "#030F嗯，啊啊…………\x02\x03",

            "#035F……是啊…………\x01",
            "现在享受祭典后的\x01",
            "余韵和残香才是最重要的。\x02\x03",

            "难得能出席这样\x01",
            "气氛和谐的宴会。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_9E47")

    Jump("loc_9E4E")

    label("loc_9E4A")

    Call(0, 28)

    label("loc_9E4E")

    TalkEnd(0xFE)
    Return()

    # Function_30_9C88 end

    def Function_31_9E52(): pass

    label("Function_31_9E52")

    EventBegin(0x0)
    OP_4A(0x1A, 0)
    OP_4A(0x11, 0)
    OP_8C(0x1A, 0, 0)
    OP_8C(0x11, 180, 0)
    Fade(1000)
    OP_6D(-6670, 12000, 58710, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, -6770, 12000, 57530, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #257
        0x1A,
        (
            "#1560F嘿，只有这种程度嘛。\x02\x03",

            "果然还是本姑娘\x01",
            "比较适合出席这样的宴会。\x02\x03",

            "#1561F不管怎么说，\x01",
            "我可是穿着真正的正装\x01",
            "涉足过社交界呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x11,
        (
            "#1009F#1P那、那算什么！\x02\x03",

            "正装什么的，\x01",
            "我也穿过！\x02\x03",

            "#1022F你这装正经的男人婆\x01",
            "才没有资格说我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x1A,
        "#1564F你、你说什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x102,
        (
            "#1048F#2P…………等、等一下你们两个。\x02\x03",

            "这里是公众场合，\x01",
            "要吵架的话还是到别的地方……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A060():
        TurnDirection(0xFE, 0x102, 600)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_A060)

    def lambda_A06E():
        TurnDirection(0xFE, 0x102, 600)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A06E)
    WaitChrThread(0x1A, 0x2)
    Sleep(400)

    ChrTalk(    #261
        0x1A,
        "#1564F#3S约修亚给我闭嘴！！#2S\x02",
    )


    ChrTalk(    #262
        0x11,
        "#1005F#3S#1P约修亚给我闭嘴！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()

    ChrTalk(    #263
        0x102,
        "#1052F#2P……是……………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1A, 0, 0)
    OP_8C(0x11, 180, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x11, 0)
    OP_A2(0x2F9D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_A169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_A169")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_A169")

    EventEnd(0x0)
    Return()

    # Function_31_9E52 end

    def Function_32_A16C(): pass

    label("Function_32_A16C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A1C8")
    OP_8C(0x1A, 0, 0)

    ChrTalk(    #264
        0x1A,
        (
            "#1560F哼哼，正好。\x02\x03",

            "既然你这么说那我们就来比试比试。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1CC")

    label("loc_A1C8")

    Call(0, 31)

    label("loc_A1CC")

    TalkEnd(0xFE)
    Return()

    # Function_32_A16C end

    def Function_33_A1D0(): pass

    label("Function_33_A1D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A233")
    OP_8C(0x11, 180, 0)

    ChrTalk(    #265
        0x11,
        (
            "#1028F哼～没问题…………\x02\x03",

            "你以为能胜过\x01",
            "我艾丝蒂尔大人吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A237")

    label("loc_A233")

    Call(0, 31)

    label("loc_A237")

    TalkEnd(0xFE)
    Return()

    # Function_33_A1D0 end

    def Function_34_A23B(): pass

    label("Function_34_A23B")

    EventBegin(0x0)
    OP_4A(0x18, 0)
    OP_8C(0x18, 270, 0)
    Fade(1000)
    OP_6D(9760, 12000, 65970, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 8640, 12000, 64269, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x18, 0x102, 400)
    Sleep(300)

    ChrTalk(    #266
        0x18,
        "#073F#1P哦，是约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x102,
        (
            "#1040F…………金大哥。\x02\x03",

            "重建工作\x01",
            "你也帮了很多忙呢。\x02\x03",

            "真是太谢谢你了。\x02",
        )
    )

    Jump("loc_A352")

    label("loc_A352")

    CloseMessageWindow()

    ChrTalk(    #268
        0x18,
        (
            "#071F#1P哈哈哈，没什么啦。\x02\x03",

            "这也算是身为游击士的\x01",
            "工作之一嘛。\x02\x03",

            "#070F……不过我也差不多\x01",
            "该回国去了。\x02\x03",

            "共和国的内政\x01",
            "现在也不能说是\x01",
            "十分安定……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 270, 0)
    OP_4B(0x18, 0)
    OP_A2(0x2FA0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_A454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_A454")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_A454")

    EventEnd(0x0)
    Return()

    # Function_34_A23B end

    def Function_35_A457(): pass

    label("Function_35_A457")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A52A")
    OP_8C(0x18, 270, 0)
    OP_4A(0x2B, 255)

    ChrTalk(    #269
        0x2B,
        (
            "#1110F对了，雾香小姐\x01",
            "没有来宴会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x18,
        (
            "#070F是啊，支部的接待员\x01",
            "都离不开工作岗位呢。\x02\x03",

            "#075F……不过，就算没有工作，\x01",
            "让她化妆出席宴会\x01",
            "也真是无法想像的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x2B, 255)
    Jump("loc_A52E")

    label("loc_A52A")

    Call(0, 34)

    label("loc_A52E")

    TalkEnd(0xFE)
    Return()

    # Function_35_A457 end

    def Function_36_A532(): pass

    label("Function_36_A532")

    EventBegin(0x0)
    OP_4A(0x1C, 0)
    OP_4A(0x1B, 0)
    OP_8C(0x1B, 270, 0)
    OP_8C(0x1C, 90, 0)
    Fade(500)
    OP_6D(8530, 12000, 54030, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    SetChrPos(0x102, 7590, 12000, 53660, 225)
    TurnDirection(0x1C, 0x102, 0)
    TurnDirection(0x1B, 0x102, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #271
        0x1B,
        (
            "#170F……啊啊，是约修亚吗。\x02\x03",

            "现在我正在和少校确认\x01",
            "『异变』后的受害状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1C,
        (
            "#270F……『利贝尔方舟』崩坏造成的\x01",
            "直接伤害似乎很小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x1B,
        (
            "#176F因为导力停止现象，\x01",
            "崩坏时没有船舶在\x01",
            "瓦雷利亚湖上遭到破坏。\x02\x03",

            "#170F虽然发生了小规模的海啸，\x01",
            "但几乎没有造成\x01",
            "什么人身伤害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#1040F#5P嗯，我和艾丝蒂尔\x01",
            "也在沿岸地区查看了一遍。\x02\x03",

            "只有一些观看崩坏现象的人们\x01",
            "以及几位钓鱼客被海潮\x01",
            "迎面打了一下而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x1C,
        (
            "#272F相对来说，导力停止现象\x01",
            "造成的混乱更为严重。\x02\x03",

            "#270F利贝尔在整个大陆\x01",
            "也是数一数二的导力技术大国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x1B,
        (
            "#178F因此反而\x01",
            "招来了灾害……吗。\x02\x03",

            "#176F……虽然『异变』已经过去，\x01",
            "但留下的课题也是十分重大的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 270, 0)
    OP_8C(0x1C, 90, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_A2(0x2F9E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_A8AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_A8AF")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_A8AF")

    EventEnd(0x0)
    Return()

    # Function_36_A532 end

    def Function_37_A8B2(): pass

    label("Function_37_A8B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_A94C")

    ChrTalk(    #277
        0x1B,
        (
            "#178F利贝尔正因为\x01",
            "导力技术广泛普及，\x01",
            "所以才造成了如此的混乱……\x02\x03",

            "#176F……『异变』已经过去，\x01",
            "但留下的课题却是十分重大的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A950")

    label("loc_A94C")

    Call(0, 36)

    label("loc_A950")

    TalkEnd(0xFE)
    Return()

    # Function_37_A8B2 end

    def Function_38_A954(): pass

    label("Function_38_A954")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_AA33")

    ChrTalk(    #278
        0x1C,
        (
            "#270F受到『导力停止现象』\x01",
            "影响的帝国南部的混乱也\x01",
            "已经逐步消散了……\x02\x03",

            "关于『利贝尔方舟』，\x01",
            "公众知道的情况仅限于\x01",
            "『神秘浮游物体』而已。\x02\x03",

            "#276F中央政府也陷入了混乱吗？\x01",
            "……或者是…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA37")

    label("loc_AA33")

    Call(0, 36)

    label("loc_AA37")

    TalkEnd(0xFE)
    Return()

    # Function_38_A954 end

    def Function_39_AA3B(): pass

    label("Function_39_AA3B")

    EventBegin(0x0)
    OP_4A(0x32, 0)
    OP_4A(0x33, 0)
    OP_8C(0x32, 180, 0)
    OP_8C(0x33, 270, 0)
    Fade(500)
    OP_6D(-5230, 12000, 67430, 0)
    OP_67(0, 7430, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    SetChrPos(0x102, -5230, 12000, 67430, 225)
    OP_8C(0x32, 90, 0)
    OP_8C(0x33, 0, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #279
        0x33,
        "#200F哟，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x102,
        (
            "#1040F多伦兄、吉尔兄。\x02\x03",

            "你们两位也接到招待了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x32,
        (
            "#190F是啊，不知道怎么回事，\x01",
            "我们也收到了请柬。\x02\x03",

            "难得受到邀请，\x01",
            "我们就急急忙忙赶来参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x102,
        (
            "#1054F怎么说好呢，\x01",
            "你们还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x33,
        (
            "#202F哈哈，是啊。\x02\x03",

            "#200F……多亏了女王陛下的恩赦，\x01",
            "给了我们光明正大前进的可能。\x02\x03",

            "也该是改过自新的时候了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x102,
        (
            "#1040F以前好像也听你们说过。\x02\x03",

            "记得是要开设运输公司对吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x33,
        (
            "#204F……其实也有很多\x01",
            "别的选择。\x02\x03",

            "#200F不过我们……\x01",
            "果然还是无法放弃\x01",
            "在天空中飞翔呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x32, 180, 0)
    OP_8C(0x33, 270, 0)
    OP_4B(0x32, 0)
    OP_4B(0x33, 0)
    OP_A2(0x2F9F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_AD55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_AD55")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_AD55")

    EventEnd(0x0)
    Return()

    # Function_39_AA3B end

    def Function_40_AD58(): pass

    label("Function_40_AD58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_ADFC")
    OP_8C(0x32, 180, 0)

    ChrTalk(    #286
        0x32,
        (
            "#198F（嚼嚼……）\x01",
            "当然我也不会反对啦。\x02\x03",

            "虽然生意上有很多\x01",
            "很难弄懂的事……\x02\x03",

            "#490F不过对于乔丝特来说\x01",
            "应该是件好事情吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE00")

    label("loc_ADFC")

    Call(0, 39)

    label("loc_AE00")

    TalkEnd(0xFE)
    Return()

    # Function_40_AD58 end

    def Function_41_AE04(): pass

    label("Function_41_AE04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_AEAD")

    ChrTalk(    #287
        0x33,
        (
            "#200F我们要靠自己振兴公司，\x01",
            "因此接纳了原来空贼团的手下们\x01",
            "作为员工。\x02\x03",

            "#203F现在面临的问题是\x01",
            "将公司做大需要的资金\x01",
            "以及是否能够提高收益……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEB1")

    label("loc_AEAD")

    Call(0, 39)

    label("loc_AEB1")

    TalkEnd(0xFE)
    Return()

    # Function_41_AE04 end

    def Function_42_AEB5(): pass

    label("Function_42_AEB5")

    EventBegin(0x0)
    OP_4A(0x10, 0)
    OP_8C(0x10, 270, 0)
    Fade(1000)
    OP_6D(3120, 12000, 65540, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 3060, 12000, 64830, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #288
        0x102,
        (
            "#1044F#11P…………凯文先生？\x02\x03",

            "原来你还留在\x01",
            "利贝尔啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 500)
    Sleep(300)

    ChrTalk(    #289
        0x10,
        (
            "#1062F#6P啊，\x01",
            "约修亚也来了吗。\x02\x03",

            "#1066F……怎么样，玩得开心吗？\x02\x03",

            "凭我的经验，这种场合不多\x01",
            "吃点的话，可是会后悔的哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFFFF)
    Sleep(500)

    ChrTalk(    #290
        0x102,
        (
            "#1035F#11P………凯文先生……\x01",
            "真是谢谢你了。\x02\x03",

            "如果你没有拜访\x01",
            "利贝尔的话，\x01",
            "………我……………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x10,
        (
            "#1840F#6P啊，别放在心上。\x02\x03",

            "我所做的只不过是\x01",
            "微不足道的小事而已。\x02\x03",

            "#1075F……看你的脸色不错，\x01",
            "应该没有留下后遗症。\x02\x03",

            "#1060F感谢什么的，\x01",
            "就一起忘掉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x102,
        (
            "#1043F#11P………………………………\x02\x03",

            "…………凯文先生，\x01",
            "难道你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x10,
        (
            "#1065F#6P…………约修亚。\x02\x03",

            "我也差不多\x01",
            "该回去了……\x02\x03",

            "#1840F希望以后还能再见面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x102,
        "#1054F#11P…………嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 0)
    OP_4B(0x10, 0)
    OP_A2(0x2FA1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_B27D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_B27D")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_B27D")

    EventEnd(0x0)
    Return()

    # Function_42_AEB5 end

    def Function_43_B280(): pass

    label("Function_43_B280")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_B2E7")
    OP_8C(0x10, 270, 0)

    ChrTalk(    #295
        0x10,
        (
            "#1064F啊，这里脊肉真的很好吃！\x02\x03",

            "#1846F唉～\x01",
            "真想打包回去啊～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2EB")

    label("loc_B2E7")

    Call(0, 42)

    label("loc_B2EB")

    TalkEnd(0xFE)
    Return()

    # Function_43_B280 end

    def Function_44_B2EF(): pass

    label("Function_44_B2EF")

    EventBegin(0x0)
    OP_4A(0x15, 0)
    OP_8C(0x15, 90, 0)
    OP_4A(0x35, 0)
    Fade(1000)
    OP_6D(13200, 12000, 59150, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    SetChrPos(0x102, 11770, 12000, 59360, 180)
    OP_0D()
    Sleep(300)

    ChrTalk(    #296
        0x15,
        (
            "#1872F……哎，让我发表意见吗？\x02\x03",

            "#1815F好、好的。\x01",
            "这………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x102,
        (
            "#1054F#1P（………好像正在接受采访。）\x02\x03",

            "（还是不要去打扰了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 90, 0)
    OP_4B(0x15, 0)
    OP_4B(0x35, 0)
    OP_A2(0x2FA2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_B453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_B453")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_B453")

    EventEnd(0x0)
    Return()

    # Function_44_B2EF end

    def Function_45_B456(): pass

    label("Function_45_B456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_B4C1")
    OP_8C(0x15, 90, 0)

    ChrTalk(    #298
        0x15,
        (
            "#1872F……哎，让我发表意见吗？\x02\x03",

            "#1815F好、好的。\x01",
            "那个嘛………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4C5")

    label("loc_B4C1")

    Call(0, 44)

    label("loc_B4C5")

    TalkEnd(0xFE)
    Return()

    # Function_45_B456 end

    def Function_46_B4C9(): pass

    label("Function_46_B4C9")

    EventBegin(0x0)
    OP_4A(0x31, 0)
    OP_8C(0x31, 270, 0)
    Fade(1000)
    OP_6D(-41100, 16000, 81610, 0)
    OP_67(0, 4535, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    SetChrPos(0x102, -41440, 16000, 80610, 270)
    OP_0D()
    Sleep(300)

    ChrTalk(    #299
        0x31,
        "#1125F……是约修亚啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x102,
        (
            "#1040F#2P父亲，您也来了。\x02\x03",

            "之前不是发来联络说\x01",
            "忙得抽不开身吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x31, 90, 400)
    Sleep(300)

    ChrTalk(    #301
        0x31,
        (
            "#1120F啊，的确是很忙。\x02\x03",

            "#1123F为了确保人民日常生活\x01",
            "而组织复兴物资的运输……\x02\x03",

            "这个国家要想回归平稳\x01",
            "还需要很长一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        (
            "#1040F#2P说起来……\x02\x03",

            "我和艾丝蒂尔在各处巡回时，\x01",
            "看到连小村庄都驻扎了王国军，\x01",
            "是为了缓解当地居民的不安吧。\x02\x03",

            "这种指示真像父亲的作风呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x31,
        (
            "#1125F这也只是做出\x01",
            "身在军队所能做到的事而已。\x02\x03",

            "虽然现在帝国和共和国的内政依然不透明，\x01",
            "王国军的重编工作也被打断……\x02\x03",

            "#1120F……不过，\x01",
            "弦也不能一直绷得太紧。\x02\x03",

            "约修亚，\x01",
            "今天你就好好休息一下吧。\x02",
        )
    )

    Jump("loc_B7CC")

    label("loc_B7CC")

    CloseMessageWindow()

    ChrTalk(    #304
        0x102,
        (
            "#1054F#2P父亲您才应该\x01",
            "适当休息一下吧？\x02\x03",

            "艾丝蒂尔也很担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x31,
        (
            "#1121F哈哈，不用担心我。\x02\x03",

            "看我这个样子，\x01",
            "现在不是正在休息吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x31, 270, 0)
    OP_4B(0x31, 0)
    OP_A2(0x2FA3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 3)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 4)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 6)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 7)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 0)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 1)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 2)), scpexpr(EXPR_END)), "loc_B8C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_B8C0")
    OP_B2(0x1, 0x0, 0x80)

    label("loc_B8C0")

    EventEnd(0x0)
    Return()

    # Function_46_B4C9 end

    def Function_47_B8C3(): pass

    label("Function_47_B8C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 3)), scpexpr(EXPR_END)), "loc_B92F")

    ChrTalk(    #306
        0x31,
        (
            "#1120F……不用担心。\x02\x03",

            "我会让你们分担一些力所能及的工作，\x01",
            "让自己休息一下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B933")

    label("loc_B92F")

    Call(0, 46)

    label("loc_B933")

    TalkEnd(0xFE)
    Return()

    # Function_47_B8C3 end

    def Function_48_B937(): pass

    label("Function_48_B937")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_B9D8")

    ChrTalk(    #307
        0x25,
        (
            "#090F呵呵，\x01",
            "刚才的讲话气氛太严肃了。\x02\x03",

            "今天晚上\x01",
            "希望大家能够\x01",
            "开心地放松一下。\x02\x03",

            "所以请一定要\x01",
            "好好享受一下宴会。\x02",
        )
    )

    Jump("loc_B9D4")

    label("loc_B9D4")

    CloseMessageWindow()
    Jump("loc_BDF1")

    label("loc_B9D8")


    ChrTalk(    #308
        0x102,
        (
            "#1040F……女王陛下。\x02\x03",

            "今天能够受到招待，\x01",
            "谢谢您。\x02",
        )
    )

    Jump("loc_BA28")

    label("loc_BA28")

    CloseMessageWindow()

    ChrTalk(    #309
        0x25,
        (
            "#090F约修亚，\x01",
            "谢谢你来参加宴会。\x02\x03",

            "我一直期待着\x01",
            "再次与你见面呢。\x02\x03",

            "听说你和艾丝蒂尔\x01",
            "在利贝尔各地奔波，\x01",
            "到处帮忙重建工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x102,
        (
            "#1035F是的，\x01",
            "无论如何我们也想亲眼确认一下情况。\x02\x03",

            "#1035F……不过，\x01",
            "看过之后我终于感到安心了。\x02\x03",

            "#1040F人啊，真的是很坚强的生物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x25,
        (
            "#094F……你说的没错。\x02\x03",

            "我已经统治了\x01",
            "这个国家四十年，\x01",
            "这次依然让我感到前所未有的吃惊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x25, 270, 400)
    Sleep(300)

    ChrTalk(    #312
        0x25,
        (
            "#090F……利贝尔是个小国。\x02\x03",

            "在大家的眼里，\x01",
            "支持着这个国家的是\x01",
            "我的治理手段和导力技术……\x02\x03",

            "但解决了这次『异变』\x01",
            "以及十年前『百日战役』的，\x01",
            "并不是这些力量。\x02\x03",

            "#094F真正支撑这个小国的，\x01",
            "……应该是住在这里的\x01",
            "每个人生存下去的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x102,
        "#1042F……人们……生存下去的力量……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x25,
        "#090F……嗯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x102, 400)
    Sleep(300)

    ChrTalk(    #315
        0x25,
        (
            "#090F约修亚，\x01",
            "请把利贝尔当作第二故乡。\x02\x03",

            "你生存的力量\x01",
            "也一定能够成为这个国家的支柱。\x02\x03",

            "我作为女王也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x102,
        (
            "#1040F………………是。\x02\x03",

            "#1053F谢谢您，陛下……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_BDF1")

    TalkEnd(0xFE)
    Return()

    # Function_48_B937 end

    def Function_49_BDF5(): pass

    label("Function_49_BDF5")

    TalkBegin(0xFE)
    OP_8C(0x35, 270, 0)

    ChrTalk(    #317
        0x35,
        (
            "#147F是的，希望您能够说一些\x01",
            "对这次『异变』终止的祝贺的话……\x02\x03",

            "不是正式的讲话形式，\x01",
            "而是以『轻松的王太女殿下』\x01",
            "这样的形象……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_BDF5 end

    def Function_50_BE93(): pass

    label("Function_50_BE93")

    TalkBegin(0xFE)
    OP_8C(0x36, 270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 2)), scpexpr(EXPR_END)), "loc_BF0D")

    ChrTalk(    #318
        0xFE,
        (
            "#156F奈尔前辈说\x01",
            "让我不要随便行动……\x02\x03",

            "#155F唉，这样的话\x01",
            "就只好用饮料来充饥了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF5A")

    label("loc_BF0D")


    ChrTalk(    #319
        0xFE,
        (
            "#154F咕咕～……\x02\x03",

            "女、女佣小姐……\x01",
            "快把料理端过来吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x32)

    label("loc_BF5A")

    TalkEnd(0xFE)
    Return()

    # Function_50_BE93 end

    def Function_51_BF5E(): pass

    label("Function_51_BF5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 7)), scpexpr(EXPR_END)), "loc_BFF7")

    ChrTalk(    #320
        0x34,
        (
            "#104F…………唉，\x01",
            "没想到那东西竟然崩坏了。\x02\x03",

            "如果再多一个小时的话，\x01",
            "就可以取一些样本了……\x02\x03",

            "唔，现在遗憾也没用了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C19F")

    label("loc_BFF7")


    ChrTalk(    #321
        0x34,
        (
            "#101F哦哦，是约修亚。\x02\x03",

            "自从『利贝尔方舟』回来后\x01",
            "就没有见过面了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x102,
        (
            "#1040F拉赛尔博士，\x01",
            "很久不见了。\x02\x03",

            "对了，\x01",
            "据说你们计划将『利贝尔方舟』\x01",
            "打捞上来进行调查……\x02",
        )
    )

    Jump("loc_C0C2")

    label("loc_C0C2")

    CloseMessageWindow()

    ChrTalk(    #323
        0x34,
        (
            "#100F嗯，和军队一起。\x02\x03",

            "……不过瓦雷利亚湖的水\x01",
            "有相当的深度。\x02\x03",

            "虽然要调查，\x01",
            "但也不能随意地打捞残骸。\x02\x03",

            "还是用声纳\x01",
            "先绘制出湖底地图比较好……\x02\x03",

            "#104F唔，\x01",
            "看来会花很长时间呢。\x02",
        )
    )

    Jump("loc_C19B")

    label("loc_C19B")

    CloseMessageWindow()
    OP_A2(0x27)

    label("loc_C19F")

    TalkEnd(0xFE)
    Return()

    # Function_51_BF5E end

    def Function_52_C1A3(): pass

    label("Function_52_C1A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_C229")

    ChrTalk(    #324
        0x20,
        (
            "#600F呼，总算能放下心来了。\x02\x03",

            "约修亚，\x01",
            "你们也赶快回洛连特吧。\x02\x03",

            "大家都在担心你们呢。\x02",
        )
    )

    Jump("loc_C225")

    label("loc_C225")

    CloseMessageWindow()
    Jump("loc_C409")

    label("loc_C229")


    ChrTalk(    #325
        0x20,
        (
            "#600F哦哦，是约修亚。\x01",
            "很久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x102,
        (
            "#1040F克劳斯市长，\x01",
            "您也来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x20,
        (
            "#600F是啊，\x01",
            "各都市的市长都被请来了。\x02\x03",

            "我一点力也没有出，\x01",
            "却和大家一样被请过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x102,
        (
            "#1035F……没有的事，\x01",
            "听说送到柏斯和格兰赛尔的救援粮食\x01",
            "就是克劳斯市长您下的指示呢。\x02\x03",

            "#1040F尤其是曾经陷入\x01",
            "那种情况的格兰赛尔。\x02\x03",

            "大家都得到了很大鼓舞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x20,
        (
            "#602F是、是吗…………\x02\x03",

            "#603F呼，那么我就放心了。\x02\x03",

            "#600F约修亚，\x01",
            "谢谢你告诉我。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_C409")

    TalkEnd(0xFE)
    Return()

    # Function_52_C1A3 end

    def Function_53_C40D(): pass

    label("Function_53_C40D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_C4AD")

    ChrTalk(    #330
        0x28,
        (
            "#720F公爵大人自从那天之后，\x01",
            "也变得十分积极了。\x02\x03",

            "一想到这点，\x01",
            "我就觉得之前的付出没有白费。\x02\x03",

            "现在有一种\x01",
            "放下了重担的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C63C")

    label("loc_C4AD")

    OP_8C(0x28, 180, 0)
    OP_62(0x28, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x28, 0x102, 500)
    Sleep(300)

    ChrTalk(    #331
        0x28,
        (
            "#720F哦哦，是约修亚。\x02\x03",

            "你们能在百忙之中抽出时间光临，\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x102,
        (
            "#1040F菲利普先生，\x01",
            "您的伤已经没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x28,
        (
            "#720F嗯，没事了。\x02\x03",

            "不过我真的是老了。\x01",
            "上次的确有点勉强。\x02\x03",

            "现在我更觉得，\x01",
            "如果再年轻三十年就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x102,
        (
            "#1043F（三十年前的菲利普先生……）\x02\x03",

            "#1035F（……不行，想象不出来。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_C63C")

    TalkEnd(0xFE)
    Return()

    # Function_53_C40D end

    def Function_54_C640(): pass

    label("Function_54_C640")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_C6A6")

    ChrTalk(    #335
        0x29,
        (
            "#710F今天是陛下举办的\x01",
            "祝贺宴会。\x02\x03",

            "请务必要\x01",
            "好好放松一下。\x02",
        )
    )

    Jump("loc_C6A2")

    label("loc_C6A2")

    CloseMessageWindow()
    Jump("loc_C732")

    label("loc_C6A6")


    ChrTalk(    #336
        0x29,
        (
            "#710F约修亚，\x01",
            "今天的宴会\x01",
            "过得还愉快吧。\x02\x03",

            "#713F今天是陛下举办的\x01",
            "庆祝宴会。\x02\x03",

            "请务必要\x01",
            "好好放松一下。\x02",
        )
    )

    Jump("loc_C72E")

    label("loc_C72E")

    CloseMessageWindow()
    OP_A2(0x18)

    label("loc_C732")

    TalkEnd(0xFE)
    Return()

    # Function_54_C640 end

    def Function_55_C736(): pass

    label("Function_55_C736")

    TalkBegin(0xFE)
    OP_8C(0x22, 270, 0)

    ChrTalk(    #337
        0x22,
        (
            "#780F不，\x01",
            "这边并没有受到重大损害。\x02\x03",

            "学生们也都\x01",
            "恢复了愉快的心情。\x02",
        )
    )

    Jump("loc_C79A")

    label("loc_C79A")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_55_C736 end

    def Function_56_C79F(): pass

    label("Function_56_C79F")

    TalkBegin(0xFE)
    OP_8C(0x21, 90, 0)

    ChrTalk(    #338
        0x21,
        (
            "#615F校长，\x01",
            "我听说学院曾经被占领过……\x02\x03",

            "#618F一听到这件事，\x01",
            "我就十分担心…………\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_56_C79F end

    def Function_57_C811(): pass

    label("Function_57_C811")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_C8D1")

    ChrTalk(    #339
        0x24,
        (
            "#620F我每次一不注意，\x01",
            "小姐就会勉强自己。\x01",
            "所以让她来这里适当休息一下。\x02\x03",

            "当柏斯的情况告一段落后，\x01",
            "我会再给小姐好好\x01",
            "安排一段假期的。\x02\x03",

            "#621F……请不用担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1F")

    label("loc_C8D1")


    ChrTalk(    #340
        0x24,
        (
            "#620F……约修亚，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        (
            "#1040F莉拉小姐，\x01",
            "你还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x24,
        (
            "#621F嗯，我倒是没什么。\x02\x03",

            "#620F……不过小姐前几天\x01",
            "却由于太过劳累而倒下了。\x02\x03",

            "所以我强制让她\x01",
            "休息一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x102,
        "#1044F是、是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x24,
        (
            "#620F为了早日重新工作，\x01",
            "现在正在休养中。\x02\x03",

            "……请不要担心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)

    label("loc_CA1F")

    TalkEnd(0xFE)
    Return()

    # Function_57_C811 end

    def Function_58_CA23(): pass

    label("Function_58_CA23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_CAE6")

    ChrTalk(    #345
        0x23,
        (
            "#803F…………不过，\x01",
            "地下导力工厂的\x01",
            "生产率才恢复不到２８％……\x02\x03",

            "还有卡佩尔的系统重建\x01",
            "以及埃尔赛尤号的\x01",
            "全面检查…………\x02\x03",

            "#806F唉……\x01",
            "剩下的工作还有很多啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBAA")

    label("loc_CAE6")


    ChrTalk(    #346
        0x23,
        (
            "#806F呼，\x01",
            "这阵混乱终于得到解决了……\x02\x03",

            "#803F嗯，只要人们有耐心，\x01",
            "女神一定会向我们\x01",
            "伸出援助之手的。\x02\x03",

            "（流泪）………………\x02",
        )
    )

    Jump("loc_CB7D")

    label("loc_CB7D")

    CloseMessageWindow()

    ChrTalk(    #347
        0x102,
        "#1035F（玛多克先生…………）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_CBAA")

    TalkEnd(0xFE)
    Return()

    # Function_58_CA23 end

    def Function_59_CBAE(): pass

    label("Function_59_CBAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 4)), scpexpr(EXPR_END)), "loc_CC29")

    ChrTalk(    #348
        0xFE,
        (
            "我原来是实业家，\x01",
            "也曾出席过各种宴会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        (
            "但像今天这样和这么多著名人士同席\x01",
            "还是第一次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCE6")

    label("loc_CC29")


    ChrTalk(    #350
        0xFE,
        "哎呀，真是豪华的宴会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "看看各位来宾的身份就知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "我原来是实业家，\x01",
            "也曾出席过各种宴会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "但像今天这样和这么多著名人士同席\x01",
            "还是第一次。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2C)

    label("loc_CCE6")

    TalkEnd(0xFE)
    Return()

    # Function_59_CBAE end

    def Function_60_CCEA(): pass

    label("Function_60_CCEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_CD75")

    ChrTalk(    #354
        0x1E,
        (
            "#703F话说回来……\x01",
            "在浮游都市开始崩坏的时候，\x01",
            "我也毫不犹豫地开始向女神祈祷。\x02\x03",

            "#701F结果你们真的平安回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF4C")

    label("loc_CD75")


    ChrTalk(    #355
        0x1E,
        (
            "#701F……是约修亚吗。\x02\x03",

            "多亏了你们，才能阻止『异变』\x01",
            "以及『结社』的阴谋。\x02\x03",

            "我也要再次\x01",
            "向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        (
            "#1040F不，您言重了。\x02\x03",

            "如果只凭我们，\x01",
            "是无法登上『利贝尔方舟』的。\x02\x03",

            "#1041F也多亏了希德中校、\x01",
            "理查德先生以及克鲁茨前辈等人\x01",
            "在地面上的作战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x1E,
        (
            "#701F呵呵，的确任何问题\x01",
            "都不能靠某人一己之力完成呢。\x02\x03",

            "不过从我个人来说，\x01",
            "还是要向你们表示感谢。\x02\x03",

            "正因为相信你们能够成功，\x01",
            "所以我们才能够\x01",
            "放手去作战。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_CF4C")

    TalkEnd(0xFE)
    Return()

    # Function_60_CCEA end

    def Function_61_CF50(): pass

    label("Function_61_CF50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 3)), scpexpr(EXPR_END)), "loc_CFAB")

    ChrTalk(    #358
        0x30,
        (
            "#163F在各方面都受到了\x01",
            "你们游击士的帮助呢。\x02\x03",

            "总之先谢谢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D073")

    label("loc_CFAB")


    ChrTalk(    #359
        0x30,
        (
            "#160F嗯……是你啊。\x02\x03",

            "不光是对付『异变』\x01",
            "连重建工作也受到了你们的帮助。\x02\x03",

            "#163F总之先谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x102,
        (
            "#1044F您客气了。\x01",
            "（哎，真是意外的反应……\x01",
            "  ……发生过什么事吗。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x23)

    label("loc_D073")

    TalkEnd(0xFE)
    Return()

    # Function_61_CF50 end

    def Function_62_D077(): pass

    label("Function_62_D077")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 7)), scpexpr(EXPR_END)), "loc_D116")

    ChrTalk(    #361
        0x2C,
        (
            "#760F其它支部的接待员\x01",
            "都忙于各自的工作呢。\x02\x03",

            "#765F我本来还想趁大家集中起来\x01",
            "开会交换一下情报……\x02\x03",

            "#760F以后有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D23E")

    label("loc_D116")


    ChrTalk(    #362
        0x102,
        (
            "#1040F艾南先生，很久不见了。\x02\x03",

            "今天是作为游击士协会的\x01",
            "代表来参加宴会的吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x2C,
        (
            "#760F嗯，其它支部的接待员\x01",
            "都忙于各自的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x102,
        (
            "#1054F是这样啊……\x01",
            "有点遗憾呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x2C,
        (
            "#765F嗯，我本来还想这是大家\x01",
            "交换情报的好机会呢……\x02\x03",

            "#760F以后有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1F)

    label("loc_D23E")

    TalkEnd(0xFE)
    Return()

    # Function_62_D077 end

    def Function_63_D242(): pass

    label("Function_63_D242")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_END)), "loc_D2DF")

    ChrTalk(    #366
        0x2D,
        (
            "#843F……不过，\x01",
            "我的修行还远远不够啊。\x02\x03",

            "还是抽时间进行一次\x01",
            "正式的修炼吧……\x02\x03",

            "#840F等到情况稳定之后\x01",
            "去和艾南商量一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D685")

    label("loc_D2DF")


    ChrTalk(    #367
        0x2D,
        (
            "#840F啊，是约修亚。\x02\x03",

            "这两个星期辛苦你了。\x02\x03",

            "你们关于各地的损害报告\x01",
            "对人员调度起了很大作用。\x02\x03",

            "谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x102,
        (
            "#1040F啊，没什么…………\x02\x03",

            "#1035F…………克鲁茨前辈。\x01",
            "关于我的游击士资格……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #369
        0x102,
        (
            "#1043F……可能你已经知道了，\x01",
            "我的力量本来是由\x01",
            "『结社』给予的。\x02\x03",

            "并且我曾经用那种力量\x01",
            "犯了很多重大的罪行。\x02\x03",

            "所以我觉得像自己这样的人\x01",
            "不能再称为游击士………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x2D,
        (
            "#843F约修亚，我呢……\x02\x03",

            "我认为力量从来都不是\x01",
            "最重要的东西。\x02\x03",

            "所以人们才能够\x01",
            "控制并使用它。\x02\x03",

            "#842F……我说的没错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x102,
        "#1044F………………没、没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x2D,
        (
            "#845F……那么，\x01",
            "我们两个有什么不一样吗。\x02\x03",

            "认识到自己还远未成熟，\x01",
            "为了信念而持续发挥着力量，\x01",
            "这样的我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x102,
        (
            "#1054F……是啊…………\x02\x03",

            "虽然没什么自信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x2D,
        (
            "#841F呵呵，只要努力就好。\x02\x03",

            "#840F而且，就我本人看来……\x02\x03",

            "你是一位十分优秀的游击士。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)

    label("loc_D685")

    TalkEnd(0xFE)
    Return()

    # Function_63_D242 end

    def Function_64_D689(): pass

    label("Function_64_D689")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 1)), scpexpr(EXPR_END)), "loc_D6EA")

    ChrTalk(    #375
        0x2E,
        (
            "#820F……说起来那边的两个人，\x01",
            "真是精力旺盛呢。\x02\x03",

            "总是这个样子吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D760")

    label("loc_D6EA")


    ChrTalk(    #376
        0x2E,
        (
            "#821F嘿嘿，\x01",
            "之前到处奔波帮忙，\x01",
            "一直累得要命……\x02\x03",

            "#823F终于可以休息一下了。\x01",
            "（嚼嚼………………）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x21)

    label("loc_D760")

    TalkEnd(0xFE)
    Return()

    # Function_64_D689 end

    def Function_65_D764(): pass

    label("Function_65_D764")

    TalkBegin(0xFE)

    ChrTalk(    #377
        0x2F,
        (
            "#835F哎呀，那两个人还真是小孩子。\x02\x03",

            "是不是因为天下太平了，\x01",
            "所以开始得意忘形了呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_65_D764 end

    def Function_66_D7CF(): pass

    label("Function_66_D7CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_D940")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_D82A")

    ChrTalk(    #378
        0x19,
        (
            "#811F嗯，一定会很适合的。\x02\x03",

            "之后一定要找个机会试试！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D93D")

    label("loc_D82A")

    OP_8C(0x19, 270, 0)

    ChrTalk(    #379
        0x19,
        (
            "#818F嗯，就这样吧。\x02\x03",

            "让乔丝特戴上红色的耳环，\x01",
            "再加上小巧的发带，\x01",
            "而艾丝蒂尔就把头发放下来……\x02\x03",

            "这样她们两个人\x01",
            "一定会和白色的裙子\x01",
            "十分相称的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x102, 500)
    Sleep(300)

    ChrTalk(    #380
        0x19,
        "#816F约修亚，你觉得怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x102,
        "#1048F突然问我，我也不知道……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_D93D")

    Jump("loc_D9D3")

    label("loc_D940")


    ChrTalk(    #382
        0x19,
        (
            "#814F哎，\x01",
            "乔丝特原来是贵族出身啊。\x02\x03",

            "我本来以为帝国的贵族\x01",
            "都是些可怕的人……\x02\x03",

            "#1311F嘿嘿，\x01",
            "没想到有这么可爱的人呢。\x02",
        )
    )

    Jump("loc_D9D2")

    label("loc_D9D2")

    CloseMessageWindow()

    label("loc_D9D3")

    TalkEnd(0xFE)
    Return()

    # Function_66_D7CF end

    def Function_67_D9D7(): pass

    label("Function_67_D9D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_DA77")

    ChrTalk(    #383
        0x2B,
        (
            "#1110F『导力停止现象』\x01",
            "以及帝国的蒸汽战车部队……\x02\x03",

            "共和国的议会\x01",
            "也一定在议论纷纷吧。\x02\x03",

            "要收拾局面，\x01",
            "还需要花费\x01",
            "很多时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB68")

    label("loc_DA77")


    ChrTalk(    #384
        0x2B,
        (
            "#1111F庆祝会吗…………\x02\x03",

            "终于切身体会到了\x01",
            "重归和平的感受呢。\x02\x03",

            "#1113F话说回来，\x01",
            "在『异变』中的应对措施\x01",
            "以及各地的重建指示……\x02\x03",

            "现在我更加佩服\x01",
            "艾莉茜雅女王的手腕了。\x02\x03",

            "在共和国肯定\x01",
            "无法做到这样的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_DB68")

    TalkEnd(0xFE)
    Return()

    # Function_67_D9D7 end

    def Function_68_DB6C(): pass

    label("Function_68_DB6C")

    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    TurnDirection(0x26, 0x102, 0)
    TurnDirection(0x27, 0x102, 0)
    Sleep(300)

    ChrTalk(    #385
        0x26,
        "#221F哦，我等你很久了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x102,
        "#1044F#2P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x27,
        (
            "#1101F哦……\x02\x03",

            "那么，\x01",
            "这就是刚才所说的？\x02",
        )
    )

    Jump("loc_DC0C")

    label("loc_DC0C")

    CloseMessageWindow()

    ChrTalk(    #388
        0x26,
        (
            "#225F是的，他就是约修亚。\x02\x03",

            "#220F我正在向大使讲述\x01",
            "你们的活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x27,
        (
            "#1100F很荣幸见到你。\x02\x03",

            "我是驻利贝尔大使\x01",
            "达维尔·克莱纳赫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x102,
        "#1054F#2P啊，您好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x27,
        (
            "#1102F乘上浮游都市的那一段，\x01",
            "我光是听着就觉得热血沸腾呢。\x02\x03",

            "明知道那可能是单程机票，\x01",
            "却放开恋人的手\x01",
            "参加特攻作战……\x02\x03",

            "#1100F哎呀，你们这样的年轻人\x01",
            "真的是国家的宝藏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x102,
        (
            "#1049F#2P谢、谢谢您的夸奖。\x02\x03",

            "（……到底都向他\x01",
            "  说了些什么呢…………）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x26, 180, 0)
    OP_8C(0x27, 0, 0)
    OP_4B(0x26, 0)
    OP_4B(0x27, 0)
    Return()

    # Function_68_DB6C end

    def Function_69_DE01(): pass

    label("Function_69_DE01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_DE48")
    OP_8C(0x26, 180, 0)

    ChrTalk(    #393
        0x26,
        (
            "#225F然后在这里，\x01",
            "奇迹般再会的两人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE52")

    label("loc_DE48")

    Call(0, 68)
    OP_A2(0x15)
    OP_A2(0x16)

    label("loc_DE52")

    TalkEnd(0xFE)
    Return()

    # Function_69_DE01 end

    def Function_70_DE56(): pass

    label("Function_70_DE56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_DEE9")

    ChrTalk(    #394
        0x27,
        (
            "#1102F年轻人的精神真是值得赞叹……\x01",
            "我光是听着就觉得热血沸腾呢。\x02\x03",

            "#1100F哎呀，你们这样的年轻人\x01",
            "真的是国家的宝藏啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEFA")

    label("loc_DEE9")

    OP_8C(0xFE, 0, 0)
    Call(0, 68)
    OP_A2(0x15)
    OP_A2(0x16)

    label("loc_DEFA")

    TalkEnd(0xFE)
    Return()

    # Function_70_DE56 end

    def Function_71_DEFE(): pass

    label("Function_71_DEFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_DF76")

    ChrTalk(    #395
        0x1D,
        (
            "#115F由于卡西乌斯准将的争取，\x01",
            "我也受到了恩赦……\x02\x03",

            "……该是我为自己\x01",
            "做个决断的时候了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1BD")

    label("loc_DF76")


    ChrTalk(    #396
        0x102,
        (
            "#1040F理查德先生……\x01",
            "您也来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x1D,
        (
            "#110F嗯……多亏了准将呢。\x02\x03",

            "我已经得到了\x01",
            "陛下正式的恩赦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x102,
        (
            "#1040F因为有阻止『结社』\x01",
            "袭击王都的功绩嘛。\x02\x03",

            "恭喜您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x1D,
        (
            "#115F……不，\x01",
            "我还是觉得实在担当不起……\x02\x03",

            "…………不过在和平已经到来的情况下，\x01",
            "我也必须直面\x01",
            "我曾经犯过的罪才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x102,
        "#1043F理查德先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x1D,
        (
            "#111F呵呵，\x01",
            "不要一副这么担心的表情。\x02\x03",

            "#115F我绝对不会\x01",
            "做出辜负陛下\x01",
            "恩情的事情。\x02\x03",

            "但是，也该是我为自己\x01",
            "做个决断的时候了……\x02\x03",

            "#110F…………我只是这么想的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x102,
        "#1040F…………是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_E1BD")

    TalkEnd(0xFE)
    Return()

    # Function_71_DEFE end

    def Function_72_E1C1(): pass

    label("Function_72_E1C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_E21A")

    ChrTalk(    #403
        0x1F,
        (
            "#183F没、没别的事了吧。\x01",
            "赶快到那边去吧。\x02\x03",

            "不要打扰阁下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E312")

    label("loc_E21A")


    ChrTalk(    #404
        0x102,
        (
            "#1044F……是你…………\x02\x03",

            "#1040F在王都遭到袭击的时候，\x01",
            "你们的援军真的是帮了大忙。\x01",
            "谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x1F,
        (
            "#183F哼……\x01",
            "那是为了保释阁下\x01",
            "所做出的交换条件。\x02\x03",

            "你们没有理由\x01",
            "来感谢我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x102,
        "#1048F（真是不诚实啊……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_E312")

    TalkEnd(0xFE)
    Return()

    # Function_72_E1C1 end

    def Function_73_E316(): pass

    label("Function_73_E316")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_E33D")

    ChrTalk(    #407
        0x2A,
        "#311F啾啾～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3E8")

    label("loc_E33D")


    ChrTalk(    #408
        0x2A,
        "#310F啾啾～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x102,
        (
            "#1040F……基库，\x01",
            "你也来参加庆祝宴会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x2A,
        "#311F啾啾☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x102,
        (
            "#1054F（的确，基库的功劳\x01",
            "  就算受到表彰也不奇怪……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_E3E8")

    TalkEnd(0x2A)
    Return()

    # Function_73_E316 end

    def Function_74_E3EC(): pass

    label("Function_74_E3EC")

    TalkBegin(0xFE)

    ChrTalk(    #412
        0xFE,
        (
            "今晚我尽全力\x01",
            "准备了这些料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xFE,
        (
            "请不要客气，\x01",
            "尽量品尝吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_74_E3EC end

    def Function_75_E441(): pass

    label("Function_75_E441")

    TalkBegin(0xFE)

    ChrTalk(    #414
        0xFE,
        (
            "啊，\x01",
            "料理还够吧。\x02",
        )
    )

    Jump("loc_E466")

    label("loc_E466")

    CloseMessageWindow()

    ChrTalk(    #415
        0xFE,
        (
            "如果有什么事情\x01",
            "请尽管吩咐我。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_75_E441 end

    def Function_76_E494(): pass

    label("Function_76_E494")

    TalkBegin(0xFE)
    OP_8C(0xFE, 180, 0)

    ChrTalk(    #416
        0xFE,
        "两、两位小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xFE,
        "请不要在这里吵架。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_76_E494 end

    def Function_77_E4DC(): pass

    label("Function_77_E4DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 5)), scpexpr(EXPR_END)), "loc_E54F")

    ChrTalk(    #418
        0xFE,
        (
            "我是从圣海姆门\x01",
            "临时调来的厨师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xFE,
        (
            "能够在这样的会场工作，\x01",
            "真是作为厨师的骄傲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5DF")

    label("loc_E54F")


    ChrTalk(    #420
        0xFE,
        "哎呀，真是厉害的宴会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xFE,
        (
            "我是从圣海姆门\x01",
            "临时调来的厨师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "没想到能在这样的会场工作，\x01",
            "真是作为厨师的骄傲啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2D)

    label("loc_E5DF")

    TalkEnd(0xFE)
    Return()

    # Function_77_E4DC end

    def Function_78_E5E3(): pass

    label("Function_78_E5E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 6)), scpexpr(EXPR_END)), "loc_E640")

    ChrTalk(    #423
        0xFE,
        (
            "约修亚先生，\x01",
            "欢迎随时过来玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xFE,
        (
            "我还会帮你\x01",
            "换衣服的……㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E71E")

    label("loc_E640")


    ChrTalk(    #425
        0xFE,
        "啊………………！\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #426
        0xFE,
        (
            "……约修亚先生，\x01",
            "欢迎随时过来玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "我还会帮你\x01",
            "换衣服的……㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #428
        0x102,
        (
            "#1048F……不用了，\x01",
            "我不会再扮女佣了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2E)

    label("loc_E71E")

    TalkEnd(0xFE)
    Return()

    # Function_78_E5E3 end

    def Function_79_E722(): pass

    label("Function_79_E722")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 7)), scpexpr(EXPR_END)), "loc_E797")

    ChrTalk(    #429
        0xFE,
        (
            "现在想想，\x01",
            "那时的事情真的像做梦一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0xFE,
        (
            "终于有种\x01",
            "事情全部结束了的感觉。\x02",
        )
    )

    Jump("loc_E793")

    label("loc_E793")

    CloseMessageWindow()
    Jump("loc_E824")

    label("loc_E797")


    ChrTalk(    #431
        0xFE,
        (
            "呼，现在想想\x01",
            "那时的事情真的像做梦一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0xFE,
        (
            "当城门崩塌，\x01",
            "那群可怕的人冲进来的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0xFE,
        "我觉得自己就要晕倒了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F)

    label("loc_E824")

    TalkEnd(0xFE)
    Return()

    # Function_79_E722 end

    def Function_80_E828(): pass

    label("Function_80_E828")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 0)), scpexpr(EXPR_END)), "loc_E89B")

    ChrTalk(    #434
        0xFE,
        (
            "真是的，\x01",
            "我不知道『结社』是什么来头……\x02",
        )
    )

    Jump("loc_E870")

    label("loc_E870")

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "不过再也不想\x01",
            "遇到这种事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8FE")

    label("loc_E89B")


    ChrTalk(    #436
        0xFE,
        (
            "这座王城终于\x01",
            "也恢复了和平。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        (
            "到昨天为止一直忙着收拾打扫，\x01",
            "还真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x30)

    label("loc_E8FE")

    TalkEnd(0xFE)
    Return()

    # Function_80_E828 end

    def Function_81_E902(): pass

    label("Function_81_E902")

    TalkBegin(0xFE)

    ChrTalk(    #438
        0xFE,
        (
            "唔，\x01",
            "接下来去给那边的客人倒酒……\x02",
        )
    )

    Jump("loc_E937")

    label("loc_E937")

    CloseMessageWindow()

    ChrTalk(    #439
        0xFE,
        "唔，然后然后……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_81_E902 end

    def Function_82_E958(): pass

    label("Function_82_E958")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 1)), scpexpr(EXPR_END)), "loc_E9B4")

    ChrTalk(    #440
        0xFE,
        "啊，这位客人…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0xFE,
        (
            "刚才给您\x01",
            "送去了料理吗？\x02",
        )
    )

    Jump("loc_E9B0")

    label("loc_E9B0")

    CloseMessageWindow()
    Jump("loc_EA1F")

    label("loc_E9B4")


    ChrTalk(    #442
        0xFE,
        "呼，今天来了好多客人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xFE,
        "啊，这边的料理请随便品尝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0xFE,
        "要趁热吃才好吃哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x31)

    label("loc_EA1F")

    TalkEnd(0xFE)
    Return()

    # Function_82_E958 end

    def Function_83_EA23(): pass

    label("Function_83_EA23")

    TalkBegin(0xFE)

    ChrTalk(    #445
        0xFE,
        (
            "啊，这位客人。\x01",
            "要拿饮料吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "我们也准备了\x01",
            "没有酒精的鸡尾酒。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_83_EA23 end

    def Function_84_EA7C(): pass

    label("Function_84_EA7C")

    TalkBegin(0xFE)

    ChrTalk(    #447
        0xFE,
        (
            "多谢前来参加庆祝宴会，\x01",
            "谢谢您。\x02",
        )
    )

    Jump("loc_EAB6")

    label("loc_EAB6")

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "请放松一下，\x01",
            "好好享受宴会吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_84_EA7C end

    def Function_85_EAE5(): pass

    label("Function_85_EAE5")

    TalkBegin(0xFE)

    ChrTalk(    #449
        0xFE,
        (
            "庆祝宴会会场\x01",
            "就在空中庭院范围内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "请好好享受\x01",
            "会场热烈的气氛吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_85_EAE5 end

    def Function_86_EB44(): pass

    label("Function_86_EB44")

    TalkBegin(0xFE)

    ChrTalk(    #451
        0xFE,
        "希望在庆祝会上玩得愉快。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_86_EB44 end

    def Function_87_EB70(): pass

    label("Function_87_EB70")

    TalkBegin(0xFE)

    ChrTalk(    #452
        0xFE,
        (
            "……十分抱歉。\x01",
            "这里面是女王宫。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_87_EB70 end

    SaveToFile()

Try(main)
