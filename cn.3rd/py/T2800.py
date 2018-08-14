from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2800   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2800.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '雷克特',                               # 9
        '目标用照相机',                         # 10
        '王立学院·小道',                       # 11
        '街景林道方向',                         # 12
        '',                                     # 13
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
        'ED6_DT07/CH02670 ._CH',             # 00
        'ED6_DT07/CH00043 ._CH',             # 01
        'ED6_DT26/CH20777 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02670P._CP',             # 00
        'ED6_DT07/CH00043P._CP',             # 01
        'ED6_DT26/CH20777P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        X                   = 84080,
        Z                   = 0,
        Y                   = 28010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3490,
        Z                   = 0,
        Y                   = 46180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 43800,
        Y                   = 0,
        Z                   = 49800,
        Range               = 50300,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xB9F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 43800,
        Y                   = 0,
        Z                   = 44200,
        Range               = 50300,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xA4D8,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 43800,
        Y                   = 0,
        Z                   = 47600,
        Range               = 46500,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xACA8,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 41180,
        Y                   = 0,
        Z                   = 74060,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 67260,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 53150,
        Y                   = 0,
        Z                   = 59630,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 48380,
        Y                   = 0,
        Z                   = 45960,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 52870,
        Y                   = 0,
        Z                   = 32110,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 53030,
        Y                   = 0,
        Z                   = 24850,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 47120,
        Y                   = 0,
        Z                   = 19010,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 22030,
        Y                   = 0,
        Z                   = 25660,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 22010,
        Y                   = 0,
        Z                   = 67170,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = 13480,
        TriggerZ            = 1000,
        TriggerY            = 46000,
        TriggerRange        = 1000,
        ActorX              = 13480,
        ActorZ              = 1000,
        ActorY              = 46000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22000,
        TriggerZ            = 500,
        TriggerY            = 68220,
        TriggerRange        = 500,
        ActorX              = 22000,
        ActorZ              = 1100,
        ActorY              = 68220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22000,
        TriggerZ            = 500,
        TriggerY            = 24820,
        TriggerRange        = 1000,
        ActorX              = 22000,
        ActorZ              = 1100,
        ActorY              = 24820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59440,
        TriggerZ            = 9000,
        TriggerY            = 17860,
        TriggerRange        = 1000,
        ActorX              = 59440,
        ActorZ              = 9500,
        ActorY              = 17860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_352",          # 00, 0
        "Function_1_3A7",          # 01, 1
        "Function_2_439",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_612",          # 04, 4
        "Function_5_76E",          # 05, 5
        "Function_6_97F",          # 06, 6
        "Function_7_19A7",         # 07, 7
        "Function_8_19E8",         # 08, 8
        "Function_9_1A10",         # 09, 9
        "Function_10_1A4E",        # 0A, 10
        "Function_11_1A52",        # 0B, 11
        "Function_12_1A56",        # 0C, 12
        "Function_13_1A5A",        # 0D, 13
        "Function_14_1A5E",        # 0E, 14
        "Function_15_1A62",        # 0F, 15
        "Function_16_1ADD",        # 10, 16
        "Function_17_1B3A",        # 11, 17
    )


    def Function_0_352(): pass

    label("Function_0_352")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_374")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_3A6")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_38A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_3A6")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3A6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_3A6")

    Return()

    # Function_0_352 end

    def Function_1_3A7(): pass

    label("Function_1_3A7")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D5")
    OP_11(0x0, 0x0, 0x0, 0x9470, 0x14C08, 0x0)

    label("loc_3D5")

    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_B2(0x0, 0x2, 0x80)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_438")
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)

    label("loc_438")

    Return()

    # Function_1_3A7 end

    def Function_2_439(): pass

    label("Function_2_439")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_439")

    label("loc_44E")

    Return()

    # Function_2_439 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1CF, 0x0, 0x64)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_6F(0x9, 60)
    OP_11(0x64, 0x64, 0x96, 0x9470, 0x14C08, 0x0)
    OP_6D(48000, 0, 45460, 0)
    OP_67(0, 9460, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(130000, 0)
    OP_6E(440, 0)
    SetChrPos(0x105, -10000, 0, 45880, 90)

    def lambda_4D1():
        OP_6D(5440, 0, 45500, 12000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4D1)

    def lambda_4E9():
        OP_67(0, 7020, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4E9)

    def lambda_501():
        OP_6C(225000, 12000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_501)

    def lambda_511():
        OP_6E(354, 12000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_511)
    FadeToBright(2000, 0)
    Sleep(9000)

    def lambda_52F():
        OP_8E(0xFE, 0x16BC, 0x0, 0xB338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52F)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x105,
        (
            "#045F#11P呵呵，又这么晚了。\x02\x03",

            "#542F每次去孤儿院，\x01",
            "总是不知不觉就待了很久。\x02\x03",

            "要赶紧回宿舍才行……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CE():
        OP_8E(0xFE, 0x553C, 0x0, 0xB338, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5CE)
    Sleep(2000)

    def lambda_5EE():
        OP_6B(2700, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5EE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/T2812   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_44F end

    def Function_4_612(): pass

    label("Function_4_612")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    OP_B2(0x1, 0x2, 0x80)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    SetChrPos(0x105, 22000, 250, 67020, 180)
    OP_6D(22640, 0, 67720, 0)
    OP_67(0, 8700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #1
        0x105,
        (
            "#049F#40W……我…………\x01",
            "不是那样的……\x02\x03",

            "#049F不是优等生……\x01",
            "…………也不是为了什么奉献……！\x02\x03",

            "明明不是为了这种理由\x01",
            "才去的……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F6E)
    EventEnd(0x0)
    Return()

    # Function_4_612 end

    def Function_5_76E(): pass

    label("Function_5_76E")

    EventBegin(0x0)
    Fade(1500)
    OP_6D(47000, 0, 44700, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(135000, 0)
    OP_6E(286, 0)
    SetChrPos(0x105, 45700, 250, 46000, 90)
    OP_6F(0x0, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)
    OP_8C(0x105, 270, 400)
    Sleep(500)

    ChrTalk(    #2
        0x105,
        "#049F#5P#40W………呼……………\x02",
    )

    CloseMessageWindow()

    def lambda_82C():
        OP_6D(44910, -300, 44260, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_82C)

    def lambda_844():
        OP_8E(0xFE, 0xAB7C, 0x0, 0xB194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_844)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x11, 0x0)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 43700, -300, 45460, 270)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 1)
    Sleep(1000)

    ChrTalk(    #3
        0x105,
        (
            "#047F#5P#40W………………………………\x02\x03",

            "…………唉………………\x02\x03",

            "#049F（…………为什么呢。\x01",
            "#5W  #40W……心中忐忑不安………）\x02\x03",

            "(为什么我会变成那样………)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearParty()
    AddParty(0x3A, 0xEE, 0xFF)
    NewScene("ED6_DT21/T2812   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_76E end

    def Function_6_97F(): pass

    label("Function_6_97F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(44910, -300, 44260, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(135000, 0)
    OP_6E(286, 0)
    OP_6D(36010, -300, 44770, 0)
    OP_67(0, 3570, -10000, 0)
    OP_6B(980, 0)
    OP_6C(225000, 0)
    OP_6E(806, 0)
    SetChrPos(0x105, 43700, -300, 45460, 270)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 45630, 0, 50000, 180)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)

    def lambda_A57():
        OP_6D(41260, -300, 44200, 4000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A57)

    def lambda_A6F():
        OP_67(0, 4930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A6F)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x105, 0x1)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #4
        0x105,
        "#049F#5P……唉……………………\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_AC6():
        OP_6B(1090, 2000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC6)
    OP_43(0x10, 0x3, 0x0, 0x8)
    WaitChrThread(0x10, 0x3)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #5
        0x10,
        "#1774F#6P『最近连自己都搞不太懂了』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#047F#5P…………请不要\x01",
            "站在我后面。\x02\x03",

            "#042F这是低级趣味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#1771F#6P哈哈哈。\x01",
            "今天心情相当不好啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B99():
        OP_8E(0xFE, 0xAB7C, 0x0, 0xB7FC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B99)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 270, 0)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x10, 43700, -300, 47100, 270)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Fade(1000)
    OP_6D(44120, -300, 45540, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(1250, 0)
    OP_6C(134000, 0)
    OP_6E(572, 0)
    OP_6D(44200, -300, 45280, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(1250, 0)
    OP_6C(134000, 0)
    OP_6E(572, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #8
        0x10,
        "#1776F#6P（唔，脸色不好……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        (
            "#049F#5P……我一直\x01",
            "怀有这样的憧憬。\x02\x03",

            "普通的生活啦，\x01",
            "家人啦，朋友啦……\x02\x03",

            "………但是，\x01",
            "却总是不顺利。\x02\x03",

            "总是，不顺利……\x02\x03",

            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#1775F#6P…………原来如此啊。\x02\x03",

            "#1779F所以不知不觉就烦躁起来，\x01",
            "对那些不明就里的家伙\x01",
            "发起脾气了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    Fade(300)
    SetChrSubChip(0x105, 2)
    Sleep(500)

    ChrTalk(    #11
        0x105,
        (
            "#042F#5P不是这样的。\x01",
            "请别把我跟学长你混为一谈。\x02\x03",

            "……我也非常\x01",
            "重视乔儿同学的。\x02\x03",

            "#049F但是……\x02\x03",

            "#046F#3S我没有做错……！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    def lambda_EC0():
        OP_6B(1200, 30000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EC0)
    Sleep(500)

    ChrTalk(    #12
        0x105,
        (
            "#049F#5P#40W什么同情……什么奉献……\x01",
            "我不是为了这种理由。\x02\x03",

            "那个地方不是这样的。\x01",
            "……是不需要别人可怜的！\x02\x03",

            "#047F不是这样，不是这样……\x01",
            "我只是因为自己喜欢，\x01",
            "纯粹地感到它很重要……\x02\x03",

            "所以，才会去那里的……！\x02\x03",

            "#049F我不是什么优等生。\x02\x03",

            "我只是……\x01",
            "……想要有家人陪伴而已……！！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_1015():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1015)
    Sleep(1000)

    ChrTalk(    #13
        0x105,
        (
            "#049F#5P#40W（果然，什么都是这样不顺利……）\x02\x03",

            "（无论是家人，还是朋友……）\x02\x03",

            "（都是我无法触及的……！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#1775F#6P嗯～。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrSubChip(0x105, 2)
    Sleep(300)

    ChrTalk(    #15
        0x105,
        "#047F#5P……学长。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #16
        0x105,
        (
            "#046F#5P#3S你就没有什么\x01",
            "要拼命去做的事情吗！？#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #17
        0x105,
        (
            "#046F#5P#3S没有什么执着或是\x01",
            "决不能退让的事情吗！？#2S\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #18
        0x10,
        "#1773F#6P哦～哦，好可怕哦～\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #19
        0x105,
        (
            "#049F#5P#40W……够了。\x01",
            "…………唉……\x02\x03",

            "#047F对学长发脾气\x01",
            "也是白搭啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)

    ChrTalk(    #20
        0x10,
        (
            "#1775F#6P………………那么？\x02\x03",

            "#1777F结果你还是不知道\x01",
            "自己到底为什么发火啊。\x02",
        )
    )

    OP_63(0x105)
    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    Fade(100)
    SetChrSubChip(0x105, 2)
    Sleep(300)

    ChrTalk(    #21
        0x105,
        (
            "#042F#5P…………学长，\x01",
            "你果然没有好好听我说话。\x02\x03",

            "我生气是因为，\x01",
            "嗯，明明不是因为同情什么的……\x02\x03",

            "#046F……我并不是，\x01",
            "为了这种理由……！\x02\x03",

            "是因为真的很重要，\x01",
            "真的这么想才…………！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#1776F#6P唉～话怎么又绕回去了。\x02\x03",

            "我都听腻了～\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xA4, 0x0, 0x64)
    Fade(250)
    SetChrPos(0x10, 43900, 0, 47100, 270)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x105,
        (
            "#043F#5P学、学长！\x01",
            "你好好听我说啊！\x02\x03",

            "#042F我是很认真在说的。\x01",
            "拜托你别这么轻描淡写的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1775F#6P嗯～\x01",
            "只有这一点\x01",
            "你一定得自己搞清楚。\x02\x03",

            "#1777F就像人们常说的那样……\x01",
            "解铃还需系铃人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        "#043F#5P#40W咦…………\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x10, 120, 500)

    def lambda_1550():
        OP_6D(45580, -300, 42590, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1550)
    OP_43(0x10, 0x3, 0x0, 0x7)
    SetChrSubChip(0x105, 0)

    ChrTalk(    #26 op#A
        0x10,
        "#1771F#15A#5P尽情烦恼吧～⊙\x02",
    )

    Sleep(2000)
    SetChrSubChip(0x105, 1)

    ChrTalk(    #27 op#A
        0x105,
        "#043F#3S#6P#15A学长！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x11, 0x0)

    def lambda_15E7():
        OP_6D(44590, -300, 44500, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_15E7)
    WaitChrThread(0x11, 0x0)
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #28
        0x105,
        (
            "#043F#5P#40W…………………………\x02\x03",

            "#047F#20W……算了。\x02\x03",

            "反正学长只会\x01",
            "捉弄人而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #29
        0x105,
        (
            "#049F#5P（……其实，没有这种事吧。）\x02\x03",

            "（雷克特学长，\x01",
            "　其实是深思熟虑的人……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, 100)
    OP_C4(0x0, 0x800)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x18\x07\x05#40W结果你还是不知道\x01",
            "自己到底为什么发火啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x18\x07\x05#40W就像人们常说的那样……\x01",
            "解铃还需系铃人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x105,
        (
            "#043F#5P#40W………我生气……\x02\x03",

            "是因为什么呢……\x02\x03",

            "#047F……我的心里这么乱，\x01",
            "这样波澜起伏……\x02\x03",

            "究竟是为什么…………？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1859():
        OP_6B(1100, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1859)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x11, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x18\x07\x0C#40W…………对了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #34
        "\x18\x07\x0C#40W我一直，装作没察觉的样子。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "\x18\x07\x0C#40W拼命抓住什么东西，\x01",
            "像念咒般告诉自己这是对的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #36
        "\x18\x07\x0C#40W我一定是，害怕失去吧。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #37
        "\x18\x07\x0C#40W正因为这样，我的心才―――……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_20(0xFA0)
    OP_21()
    Sleep(2000)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_97F end

    def Function_7_19A7(): pass

    label("Function_7_19A7")


    def lambda_19AD():
        OP_8F(0xFE, 0xB1A8, 0x0, 0xB158, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19AD)
    WaitChrThread(0x10, 0x1)

    def lambda_19CD():
        OP_8E(0xFE, 0xB194, 0x0, 0x7814, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19CD)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_7_19A7 end

    def Function_8_19E8(): pass

    label("Function_8_19E8")


    def lambda_19EE():
        OP_8E(0xFE, 0xAED8, 0x0, 0xB2E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_19EE)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    Return()

    # Function_8_19E8 end

    def Function_9_1A10(): pass

    label("Function_9_1A10")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #38
        0x105,
        "#049F…………………………\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_9_1A10 end

    def Function_10_1A4E(): pass

    label("Function_10_1A4E")

    SetPlaceName(0x5F)
    Return()

    # Function_10_1A4E end

    def Function_11_1A52(): pass

    label("Function_11_1A52")

    SetPlaceName(0x5C)
    Return()

    # Function_11_1A52 end

    def Function_12_1A56(): pass

    label("Function_12_1A56")

    SetPlaceName(0x5D)
    Return()

    # Function_12_1A56 end

    def Function_13_1A5A(): pass

    label("Function_13_1A5A")

    SetPlaceName(0x6C)
    Return()

    # Function_13_1A5A end

    def Function_14_1A5E(): pass

    label("Function_14_1A5E")

    SetPlaceName(0x6D)
    Return()

    # Function_14_1A5E end

    def Function_15_1A62(): pass

    label("Function_15_1A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A92")

    ChrTalk(    #39
        0x105,
        "#047F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD9")

    label("loc_1A92")


    ChrTalk(    #40
        0x105,
        (
            "#042F…………………………\x02\x03",

            "#047F现在我不想见……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1AD9")

    TalkEnd(0xFF)
    Return()

    # Function_15_1A62 end

    def Function_16_1ADD(): pass

    label("Function_16_1ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B0D")

    ChrTalk(    #41
        0x105,
        "#047F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B36")

    label("loc_1B0D")


    ChrTalk(    #42
        0x105,
        "#049F现在我谁也不想见……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1B36")

    TalkEnd(0xFF)
    Return()

    # Function_16_1ADD end

    def Function_17_1B3A(): pass

    label("Function_17_1B3A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2811   ._SN", 112, 0, 0)
    IdleLoop()
    TalkEnd(0xFF)
    Return()

    # Function_17_1B3A end

    SaveToFile()

Try(main)
