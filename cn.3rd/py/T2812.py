from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2812   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2812.x',
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
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '雷欧',                                 # 11
        '临时',                                 # 12
        '目标用照相机',                         # 13
        '',                                     # 14
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02680 ._CH',             # 02
        'ED6_DT07/CH02393 ._CH',             # 03
        'ED6_DT26/CH20785 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02680P._CP',             # 02
        'ED6_DT07/CH02393P._CP',             # 03
        'ED6_DT26/CH20785P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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


    DeclActor(
        TriggerX            = 3000,
        TriggerZ            = 4000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = 3000,
        ActorZ              = 4500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3000,
        TriggerZ            = 4000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -3000,
        ActorZ              = 4500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3000,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = 3000,
        ActorZ              = 500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3000,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -3000,
        ActorZ              = 500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_234",          # 01, 1
        "Function_2_285",          # 02, 2
        "Function_3_FC6",          # 03, 3
        "Function_4_FDD",          # 04, 4
        "Function_5_112D",         # 05, 5
        "Function_6_1205",         # 06, 6
        "Function_7_125D",         # 07, 7
        "Function_8_12E9",         # 08, 8
        "Function_9_1375",         # 09, 9
        "Function_10_1404",        # 0A, 10
        "Function_11_2581",        # 0B, 11
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_221")
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_233")

    label("loc_221")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_233")

    Return()

    # Function_0_202 end

    def Function_1_234(): pass

    label("Function_1_234")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_284")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_1B(0x0, 0x0, 0x6)

    label("loc_284")

    Return()

    # Function_1_234 end

    def Function_2_285(): pass

    label("Function_2_285")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-87500, -1500, 340, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, -89200, 0, -5000, 90)
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x42B, 0x0)
    ExitThread()

    def lambda_2F1():
        OP_6D(-87500, 2400, 340, 8000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2F1)
    OP_43(0x14, 0x1, 0x0, 0x3)
    FadeToBright(2000, 0)

    def lambda_319():
        OP_8E(0xFE, 0xFFFEB7E0, 0x7D0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_319)
    WaitChrThread(0x105, 0x1)

    def lambda_339():
        OP_8E(0xFE, 0xFFFEB7E0, 0xFA0, 0xFFFFFD30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_339)
    WaitChrThread(0x105, 0x1)

    def lambda_359():
        OP_8E(0xFE, 0xFFFE9454, 0xFA0, 0xFFFFFD30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_359)
    WaitChrThread(0x105, 0x1)
    Sleep(100)
    OP_8C(0x105, 90, 700)
    Sleep(800)
    OP_8C(0x105, 180, 700)
    Sleep(800)
    OP_8C(0x105, 90, 700)
    Sleep(800)
    OP_8C(0x105, 0, 700)
    Sleep(300)
    OP_70(0x4, 0x1E)
    OP_73(0x4)

    def lambda_3B8():
        OP_8E(0xFE, 0xFFFE9454, 0xFA0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-119350, 0, -4310, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x105, 0xFF)
    SetChrPos(0x105, -120860, 0, -9500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, -120460, 0, -9100, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_D7(0x1, 20000, 19)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_467():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_467)

    def lambda_479():
        OP_8E(0xFE, 0xFFFE28C0, 0x0, 0xFFFFE1E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_479)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x105,
        (
            "#044F#12P咦、咦……？\x01",
            "一片漆黑…………\x02\x03",

            "#043F乔儿同学……\x01",
            "已经睡了吗……？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -120860, 0, -3600, 180)
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x64)
    OP_D7(0x0, 20000, 19)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #1
        0x105,
        "#044F#12P#3S哇、哇…………！？#2S\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#649F#5P#3S#80W你～回～来～了～啊……！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        (
            "#045F#12P我、我回来了乔儿同学。\x02\x03",

            "#542F嗯…………\x01",
            "你站在那里干什么呢？\x02\x03",

            "还把灯都关了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#645F#5P哎呀～…………\x01",
            "可爱的科洛丝小姐不在\x01",
            "我好寂寞啊～。\x02\x03",

            "最近一段时间，每到假日\x01",
            "你就高高兴兴地外出，\x01",
            "一直都不回来嘛。\x02\x03",

            "#649F这么长的时间，\x01",
            "你都上哪里去了呀～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#540F#12P对、对不起。\x01",
            "我又超过宵禁的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#648F#5P啊～，那个没关系。\x01",
            "我顺利帮你瞒过老师了。\x02\x03",

            "可是总这么持续下去，\x01",
            "总有一天会暴露的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        (
            "#045F#12P是、是啊，说得对……\x02\x03",

            "#542F今后，\x01",
            "我会尽量早点回来的。\x02\x03",

            "#540F（要不然，\x01",
            "　特蕾莎老师也会生气的呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_85F():
        OP_6D(-119940, 0, -1990, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_85F)

    def lambda_877():
        OP_67(0, 4270, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_877)

    def lambda_88F():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_88F)

    def lambda_89F():

        label("loc_89F")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_89F")

    QueueWorkItem2(0x10, 2, lambda_89F)

    def lambda_8B0():
        OP_8E(0xFE, 0xFFFE21A4, 0x0, 0xFFFFEA20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8B0)
    WaitChrThread(0x105, 0x1)

    def lambda_8D0():
        OP_8E(0xFE, 0xFFFE21A4, 0x0, 0xFFFFF1F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8D0)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x14, 0x0)

    ChrTalk(    #8
        0x10,
        "#641F#11P…………那么？\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x105, 0x10, 400)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        "#044F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#649F#11P你每次都是上哪儿去了啊？？\x02\x03",

            "#100W难不成～…………\x02\x03",

            "#659F#20W#3S……是去找男人了！！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #11
        0x105,
        (
            "#542F#6P不、不是的啦。\x02\x03",

            "#045F只是去朋友家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#649F#11P哦，朋友。\x01",
            "朋友啊！？\x02\x03",

            "那到底是\x01",
            "怎样的朋友呢！！？\x02",
        )
    )

    Jump("loc_A84")

    label("loc_A84")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #13
        0x105,
        (
            "#045F#6P嗯、嗯……\x02\x03",

            "#048F是叫玛西亚孤儿院的地方。\x02\x03",

            "以前我在那里\x01",
            "受过照顾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#643F#11P咦…………孤儿院？\x02\x03",

            "啊啊，这么说来\x01",
            "去玛诺利亚村途中是有这么一个地方呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x10,
        (
            "#645F#11P怎么是孤儿院啊～……\x01",
            "……………啧，真可惜。\x02\x03",

            "#648F不过挺有科洛丝的风格嘛？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    Sleep(150)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #16
        0x105,
        "#044F#6P#40W……咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#644F#11P嗯嗯，照顾可怜的孩子们，\x01",
            "真是具有奉献精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        "#043F#60W#6P…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #19
        0x10,
        "#641F#11P嘿，你个优等生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#049F#60W#6P………………才……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #21
        0x105,
        "#046F#4S#20W#6P才不是可怜！！#2S\x02",
    )

    OP_7C(0x64, 0xDC, 0xBB8, 0x64)

    def lambda_D54():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_D54)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #22
        0x10,
        "#643F#11P……咦？\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB7)
    Sleep(500)

    ChrTalk(    #23
        0x105,
        (
            "#042F#6P那、那些孩子们\x01",
            "才不『可怜』。#2S\x02\x03",

            "而且我也不是\x01",
            "在做什么奉献！#2S\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)
    OP_8C(0x105, 180, 600)
    Sleep(300)

    ChrTalk(    #24
        0x105,
        "#049F#4S#5P告辞了！！#2S\x02",
    )

    OP_7C(0x0, 0xB4, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_E3C():
        OP_6D(-118900, 0, -4460, 1500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_E3C)

    def lambda_E54():
        OP_8E(0xFE, 0xFFFE21A4, 0x0, 0xFFFFE8A4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E54)
    WaitChrThread(0x105, 0x1)

    def lambda_E74():
        OP_8E(0xFE, 0xFFFE2910, 0x0, 0xFFFFE1D8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E74)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 700)
    OP_22(0x6, 0x0, 0x64)
    Sleep(200)

    def lambda_EA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_EA5)

    def lambda_EB7():
        OP_8E(0xFE, 0xFFFE2910, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EB7)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_22(0x18B, 0x0, 0x64)
    Sleep(2500)

    ChrTalk(    #25
        0x10,
        (
            "#643F#5P……………………\x02\x03",

            "吓、吓我一跳……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #26
        0x10,
        (
            "#1892F#5P#40W………………嗯……\x02\x03",

            "我是不是\x01",
            "坏毛病又犯了呢……\x02",
        )
    )

    Jump("loc_F9D")

    label("loc_F9D")

    CloseMessageWindow()

    def lambda_FA4():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_FA4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_285 end

    def Function_3_FC6(): pass

    label("Function_3_FC6")

    Sleep(1500)
    ClearMapFlags(0x10000000)
    SetPlaceName(0x6D)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_FC6 end

    def Function_4_FDD(): pass

    label("Function_4_FDD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-800, 4000, -3280, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13B, 0, -500, -9250, 0)
    OP_9F(0x13B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_104D():
        OP_6D(-800, 0, -3280, 5000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_104D)
    FadeToBright(2000, 0)
    OP_0D()
    ClearMapFlags(0x10000000)
    SetPlaceName(0x6C)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x14, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_108F():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFE570, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_108F)

    def lambda_10AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_10AA)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x13B, 0x1)
    Sleep(300)
    OP_62(0x13B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #27
        0x13B,
        (
            "#1892F#6P（去找汉斯…………\x01",
            "　问问看吧……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_FDD end

    def Function_5_112D(): pass

    label("Function_5_112D")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "出声叫门\x01",      # 0
            "还是算了\x01",      # 1
        )
    )

    Jump("loc_1173")

    label("loc_1173")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")
    Call(0, 10)
    Jump("loc_1201")

    label("loc_119F")

    OP_62(0x13B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #28
        0x13B,
        (
            "#647F（嗯～…………）\x02\x03",

            "#1892F（下不定决心……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1201")

    TalkEnd(0xFF)
    Return()

    # Function_5_112D end

    def Function_6_1205(): pass

    label("Function_6_1205")

    EventBegin(0x2)

    ChrTalk(    #29
        0x13B,
        (
            "#1892F（去找汉斯…………\x01",
            "　问问看吧……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13B, 0, 400)
    OP_90(0x13B, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    EventEnd(0x4)
    Return()

    # Function_6_1205 end

    def Function_7_125D(): pass

    label("Function_7_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_128F")

    ChrTalk(    #30
        0x13B,
        "#647F这里不是汉斯的房间……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E5")

    label("loc_128F")


    ChrTalk(    #31
        0x13B,
        (
            "#647F这里不是\x01",
            "汉斯的房间吧。\x02\x03",

            "#1892F……不想见到\x01",
            "其他的学生……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_12E5")

    TalkEnd(0xFF)
    Return()

    # Function_7_125D end

    def Function_8_12E9(): pass

    label("Function_8_12E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_131B")

    ChrTalk(    #32
        0x13B,
        "#647F被老师发现就麻烦了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1371")

    label("loc_131B")


    ChrTalk(    #33
        0x13B,
        (
            "#647F这里不是\x01",
            "汉斯的房间吧。\x02\x03",

            "#1892F……不想见到\x01",
            "其他的学生……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1371")

    TalkEnd(0xFF)
    Return()

    # Function_8_12E9 end

    def Function_9_1375(): pass

    label("Function_9_1375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13A8")

    ChrTalk(    #34
        0x13B,
        "#1892F被老师发现就麻烦了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1400")

    label("loc_13A8")


    ChrTalk(    #35
        0x13B,
        (
            "#1892F因为宵禁时间已经开始了啊……\x02\x03",

            "被艾福托老师\x01",
            "发现就麻烦了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1400")

    TalkEnd(0xFF)
    Return()

    # Function_9_1375 end

    def Function_10_1404(): pass

    label("Function_10_1404")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(2330, 4000, 900, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(320000, 0)
    OP_6E(358, 0)
    SetChrPos(0x13B, 3200, 4000, -1000, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 3200, 4000, 1500, 180)
    Sleep(1000)
    OP_62(0x13B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13B)
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x13B,
        "#1890F#6P汉斯～，在吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "#1P啊、啊啊。\x01",
            "…………乔儿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#1P你稍等一下。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_1524():
        OP_8E(0xFE, 0xC1C, 0xFA0, 0x12C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1524)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #39
        0x11,
        (
            "#733F#11P怎么了，这么晚。\x02\x03",

            "#732F发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x13B,
        "#1892F#6P嗯～……没什么～…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        (
            "#734F#11P你这不是没什么的表情吧。\x02\x03",

            "#730F……总之先进来吧。\x01",
            "现在就我一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x13B,
        "#649F#6P你别做奇怪的事哦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        (
            "#734F#11P谁会做啊!\x01",
            "白痴,快点进来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 500)

    def lambda_1675():
        OP_8E(0xFE, 0xC80, 0xFA0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1675)
    WaitChrThread(0x11, 0x1)

    def lambda_1695():
        OP_8E(0xFE, 0xC80, 0xFA0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1695)
    WaitChrThread(0x13B, 0x1)
    Fade(1000)
    OP_6D(29860, 0, -5000, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13B, 30800, 0, -9500, 0)
    SetChrPos(0x11, 30800, 0, -9500, 0)
    OP_9F(0x13B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_172F():
        OP_6D(29860, 0, -1000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_172F)

    def lambda_1747():
        OP_67(0, 4960, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1747)

    def lambda_175F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_175F)

    def lambda_1771():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1771)
    Sleep(1000)

    def lambda_1791():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_1791)

    def lambda_17A3():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFF128, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_17A3)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x11, 0x1)

    def lambda_17CD():

        label("loc_17CD")

        TurnDirection(0xFE, 0x13B, 500)
        OP_48()
        Jump("loc_17CD")

    QueueWorkItem2(0x11, 2, lambda_17CD)
    WaitChrThread(0x13B, 0x1)

    def lambda_17E3():
        OP_6D(28440, 0, -1490, 2500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_17E3)

    def lambda_17FB():
        OP_8E(0xFE, 0x7274, 0x0, 0xFFFFF128, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_17FB)
    WaitChrThread(0x13B, 0x1)
    OP_8C(0x13B, 180, 500)
    Sleep(300)
    SetChrFlags(0x13B, 0x4)

    def lambda_182C():
        OP_96(0xFE, 0x7274, 0x1CC, 0xFFFFF3A8, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_182C)
    WaitChrThread(0x13B, 0x1)
    SetChrChipByIndex(0x13B, 3)
    SetChrSubChip(0x13B, 0)
    OP_22(0x8F, 0x0, 0x64)
    WaitChrThread(0x14, 0x0)
    OP_44(0x11, 0x2)
    Sleep(500)

    ChrTalk(    #44
        0x11,
        (
            "#735F#12P那么，\x02\x03",

            "#730F………是关于科洛丝吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #45
        0x13B,
        (
            "#645F#11P唉～…………\x01",
            "真是瞒不住汉斯啊～。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x13B, 1)
    Sleep(500)

    ChrTalk(    #46
        0x13B,
        (
            "#1890F#5P汉斯你啊，\x01",
            "没跟科洛丝吵过架吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#735F#12P现在还没有过。\x02\x03",

            "那家伙，\x01",
            "一般很少说出自己的意见嘛。\x02\x03",

            "#732F……你们吵架了？\x02",
        )
    )

    Jump("loc_19BA")

    label("loc_19BA")

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x13B, 0)
    Sleep(500)

    ChrTalk(    #48
        0x13B,
        (
            "#1892F#11P#40W嗯……\x02\x03",

            "……………………\x02\x03",

            "……我总觉得\x01",
            "自己是个讨厌的人。\x02\x03",

            "我好像又说了\x01",
            "不经大脑的话。\x02\x03",

            "…………让科洛丝……\x01",
            "非常生气…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#733F#12P生气了！？　那个科洛丝？\x02\x03",

            "#735F那可真厉害啊……\x01",
            "我还真想见识一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_59()
    Fade(100)
    SetChrSubChip(0x13B, 1)
    Sleep(300)

    ChrTalk(    #50
        0x13B,
        "#1893F#5P……汉斯～，你在听吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#732F#12P哦，当然在听！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x13B,
        (
            "#1892F#5P…………感觉啊……\x02\x03",

            "#645F好像……\x01",
            "没脸再见她了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #53
        0x13B,
        (
            "#1892F#5P……真不想回去啊～……\x02\x03",

            "#1890F今晚我能住这儿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#734F#12P能才有鬼。\x01",
            "赶快回去。\x02\x03",

            "#730F只要道歉，\x01",
            "那家伙应该会原谅你的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x13B,
        "#1892F#5P是这样吗…………\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x13B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13B)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "今天不回去了\x01",            # 0
            "今天还是乖乖回去吧\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2157")

    ChrTalk(    #56
        0x13B,
        (
            "#1892F#5P（科洛丝大概\x01",
            "　不会再跟我说话了吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x186, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x13B, 28780, 460, -2560, 180)
    SetChrFlags(0x13B, 0x2)
    SetChrFlags(0x13B, 0x800)
    SetChrChipByIndex(0x13B, 4)
    SetChrSubChip(0x13B, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x13B,
        "#1892F#5P唉…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(300)

    ChrTalk(    #58
        0x11,
        (
            "#735F（这家伙以前也因为\x01",
            "　类似的事情失去过朋友……）\x02\x03",

            "#736F（……可能在害怕吧。\x01",
            "　害怕失去科洛丝……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0xFFFFFE3E, 1350, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(1000)

    ChrTalk(    #59
        0x13B,
        "#5P呼啊～。\x02",
    )

    CloseMessageWindow()
    OP_62(0x13B, 0xFFFFFE3E, 1350, 0x1C, 0x21, 0x12C, 0x0)

    ChrTalk(    #60
        0x11,
        "#733F#12P……怎么就睡了！？\x02",
    )

    CloseMessageWindow()

    def lambda_1EC5():
        OP_6D(29860, 0, -3000, 1200)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1EC5)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 30960, 0, -9500, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_1F03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1F03)

    def lambda_1F15():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFE318, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F15)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x11, 0x12, 500)

    ChrTalk(    #61
        0x11,
        (
            "#733F#11P啊…………\x01",
            "雷、雷欧学长！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F77():
        OP_8F(0xFE, 0x79A4, 0x0, 0xFFFFF100, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F77)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #62
        0x11,
        (
            "#731F#11P啊～……哎～………\x01",
            "今、今天好晚啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FD2():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFEA0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1FD2)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    TurnDirection(0x12, 0x13B, 500)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_8C(0x11, 270, 600)
    Sleep(500)
    OP_8C(0x11, 180, 600)
    OP_63(0x12)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #63
        0x11,
        (
            "#733F#11P嗯～那个，\x01",
            "这个是，因为有各种原因……\x02\x03",

            "#731F啊～就是说\x01",
            "这家伙不想回去了……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 300)
    Sleep(500)

    ChrTalk(    #64
        0x12,
        (
            "#1782F#6P……事情经过就免了。\x02\x03",

            "#1780F我们睡外面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x11,
        (
            "#734F#11P（到底是明白了，\x01",
            "　还是误会了……！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_213F():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_213F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_2562")

    label("loc_2157")

    OP_59()
    Fade(300)
    SetChrSubChip(0x13B, 0)
    Sleep(500)

    ChrTalk(    #66
        0x13B,
        "#645F#5P呼…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2191():
        OP_96(0xFE, 0x7274, 0x0, 0xFFFFF128, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_2191)
    WaitChrThread(0x13B, 0x1)
    SetChrChipByIndex(0x13B, 65535)
    SetChrSubChip(0x13B, 0)
    ClearChrFlags(0x13B, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #67
        0x13B,
        "#648F#5P嗯～那回头见～☆\x02",
    )

    CloseMessageWindow()

    def lambda_21F2():
        OP_6D(29860, 0, -3000, 1200)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_21F2)

    def lambda_220A():

        label("loc_220A")

        TurnDirection(0xFE, 0x13B, 500)
        OP_48()
        Jump("loc_220A")

    QueueWorkItem2(0x11, 2, lambda_220A)

    def lambda_221B():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFF128, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_221B)
    WaitChrThread(0x13B, 0x1)

    def lambda_223B():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFDAE4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_223B)
    OP_43(0x13B, 0x3, 0x0, 0xB)
    Sleep(600)

    ChrTalk(    #68
        0x11,
        "#733F#11P啊……乔儿…………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13B, 0x1)
    WaitChrThread(0x13B, 0x3)
    OP_44(0x11, 0x2)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #69
        0x11,
        (
            "#735F#11P（那家伙以前也因为\x01",
            "　类似的事情失去过朋友……）\x02\x03",

            "#736F（真有点担心啊……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 30960, 0, -9500, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_2349():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2349)

    def lambda_235B():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFE318, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_235B)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x11, 0x12, 500)

    ChrTalk(    #70
        0x11,
        (
            "#733F#11P啊…………雷欧学长！？\x02\x03",

            "#731F今、今天好晚啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        (
            "#1782F#6P刚才在外面和乔儿擦身而过……\x02\x03",

            "#1780F她在哭哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #72
        0x11,
        (
            "#733F#11P哎～……不是……\x01",
            "那、那是因为～……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_248F():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFEA0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_248F)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_8C(0x12, 330, 500)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)
    TurnDirection(0x12, 0x11, 400)
    Sleep(300)

    ChrTalk(    #73
        0x12,
        "#1783F#6P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x11,
        "#734F#11P（好恐怖！　别这么面无表情的！！）\x02",
    )

    CloseMessageWindow()

    def lambda_254D():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_254D)
    FadeToDark(2000, 0, -1)
    OP_0D()

    label("loc_2562")

    ClearParty()
    AddParty(0x4, 0xEE, 0xFF)
    OP_BB(0x4, 0x1, 0x4)
    OP_BD()
    Sleep(1000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1404 end

    def Function_11_2581(): pass

    label("Function_11_2581")

    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)

    def lambda_2591():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_2591)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_11_2581 end

    SaveToFile()

Try(main)
