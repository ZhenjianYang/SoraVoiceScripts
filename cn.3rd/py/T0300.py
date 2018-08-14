from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0300.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
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
        '约修亚',                               # 9
        '缇欧',                                 # 10
        '伊莉莎',                               # 11
        '蜂',                                   # 12
        '目标用照相机',                         # 13
        '艾利兹大道方向',                       # 14
        '',                                     # 15
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
        'ED6_DT07/CH02750 ._CH',             # 00
        'ED6_DT07/CH02740 ._CH',             # 01
        'ED6_DT07/CH02730 ._CH',             # 02
        'ED6_DT09/CH10270 ._CH',             # 03
        'ED6_DT07/CH02220 ._CH',             # 04
        'ED6_DT26/CH20339 ._CH',             # 05
        'ED6_DT26/CH20787 ._CH',             # 06
        'ED6_DT26/CH20788 ._CH',             # 07
        'ED6_DT26/CH20789 ._CH',             # 08
        'ED6_DT26/CH20794 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
        'ED6_DT07/CH02740P._CP',             # 01
        'ED6_DT07/CH02730P._CP',             # 02
        'ED6_DT09/CH10270P._CP',             # 03
        'ED6_DT07/CH02220P._CP',             # 04
        'ED6_DT26/CH20339P._CP',             # 05
        'ED6_DT26/CH20787P._CP',             # 06
        'ED6_DT26/CH20788P._CP',             # 07
        'ED6_DT26/CH20789P._CP',             # 08
        'ED6_DT26/CH20794P._CP',             # 09
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
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
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
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


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_22D",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_3B7",          # 03, 3
        "Function_4_1911",         # 04, 4
        "Function_5_37C8",         # 05, 5
        "Function_6_3819",         # 06, 6
        "Function_7_388E",         # 07, 7
        "Function_8_38DB",         # 08, 8
        "Function_9_3943",         # 09, 9
        "Function_10_39B8",        # 0A, 10
        "Function_11_3A05",        # 0B, 11
        "Function_12_3ABD",        # 0C, 12
        "Function_13_3AD4",        # 0D, 13
        "Function_14_3CCC",        # 0E, 14
        "Function_15_563B",        # 0F, 15
        "Function_16_56B3",        # 10, 16
        "Function_17_5766",        # 11, 17
        "Function_18_57EB",        # 12, 18
        "Function_19_5899",        # 13, 19
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1DC")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_22C")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1FB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_22C")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_21A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_22C")

    label("loc_21A")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_22C")

    Return()

    # Function_0_1BA end

    def Function_1_22D(): pass

    label("Function_1_22D")

    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    Return()

    # Function_1_22D end

    def Function_2_23A(): pass

    label("Function_2_23A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3A1")

    label("loc_25F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3A1")

    label("loc_278")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3A1")

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3A1")

    label("loc_2AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3A1")

    label("loc_2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3A1")

    label("loc_2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3A1")

    label("loc_2F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3A1")

    label("loc_30E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3A1")

    label("loc_327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3A1")

    label("loc_340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3A1")

    label("loc_359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3A1")

    label("loc_372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3A1")

    label("loc_38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3A1")

    label("loc_3B6")

    Return()

    # Function_2_23A end

    def Function_3_3B7(): pass

    label("Function_3_3B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(450)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 1)
    SetChrPos(0x101, -3600, 0, -5600, 0)
    OP_6D(-17750, 0, -430, 0)
    OP_67(0, 5550, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    Sleep(2000)
    Sleep(500)

    def lambda_44E():
        OP_6B(3130, 5000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_44E)

    def lambda_45E():
        OP_67(0, 6050, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45E)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    WaitChrThread(0x14, 0x0)

    ChrTalk(    #0
        0x10,
        (
            "#1676F#5P#40W………………………………\x02\x03",

            "#1675F…………那时候，我…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E5():
        OP_6D(-12270, 0, -3050, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4E5)

    def lambda_4FD():
        OP_6C(160000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4FD)
    Sleep(3500)

    NpcTalk(    #1
        0x101,
        "活泼的声音",
        "#4P咦，不在了……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x101,
        "活泼的声音",
        (
            "#4P真是的，明明受了伤，\x01",
            "还随便到处乱跑～！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #3
        0x101,
        "活泼的声音",
        (
            "#4P约修亚～！\x01",
            "你去了哪里啊～！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x101,
        "活泼的声音",
        "#4P约修亚～！\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x101, -3600, 0, -7600, 90)

    def lambda_5F4():
        OP_8E(0xFE, 0xFFFFE796, 0x0, 0xFFFFE336, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F4)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 160, 400)
    Sleep(700)
    OP_8C(0x101, 340, 400)
    Sleep(300)

    def lambda_62C():
        OP_8E(0xFE, 0xFFFFD814, 0x0, 0xFFFFF7D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62C)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 25, 400)
    Sleep(700)
    TurnDirection(0x101, 0x10, 400)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        (
            "#293F#5P啊，约修亚！\x01",
            "你在这里啊。\x02\x03",

            "#292F都叫你不要勉强啦！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C9():
        OP_6D(-16780, 0, -260, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6C9)

    def lambda_6E1():
        OP_6C(168000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6E1)

    def lambda_6F1():
        OP_8E(0xFE, 0xFFFFCACC, 0x0, 0xFFFFFE34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #6
        0x10,
        (
            "#1676F#5P………………………………\x02\x03",

            "#1676F…………我已经没事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#293F#5P咦…………真的？\x02\x03",

            "……烧已经退了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#1676F#5P……只是伴随负伤产生的暂时性发热。\x02\x03",

            "今天早晨就退了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#293F#5P是吗…………\x02\x03",

            "#290F呼～，太好了……\x02\x03",

            "约修亚一直在\x01",
            "做噩梦呢。\x02\x03",

            "真担心\x01",
            "你会不会有事。\x02",
        )
    )

    Jump("loc_874")

    label("loc_874")

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    Sleep(200)

    ChrTalk(    #10
        0x10,
        (
            "#1671F#5P………………………………\x02\x03",

            "……我……说了什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#293F#5P…………哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#1675F#5P……不，没什么。\x02\x03",

            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_938():
        OP_6B(3030, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_938)

    def lambda_948():
        OP_8E(0xFE, 0xFFFFC7FC, 0x0, 0x82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_948)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_972():
        OP_96(0xFE, 0xFFFFC324, 0x3B6, 0x44C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_972)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_99A():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_99A)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #13
        0x101,
        (
            "#290F嗯…………\x02\x03",

            "既然退烧了，\x01",
            "那我们一起玩吧。\x02\x03",

            "你一直躺在床上，\x01",
            "很无聊吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #14
        0x10,
        "#1674F#11P………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#291F嗯嗯，我明白我明白。\x02\x03",

            "我发烧的时候\x01",
            "也是无聊得要死呢。\x02\x03",

            "#293F啊，\x01",
            "不过约修亚脚受伤了，\x01",
            "还不能跑吧……\x02\x03",

            "#296F唔……那么\x01",
            "踢罐子和捉迷藏也都不行……\x02",
        )
    )

    Jump("loc_B12")

    label("loc_B12")

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        "#1676F#11P…………………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #17
        0x10,
        (
            "#1676F#5P你想玩的话，\x01",
            "自己玩就好了。\x02\x03",

            "#1671F不要接近我。\x02\x03",

            "#1671F……这里应该\x01",
            "也很快会有危险了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#293F哎…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1676F#5P感谢你帮我包扎伤口。\x01",
            "真是太麻烦你们了。\x02\x03",

            "……也替我转达给\x01",
            "卡西乌斯·布莱特吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #20
        0x101,
        (
            "#293F………………………………\x02\x03",

            "#292F#3S不行哦，\x01",
            "不准摆这副表情！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #21
        0x10,
        "#1678F#11P咦………………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#290F没精神的时候，\x01",
            "最好做自己喜欢的事情。\x02\x03",

            "#291F好，你等一下哦。\x01",
            "我这就拿好东西来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D58():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D58)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_D7D():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D7D)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_DA5():
        OP_8E(0xFE, 0xFFFFE41C, 0x0, 0xFFFFEF70, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA5)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(3000)
    OP_63(0x10)

    ChrTalk(    #23
        0x10,
        (
            "#1675F#5P（现在还没有追兵的气息。）\x02\x03",

            "#1676F（找到这里的话，\x01",
            "  大概还要两三天吗……）\x02\x03",

            "（再等三天…………）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x10, 1)
    Sleep(800)

    def lambda_E8D():
        OP_8E(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E8D)
    Sleep(700)

    ChrTalk(    #24 op#A
        0x101,
        "#291F#12A#12P约修亚～……！\x02",
    )

    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_EDE():
        OP_96(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EDE)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_F06():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F06)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #25
        0x101,
        (
            "#290F来，这个给你。\x02\x03",

            "打起精神来嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05艾丝蒂尔拿出『团子虫』。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #27
        0x10,
        (
            "#1671F#11P…………………………………？\x02\x03",

            "（…………莫名其妙……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#291F看，很可爱吧？\x02\x03",

            "戳一下就会变成一团哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#1676F#11P……不要啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#293F咦，为什么？\x01",
            "明明这么可爱～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1670F#11P这种东西，我不需要。\x02\x03",

            "还有，不要再来这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#296F唔，\x01",
            "你不喜欢这种虫啊……\x02",
        )
    )

    Jump("loc_110F")

    label("loc_110F")

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#1678F#11P…………不，\x01",
            "不是这个意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#291F你等一下。\x01",
            "我去取那个盒子来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1179():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1179)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_119E():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119E)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_11C6():
        OP_8E(0xFE, 0xFFFFE41C, 0x0, 0xFFFFEF70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C6)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #35
        0x10,
        "#1674F#11P……………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)
    Sleep(1000)

    def lambda_1222():
        OP_8E(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1222)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_1247():
        OP_96(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1247)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_126F():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_126F)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #36
        0x101,
        "#292F约修亚，这个怎么样！！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#291F#3S『鬼蜻蜓』！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#1676F#5P都说了，我不要……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#292F那，这个！\x01",
            "这个绝对没问题！\x02\x03",

            "你一定会喜欢的！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #40
        0x101,
        "#291F#3S『玛鲁加大蜥蜴』！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#1676F#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #42
        0x101,
        "#294F#3S连这个也不行吗！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(800)

    ChrTalk(    #43
        0x10,
        (
            "#1675F#11P……那个，\x01",
            "我不是说每种虫子有什么不好……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_145B():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_145B)
    Sleep(500)

    ChrTalk(    #44
        0x101,
        (
            "#292F呜呜…………！\x02\x03",

            "#294F这个可是我\x01",
            "最喜欢的啊～！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1671F#11P（……怎么了，这女孩……？）\x02\x03",

            "（从刚才就一直莫名其妙的……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#292F……约修亚，\x01",
            "你在这里坐一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#1671F#11P…………正坐着呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#290F约修亚你……\x01",
            "喜欢什么样的虫子呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15AC():
        OP_6B(2980, 100)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15AC)

    ChrTalk(    #49
        0x101,
        (
            "#291F喜欢大的！？\x01",
            "还是喜欢漂亮的！？\x02",
        )
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_15FE():
        OP_6B(2930, 100)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15FE)

    ChrTalk(    #50
        0x101,
        (
            "#291F#3S喜欢脚多的！？\x01",
            "还是喜欢触角长的！？\x02",
        )
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1657():
        OP_6B(2880, 100)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1657)

    ChrTalk(    #51
        0x101,
        (
            "#291F#4S要有壳的？　有翅膀的？\x01",
            "还是有蹼的！？\x02",
        )
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#1671F#11P…………………………\x02\x03",

            "…………我不要什么虫。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16FC():
        OP_6B(3030, 1000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16FC)

    ChrTalk(    #53 op#A
        0x101,
        "#293F#5S#15A（打击）——！！#2S#240W\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x3E8)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0x101,
        (
            "#295F呜呜，也就是说…………\x02\x03",

            "不是能让人大吃一惊的东西\x01",
            "果然是不行啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#294F……好，你等着。\x02\x03",

            "我去给你抓来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17EB():
        OP_6D(-14780, 0, -2260, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_17EB)

    def lambda_1803():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1803)

    def lambda_181B():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_181B)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_1840():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1840)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_1868():
        OP_8E(0xFE, 0xFFFFCF86, 0x0, 0xFFFFFE2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1868)
    WaitChrThread(0x101, 0x1)

    def lambda_1888():
        OP_8E(0xFE, 0xFFFFE228, 0x0, 0xFFFFC8EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1888)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #56
        0x10,
        (
            "#1674F#11P…………………………\x02\x03",

            "……那女孩，喜欢虫子？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R0100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3B7 end

    def Function_4_1911(): pass

    label("Function_4_1911")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 1)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrPos(0x101, -8029, 0, -8280, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_6D(-16780, 0, -260, 0)
    OP_67(0, 6050, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(168000, 0)
    OP_6E(262, 0)
    OP_1D(0xB7)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x10,
        (
            "#1675F#5P………………………………\x02\x03",

            "（唉，这种气氛还真是平静啊。）\x02\x03",

            "（多少次穿越生死线，\x01",
            "  这种状况还是头一次遇到……）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #58
        0x101,
        "活泼的声音",
        "#4P#3S约修亚～！#2S\x02",
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x96, 0x1)
    Sleep(1200)

    ChrTalk(    #59
        0x10,
        "#1671F#5P…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_1AB3():
        OP_8E(0xFE, 0xFFFFCF86, 0x0, 0xFFFFFE2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AB3)
    WaitChrThread(0x101, 0x1)

    def lambda_1AD3():
        OP_8E(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AD3)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #60 op#A
        0x101,
        "#290F#10A#6P怎么样！\x02",
    )

    SetChrFlags(0x101, 0x4)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_1B1D():
        OP_96(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B1D)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_1B45():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B45)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #61
        0x101,
        (
            "#291F喏，你看你看！\x01",
            "好有趣的脸！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #62
        0x10,
        (
            "#1670F#11P…………都说了，\x01",
            "我不要啦。\x02\x03",

            "你还真是不吸取教训……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#294F命名为『惊吓人面蛾』！\x01",
            "因为翅膀上的花纹像人脸一样！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#1678F#11P……………………………………\x02\x03",

            "（…………什么啊这是……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#291F啊哈哈！\x01",
            "吓一跳吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(150)
    SetChrSubChip(0x10, 16)
    Sleep(500)

    ChrTalk(    #66
        0x10,
        "#1677F#5P…………没有啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #67
        0x101,
        (
            "#291F嗯嗯，\x01",
            "姐姐的努力终于有回报了～☆\x02\x03",

            "#290F好，\x01",
            "下次要抓更厉害的来给你看哦！\x02",
        )
    )

    Jump("loc_1D64")

    label("loc_1D64")

    CloseMessageWindow()

    def lambda_1D6B():
        OP_6D(-14780, 0, -2260, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1D6B)

    def lambda_1D83():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1D83)

    def lambda_1D9B():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D9B)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_1DC0():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DC0)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_1DE8():
        OP_8E(0xFE, 0xFFFFCF86, 0x0, 0xFFFFFE2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DE8)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #68 op#A
        0x101,
        "#291F#6P#15A呀嗬——！\x02",
    )


    def lambda_1E2A():
        OP_8E(0xFE, 0xFFFFE228, 0x0, 0xFFFFC8EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E2A)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #69
        0x10,
        "#1675F#5P真是个吵闹的女孩……\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    ClearChrFlags(0x101, 0x4)
    SetChrPos(0x101, -8029, 0, -8280, 0)
    SetChrSubChip(0x10, 1)
    OP_6D(-16780, 0, -260, 0)
    OP_67(0, 6050, -10000, 0)
    SoundLoad(373)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #70
        0x101,
        "活泼的声音",
        "#4P……约…………亚～！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #71
        0x10,
        "#1677F#5P…………回来了……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 3100, -500, -37490, 0)
    SetChrPos(0x101, 3100, -1000, -37490, 0)
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1F92():
        OP_6D(1870, -1000, -24530, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1F92)

    def lambda_1FAA():
        OP_6C(180000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FAA)
    Sleep(4000)

    def lambda_1FBF():
        OP_8E(0xFE, 0x7A8, 0xFFFFFC18, 0xFFFFB55A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FBF)
    Sleep(1000)

    ChrTalk(    #72 op#A
        0x101,
        "#294F#15A#6P#3S约修亚～！！\x02",
    )


    def lambda_2006():
        OP_8E(0xFE, 0x7A8, 0x1F4, 0xFFFFD1DE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2006)
    OP_43(0x13, 0x2, 0x0, 0xC)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_2032():
        OP_96(0xFE, 0x7A8, 0x0, 0xFFFFC005, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2032)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_205A():
        OP_8E(0xFE, 0x7A8, 0x0, 0xFFFFCA0E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_205A)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x13, 0x1)
    Fade(1000)
    OP_6D(-14050, 0, 450, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(192000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -9970, 0, -11460, 335)
    SetChrPos(0x13, -9970, 500, -11460, 335)

    def lambda_20E3():
        OP_8E(0xFE, 0xFFFFC950, 0x0, 0x53C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20E3)
    Sleep(600)
    OP_43(0x13, 0x3, 0x0, 0xB)
    Sleep(200)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x64, 0x1)
    SetChrSubChip(0x10, 8)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #73 op#A
        0x101,
        "#15A#3S……跳进去！#2S\x02",
    )

    SetChrFlags(0x101, 0x4)

    def lambda_2157():
        TurnDirection(0xFE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2157)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_216A():
        OP_96(0xFE, 0xFFFFC1C6, 0x3B6, 0x6B8, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_216A)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_2192():
        OP_8F(0xFE, 0xFFFFBB90, 0x3B6, 0x776, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2192)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #74 op#A
        0x10,
        "#15A#2P咦……！？\x02",
    )

    LoadEffect(0x0, "map\\mp012_00.eff")
    LoadEffect(0x1, "map\\sibuki0.eff")
    LoadEffect(0x2, "map\\mp013_02.eff")

    def lambda_220E():
        OP_6D(-15600, -3000, 4510, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_220E)

    def lambda_2226():
        OP_6C(180000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2226)

    def lambda_2236():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2236)

    def lambda_2244():
        OP_8E(0xFE, 0xFFFFBD02, 0x3B6, 0xE7E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2244)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrPos(0x10, -18120, 800, 1800, 315)

    def lambda_227F():
        OP_8F(0xFE, 0xFFFFBAAA, 0x3B6, 0xE10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_227F)
    WaitChrThread(0x101, 0x1)

    def lambda_229F():
        OP_8C(0xFE, 215, 100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_229F)

    def lambda_22AD():
        OP_8C(0xFE, 215, 100)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_22AD)
    OP_22(0xA3, 0x0, 0x5A)

    def lambda_22C0():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF448, 0x26B6, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22C0)

    def lambda_22DE():
        OP_96(0xFE, 0xFFFFC0EB, 0xFFFFF448, 0x2472, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_22DE)
    Sleep(200)
    ClearChrFlags(0x101, 0x1)
    Sleep(100)
    ClearChrFlags(0x10, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_22(0xE4, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -15040, -2500, 9910, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -16149, -2500, 9330, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, -15040, -1700, 9910, 0, 0, 0, 700, 700, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0xFF, -16149, -1700, 9330, 0, 0, 0, 700, 700, 500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x96, 0xBB8, 0x3E8)
    Sleep(6000)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x4, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0xFF, -16149, -1700, 9330, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    Sleep(4000)

    def lambda_2484():
        OP_6D(-15660, -3000, 6510, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2484)
    Sleep(4000)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFF, -15040, -2200, 9910, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_43(0x101, 0x0, 0x0, 0x6)

    ChrTalk(    #75
        0x101,
        (
            "#293F#6P呼哇…………！\x02\x03",

            "#291F啊哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, -16149, -2200, 9330, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0xFF, -16149, -1700, 9330, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_43(0x10, 0x0, 0x0, 0x9)

    ChrTalk(    #76
        0x10,
        (
            "#1673F#5P……呼…………！\x02\x03",

            "#1677F呼、呼…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    OP_8C(0x10, 35, 400)
    Sleep(500)

    ChrTalk(    #77
        0x10,
        "#1672F#11P#3S……你干什么啊！\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#293F#6P嗯…………？\x02\x03",

            "#291F啊哈哈哈哈！\x02\x03",

            "来啊来啊！\x01",
            "来打水仗吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x0)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -15040, -2200, 9910, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -15540, -2200, 9610, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2771():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF6A0, 0x26B6, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2771)
    Sleep(500)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -15040, -2200, 9910, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -15540, -2200, 9610, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x7, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2838():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF6A0, 0x26B6, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2838)
    WaitChrThread(0xEE, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x7)
    OP_82(0x2, 0x2)

    ChrTalk(    #79
        0x10,
        "#1675F#11P……呜…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#290F#6P啊，好舒服……\x02\x03",

            "#291F啊，对了。\x01",
            "来钓鱼吧。\x02\x03",

            "虽然我也喜欢玩水，\x01",
            "不过还是钓鱼更有趣呢。\x02\x03",

            "#292F好，\x01",
            "把今天午饭要吃的东西钓上来吧！\x02",
        )
    )

    Jump("loc_2932")

    label("loc_2932")

    CloseMessageWindow()

    def lambda_2939():

        label("loc_2939")

        TurnDirection(0xFE, 0x101, 500)
        OP_48()
        Jump("loc_2939")

    QueueWorkItem2(0x10, 3, lambda_2939)
    OP_8C(0x101, 135, 400)
    OP_82(0x7, 0x2)
    OP_44(0x101, 0x0)

    def lambda_2958():
        OP_8E(0xFE, 0xFFFFC996, 0xFFFFF6A0, 0x2012, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2958)
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x101, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_82(0x7, 0x2)
    Sleep(500)
    OP_82(0x6, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x13, 0x0)
    OP_82(0x5, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x8)
    PlayEffect(0x2, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x4, 0x2)
    TurnDirection(0x101, 0x10, 500)
    OP_44(0x10, 0x3)

    ChrTalk(    #81
        0x101,
        (
            "#290F#5P来，约修亚也上来吧。\x02\x03",

            "不赶快换衣服的话会感冒的哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        "#1670F#12P…………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x10, 0xFF)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x10, 0x20)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x10, 0x1)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 1)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrPos(0x101, -12550, 0, 7600, 135)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)

    def lambda_2AEE():

        label("loc_2AEE")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2AEE")

    QueueWorkItem2(0x101, 2, lambda_2AEE)
    OP_6D(-15360, 0, 4470, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(178000, 0)
    OP_6E(262, 0)
    SoundLoad(450)
    LoadEffect(0x7, "map\\mp013_02.eff")
    LoadEffect(0x2, "map\\mp071_01.eff")
    LoadEffect(0x3, "map\\mp071_02.eff")
    LoadEffect(0x4, "map\\mp071_03.eff")
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_2BF6():
        OP_99(0xFE, 0x4, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BF6)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #83
        0x101,
        (
            "#291F钓到了，是大家伙！\x02\x03",

            "这是约修亚的份哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #84
        0x10,
        "#1676F#6P我的份……不用了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#291F接下来要钓我的。\x02\x03",

            "#294F没钓上来就不吃午饭！！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_2D4E():

        label("loc_2D4E")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2D4E")

    QueueWorkItem2(0x101, 2, lambda_2D4E)
    Sleep(300)
    OP_22(0x19, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #86
        0x10,
        (
            "#1674F#6P………………………………\x02\x03",

            "#1677F（真是的………\x01",
            "  完全不听别人说话……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x0, 0x2)

    def lambda_2E2D():

        label("loc_2E2D")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_2E2D")

    QueueWorkItem2(0x101, 2, lambda_2E2D)
    OP_43(0x101, 0x3, 0x0, 0xD)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #87
        0x101,
        (
            "#292F哦，来了来了！\x02\x03",

            "#294F喝啊～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_2EBD():
        OP_99(0xFE, 0x6, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EBD)
    OP_22(0x18, 0x0, 0x64)
    OP_44(0x101, 0x3)
    OP_82(0x1, 0x0)
    OP_82(0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #88
        0x101,
        (
            "#293F啊，是银伞鱼。\x02\x03",

            "#296F唔，好小。\x01",
            "这个就给老爸吧……\x02\x03",

            "#292F那个不良中年，\x01",
            "肯定又在哪儿闲逛呢。\x01",
            "这是理所当然的惩罚！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x96, 0x1)
    Sleep(1200)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #89
        0x10,
        "#1678F#12P咦………………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#291F接下来就是我的了。\x01",
            "我的午饭！\x02\x03",

            "咿——呀～～～！ \x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_307D():

        label("loc_307D")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_307D")

    QueueWorkItem2(0x101, 2, lambda_307D)
    Sleep(300)
    OP_22(0x19, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    OP_63(0x10)

    ChrTalk(    #91
        0x10,
        (
            "#1678F#12P（这女孩，\x01",
            "  不知道卡西乌斯·布莱特的事吗…………）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #92
        0x10,
        (
            "#1675F#6P（什么也不对女儿说。\x01",
            "  倒也像是他的风格……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_318B():

        label("loc_318B")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_318B")

    QueueWorkItem2(0x101, 2, lambda_318B)
    OP_43(0x101, 0x3, 0x0, 0xD)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_31DF():

        label("loc_31DF")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_31DF")

    QueueWorkItem2(0x101, 2, lambda_31DF)
    OP_44(0x101, 0x3)
    OP_82(0x1, 0x0)
    OP_82(0x0, 0x2)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #93
        0x101,
        (
            "#293F啊啊，被逃掉了！\x02\x03",

            "#294F可恶——！！\x01",
            "下次！　下次一定要钓到！！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #94
        0x10,
        "#1671F………………………………\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x7, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)

    ChrTalk(    #95
        0x101,
        (
            "#293F嗯，上钩了！\x02\x03",

            "#296F不，不对……\x01",
            "只是碰了一下而已……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_20(0x1F40)
    Sleep(2000)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #96
        0x10,
        "#1678F#6P……………………？\x02",
    )

    CloseMessageWindow()

    def lambda_33DE():
        OP_6D(-17520, 400, 2520, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_33DE)

    def lambda_33F6():
        OP_6C(198000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33F6)
    WaitChrThread(0x14, 0x0)
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #97
        0x10,
        "#1675F我说啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#293F嗯…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #99
        0x101,
        "#290F………………什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        "#1675F没什么………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 16)
    OP_0D()

    def lambda_34D6():
        OP_6D(-20940, 0, -1000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_34D6)

    def lambda_34EE():
        OP_6C(194000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_34EE)
    Sleep(3000)
    OP_63(0x101)
    WaitChrThread(0x14, 0x0)
    Fade(3000)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -21270, 800, 2220, 0)
    SetChrFlags(0x101, 0x8)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(3000)
    OP_23(0x1C2)
    Sleep(1500)

    ChrTalk(    #101
        0x10,
        (
            "#1678F#40W（为什么…………\x01",
            "#5W  #40W……这么亮……？）\x02\x03",

            "#1675F#40W（绿色……好耀眼………）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(1000)
    Fade(1000)
    OP_6D(-14110, 0, 4950, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(178000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -12550, 0, 7600, 135)
    ClearChrFlags(0x101, 0x8)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3648():

        label("loc_3648")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_3648")

    QueueWorkItem2(0x101, 2, lambda_3648)
    OP_43(0x101, 0x3, 0x0, 0xD)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #102
        0x101,
        (
            "#294F啊，来啦！！\x01",
            "这次一定是大家伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#292F好，午饭到手了！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_36F3():
        OP_99(0xFE, 0x6, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36F3)
    OP_22(0x18, 0x0, 0x64)
    OP_44(0x101, 0x3)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #104
        0x101,
        "#293F#3S咦，怎么这么小！？#2S\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    Call(0, 14)
    Return()

    # Function_4_1911 end

    def Function_5_37C8(): pass

    label("Function_5_37C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3818")
    OP_22(0x18, 0x0, 0x50)
    OP_22(0x22, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0x101, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("Function_5_37C8")

    label("loc_3818")

    Return()

    # Function_5_37C8 end

    def Function_6_3819(): pass

    label("Function_6_3819")

    SetChrFlags(0xFE, 0x20)

    def lambda_3824():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF6A0, 0x26B6, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3824)
    WaitChrThread(0xFE, 0x1)

    label("loc_3841")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_388D")

    def lambda_3850():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3850)
    WaitChrThread(0xFE, 0x1)

    def lambda_3870():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3870)
    WaitChrThread(0xFE, 0x1)
    Jump("loc_3841")

    label("loc_388D")

    Return()

    # Function_6_3819 end

    def Function_7_388E(): pass

    label("Function_7_388E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38DA")

    def lambda_389D():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_389D)
    WaitChrThread(0xFE, 0x1)

    def lambda_38BD():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38BD)
    WaitChrThread(0xFE, 0x1)
    Jump("Function_7_388E")

    label("loc_38DA")

    Return()

    # Function_7_388E end

    def Function_8_38DB(): pass

    label("Function_8_38DB")


    def lambda_38E1():
        OP_8F(0xFE, 0xFFFFCC34, 0xFFFFF6A0, 0x1C02, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38E1)

    label("loc_38F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3942")

    def lambda_3905():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3905)
    WaitChrThread(0xFE, 0x1)

    def lambda_3925():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3925)
    WaitChrThread(0xFE, 0x1)
    Jump("loc_38F6")

    label("loc_3942")

    Return()

    # Function_8_38DB end

    def Function_9_3943(): pass

    label("Function_9_3943")

    SetChrFlags(0xFE, 0x20)

    def lambda_394E():
        OP_96(0xFE, 0xFFFFC0EB, 0xFFFFF6A0, 0x2472, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_394E)
    WaitChrThread(0xFE, 0x1)

    label("loc_396B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39B7")

    def lambda_397A():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_397A)
    WaitChrThread(0xFE, 0x1)

    def lambda_399A():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_399A)
    WaitChrThread(0xFE, 0x1)
    Jump("loc_396B")

    label("loc_39B7")

    Return()

    # Function_9_3943 end

    def Function_10_39B8(): pass

    label("Function_10_39B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A04")

    def lambda_39C7():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39C7)
    WaitChrThread(0xFE, 0x1)

    def lambda_39E7():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39E7)
    WaitChrThread(0xFE, 0x1)
    Jump("Function_10_39B8")

    label("loc_3A04")

    Return()

    # Function_10_39B8 end

    def Function_11_3A05(): pass

    label("Function_11_3A05")


    def lambda_3A0B():
        OP_8E(0xFE, 0xFFFFC75C, 0x1F4, 0x1A4A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A0B)
    WaitChrThread(0xFE, 0x1)

    def lambda_3A2B():
        OP_8E(0xFE, 0xFFFFC022, 0xFFFFF830, 0x1766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A2B)
    WaitChrThread(0xFE, 0x1)
    OP_97(0xFE, 0xFFFFC3C4, 0x1DB0, 0xAFC80, 0x898, 0x1)
    OP_43(0xFE, 0x2, 0x0, 0x2)

    def lambda_3A67():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_3A67)
    Sleep(2000)
    OP_44(0xFE, 0x2)

    def lambda_3A7E():
        OP_8E(0xFE, 0xFFFFC75C, 0x1F4, 0x1A4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A7E)
    WaitChrThread(0xFE, 0x1)

    def lambda_3A9E():
        OP_8E(0xFE, 0xFFFFDE9A, 0x1F4, 0xFFFFCC48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A9E)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_11_3A05 end

    def Function_12_3ABD(): pass

    label("Function_12_3ABD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AD3")
    OP_22(0x175, 0x0, 0x64)
    Sleep(3500)
    Jump("Function_12_3ABD")

    label("loc_3AD3")

    Return()

    # Function_12_3ABD end

    def Function_13_3AD4(): pass

    label("Function_13_3AD4")

    PlayEffect(0x2, 0xFF, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_3B09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CCB")
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Jump("loc_3B09")

    label("loc_3CCB")

    Return()

    # Function_13_3AD4 end

    def Function_14_3CCC(): pass

    label("Function_14_3CCC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x101, 10730, 0, -9920, 245)
    OP_6D(3330, -1000, -32130, 0)
    OP_67(0, 7980, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #105 op#A op#5
        "\x18\x07\x00#35A#40W――The Second Week.　\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0xF)
    SetChrPos(0x11, 4410, -1000, -40080, 0)
    SetChrPos(0x12, 3370, -1000, -40080, 0)

    def lambda_3DAE():
        OP_8E(0xFE, 0x79E, 0xFFFFFC18, 0xFFFFAAB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3DAE)
    Sleep(100)

    def lambda_3DCE():
        OP_8E(0xFE, 0xBEA, 0xFFFFFC18, 0xFFFFAAB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3DCE)
    Sleep(2000)

    def lambda_3DEE():
        OP_6D(3310, -1000, -22600, 7500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3DEE)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #106 op#A
        0x12,
        "#11P#22A怎么回事呢……\x02",
    )

    Sleep(2000)

    ChrTalk(    #107
        0x12,
        "#11P昨天也没来店里……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #108
        0x11,
        (
            "#5P哎，反正艾丝蒂尔\x01",
            "总是一会儿一个主意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x11,
        (
            "#5P应该不用\x01",
            "怎么替她担心吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        (
            "#11P不过，\x01",
            "以前可是每天都来玩的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F03():
        OP_8E(0xFE, 0x5AA, 0x0, 0xFFFFC9F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3F03)
    OP_8C(0x11, 0, 400)

    def lambda_3F25():
        OP_8E(0xFE, 0x9F6, 0x0, 0xFFFFC9F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3F25)
    Sleep(1000)
    Fade(1000)
    OP_6D(2000, 0, -9910, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(3760, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_3F87():
        OP_6D(2000, 0, -5910, 2500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3F87)

    def lambda_3F9F():
        OP_67(0, 3880, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3F9F)
    Sleep(1000)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #111
        0x12,
        "#5P#3S艾丝蒂尔，在吗～？\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #112
        0x12,
        "#5P#3S艾丝蒂尔——！\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    OP_63(0x11)
    Sleep(500)
    OP_8C(0x12, 315, 400)
    Sleep(600)
    OP_8C(0x12, 45, 400)
    Sleep(600)
    OP_8C(0x12, 0, 400)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x12, 0x11, 400)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #113
        0x12,
        (
            "#1P该、该不会，\x01",
            "是被坏人给绑架了吧～！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        (
            "#2P……这么说的话，\x01",
            "被魔兽袭击而身负重伤，\x01",
            "悲惨地横死在森林里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        "#2P……这种可能性倒是相当的高。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x12,
        "#1P#3S咦咦咦～！？\x02",
    )

    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        (
            "#2P那孩子平时\x01",
            "似乎就经常去危险的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x12, 0, 500)
    Sleep(300)

    ChrTalk(    #118
        0x12,
        "#1P艾、艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #119
        0x11,
        "#2P开玩笑的啦。\x02",
    )

    CloseMessageWindow()

    def lambda_4242():
        OP_8E(0xFE, 0x9F6, 0x0, 0xFFFFD152, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4242)
    Sleep(100)
    OP_8C(0x12, 0, 100)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #120
        0x11,
        (
            "#2P艾丝蒂尔～？\x01",
            "差不多该出来了吧——！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        "#2P伊莉莎要哭了哦～！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x10, -9980, 0, -2130, 245)

    NpcTalk(    #122
        0x10,
        "男孩子的声音",
        "#4P……要找艾丝蒂尔的话，她出去了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 4)
    SetChrPos(0x10, -17800, 940, 1840, 0)
    TurnDirection(0x12, 0x10, 500)
    Sleep(50)
    TurnDirection(0x11, 0x10, 500)

    def lambda_438B():
        OP_6D(-18040, 0, 2040, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_438B)

    def lambda_43A3():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_43A3)

    def lambda_43BB():
        OP_6C(304000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_43BB)

    def lambda_43CB():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_43CB)
    Sleep(2500)
    SetChrPos(0x11, -5820, 0, -5220, 305)
    SetChrPos(0x12, -6840, 0, -5940, 305)

    def lambda_4402():
        OP_8E(0xFE, 0xFFFFCBC6, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4402)
    Sleep(100)

    def lambda_4422():
        OP_8E(0xFE, 0xFFFFC87E, 0x0, 0xFFFFFC36, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4422)
    WaitChrThread(0x12, 0x1)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x11,
        "嗯嗯…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x12,
        "咦～…………？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10,
        "#1676F#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #126
        0x11,
        "…………谁！？\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #127
        0x12,
        "………你是谁啊～！？\x02",
    )

    CloseMessageWindow()

    def lambda_4535():
        OP_6B(3300, 3000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4535)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrSubChip(0x10, 1)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -16460, 950, 820, 315)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, -16480, 950, 2450, 250)
    ClearParty()
    AddParty(0x54, 0xEE, 0xFF)
    ClearChrFlags(0x155, 0x2)
    SetChrPos(0x155, 3070, -1000, -43370, 0)
    OP_6D(2990, -1000, -31230, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SoundLoad(142)

    def lambda_45ED():
        OP_6D(0, 0, -13320, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_45ED)

    def lambda_4605():
        OP_6C(134000, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4605)
    OP_43(0x155, 0x3, 0x0, 0xF)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #128 op#A
        0x155,
        "#290F#15A#3S#6P约修亚～！\x02",
    )

    Sleep(2700)

    ChrTalk(    #129 op#A
        0x155,
        (
            "#291F#25A#3S#5P看，我抓到\x01",
            "很厉害的虫子了哦！\x02",
        )
    )

    Sleep(2000)
    OP_59()
    Sleep(1000)
    OP_44(0x155, 0xFF)
    Fade(1000)
    OP_6D(-15700, 0, -1170, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(163000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, -5500, 0, -6460, 270)
    Sleep(1000)

    def lambda_46EF():
        OP_8E(0xFE, 0xFFFFC87E, 0x0, 0xFFFFFC22, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_46EF)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x10, 500)
    OP_62(0x155, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #130
        0x155,
        (
            "#293F#5P……咦，\x01",
            "缇欧和伊莉莎？\x02\x03",

            "#290F你们来了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x12, 0x155, 400)
    Sleep(50)
    OP_8C(0x11, 115, 400)

    ChrTalk(    #131
        0x12,
        "#2P啊，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x12,
        "#2P真是的，你之前都干什么去了～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x12,
        "#2P人家担心死了～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        "#12P对了，艾丝蒂尔，这孩子你认识？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x11,
        (
            "#12P刚才不管问他什么，\x01",
            "他都不回答呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x11,
        "#12P还说『我没义务回答你们』。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #137
        0x10,
        (
            "#1676F#5P………………艾丝蒂尔。\x02\x03",

            "#1671F这两人是你的朋友？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x155,
        (
            "#293F#5P哎，嗯。\x01",
            "怎么了…………？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #139
        0x10,
        (
            "#1676F#5P（和本人的说法一致啊。）\x02\x03",

            "（……到处都是破绽，\x01",
            "  看起来也不像受过训练的样子。）\x02\x03",

            "#1675F（还以为那些家伙\x01",
            "  差不多该找上门来了……）\x02\x03",

            "（看来不是这两人啊……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #140
        0x11,
        (
            "#12P从刚才开始就一直这个样子。\x01",
            "又是在洛连特没见过的生面孔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x11,
        (
            "#12P艾丝蒂尔，\x01",
            "你认识这孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x155,
        (
            "#293F#5P啊，嗯。\x01",
            "约修亚啊，其实是…………\x02\x03",

            "#291F#3S我弟弟呀！！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x64, 0x1)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0x10,
        "#1674F#5P（…………哎……！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12,
        "#2P咦，艾丝蒂尔的弟弟？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x12,
        (
            "#2P原、原来是这样啊。\x01",
            "呼，吓我一跳～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x11,
        (
            "#12P喂，艾丝蒂尔。\x01",
            "这算什么说明啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        (
            "#12P突然冒出个弟弟……\x01",
            "还是让人摸不着头脑啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x155,
        (
            "#291F#5P是真的嘛。\x02\x03",

            "对吧，约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x10,
        "#1676F#5P……哪有这种事。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrPos(0x10, -17820, 950, 1500, 315)
    Sleep(500)

    def lambda_4CBB():
        OP_6D(-13920, 0, -3730, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4CBB)

    def lambda_4CD3():
        OP_6C(180000, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4CD3)
    OP_43(0x10, 0x3, 0x0, 0x10)

    def lambda_4CEA():

        label("loc_4CEA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4CEA")

    QueueWorkItem2(0x155, 2, lambda_4CEA)
    Sleep(50)

    def lambda_4D00():

        label("loc_4D00")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4D00")

    QueueWorkItem2(0x11, 2, lambda_4D00)
    Sleep(50)

    def lambda_4D16():

        label("loc_4D16")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4D16")

    QueueWorkItem2(0x12, 2, lambda_4D16)
    Sleep(3000)

    ChrTalk(    #150 op#A
        0x155,
        (
            "#294F#11P#25A啊，约修亚！\x01",
            "给我慢着！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #151 op#A
        0x155,
        (
            "#292F#12P#15A唔唔……\x02\x03",

            "#20A给我好好\x01",
            "听姐姐说话啦！\x02",
        )
    )

    Jump("loc_4DA9")

    label("loc_4DA9")

    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #152
        0x10,
        (
            "#1675F#5P#40W……你这样的家伙\x01",
            "怎么可能是我姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x155,
        "#293F#12P咦…………？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(-13280, 0, -2140, 0)
    OP_67(0, 4040, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(    #154
        0x10,
        (
            "#1676F#6P我并不打算和你们混熟。\x02\x03",

            "我之所以会在这里……\x02\x03",

            "#1671F卡西乌斯·布莱特也说了吧。\x01",
            "……是『顺其自然』。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #155
        0x155,
        "#293F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10,
        (
            "#1675F#6P还有……\x02\x03",

            "你能不能别再\x01",
            "拿什么虫子来了。\x02\x03",

            "#1676F虽然不知道你在打什么主意，\x01",
            "管太多闲事可是会受伤的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)
    OP_8C(0x10, 140, 300)

    def lambda_4FDF():
        OP_8E(0xFE, 0xFFFFDAC6, 0x0, 0xFFFFE656, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4FDF)
    Sleep(900)

    def lambda_4FFF():
        OP_6D(-11530, 0, -5430, 1000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4FFF)

    def lambda_5017():
        OP_6C(286000, 1000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5017)

    def lambda_5027():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5027)

    def lambda_5037():
        OP_8E(0xFE, 0xFFFFD35A, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5037)
    WaitChrThread(0x155, 0x1)
    SetChrFlags(0x155, 0x4)

    ChrTalk(    #157 op#A
        0x155,
        "#294F#10A#2P呃！\x02",
    )

    OP_22(0xA3, 0x0, 0x46)

    def lambda_507D():
        OP_96(0xFE, 0xFFFFDAC6, 0x3E8, 0xFFFFE656, 0x578, 0x1388)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_507D)
    WaitChrThread(0x155, 0x1)
    OP_22(0x8E, 0x0, 0x55)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 3)

    ChrTalk(    #158 op#A
        0x10,
        "#1673F#3P#10A呜…………！？\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_50E7():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_50E7)
    Sleep(50)

    def lambda_5106():
        OP_96(0xFE, 0xFFFFD62A, 0x0, 0xFFFFEBEC, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5106)
    WaitChrThread(0x155, 0x1)
    Sleep(2000)
    OP_43(0x155, 0x3, 0x0, 0x11)
    Sleep(500)

    ChrTalk(    #159
        0x155,
        "#294F#11P哼，可恶可恶！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10,
        "#1673F好、好痛……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x155,
        (
            "#292F#11P在这个家里，\x01",
            "我可是前辈！\x02\x03",

            "#294F我就是姐姐！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        "#1675F好、好痛啊……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x4)
    OP_A2(0x0)
    WaitChrThread(0x155, 0x3)

    def lambda_51F6():
        OP_8E(0xFE, 0xFFFFD936, 0x0, 0xFFFFE854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_51F6)
    WaitChrThread(0x155, 0x1)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_523C():
        OP_96(0xFE, 0xFFFFDAC6, 0x12C, 0xFFFFE656, 0x12C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_523C)
    WaitChrThread(0x10, 0x1)

    def lambda_525F():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_525F)
    Sleep(300)

    ChrTalk(    #163
        0x155,
        (
            "#291F#11P怎～么样，我是姐姐吧？\x02\x03",

            "#100W我·是·你·的·大·姐·姐。\x01",
            "#20W来，快叫姐姐！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        "#1670F……不……不要。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x155,
        "#294F#11P#3S你说什么～！！#2S\x02",
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)
    ClearChrFlags(0x10, 0x4)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_534E():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_534E)

    def lambda_536C():
        OP_8F(0xFE, 0xFFFFD62A, 0x0, 0xFFFFEBEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_536C)
    WaitChrThread(0x155, 0x1)
    OP_A3(0x0)
    OP_43(0x155, 0x3, 0x0, 0x12)
    Sleep(3000)
    OP_A2(0x0)
    Fade(1000)
    OP_6D(-18550, 0, 2390, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(294000, 0)
    OP_6E(262, 0)
    OP_44(0x12, 0xFF)
    OP_44(0x11, 0xFF)
    OP_8C(0x12, 160, 0)
    OP_8C(0x11, 160, 0)

    def lambda_53F6():
        OP_8F(0xFE, 0xFFFFC23E, 0x3B6, 0x618, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_53F6)
    Sleep(1000)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #166
        0x12,
        "#5P你们关系真好啊～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        "#11P嗯，看起来是这样呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_44(0x155, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrFlags(0x155, 0x4)
    SetChrPos(0x155, -10400, 500, -5390, 114)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -10400, 500, -5390, 114)

    ChrTalk(    #168
        0x10,
        "#1670F#2P……你们两个，很吵呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #169
        0x155,
        "#291F#3S#2P有破绽！\x02",
    )

    CloseMessageWindow()
    OP_22(0x8E, 0x0, 0x55)
    OP_59()
    SetChrFlags(0x155, 0x800)
    SetChrPos(0x155, -10340, 400, -5310, 160)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 1)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -10290, -100, -4900, 160)

    def lambda_5562():
        OP_6D(-11800, 0, -4660, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5562)
    Sleep(1000)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_5584():
        OP_96(0xFE, 0xFFFFD558, 0x0, 0xFFFFEDE0, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5584)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x5A)
    Sleep(500)
    WaitChrThread(0x14, 0x0)

    ChrTalk(    #170
        0x155,
        (
            "#290F#5P约修亚，\x01",
            "从今天开始我就是姐姐了哦。\x02\x03",

            "#291F这事就这么定了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_560C():
        OP_6B(2870, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_560C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3CCC end

    def Function_15_563B(): pass

    label("Function_15_563B")

    SetChrFlags(0x101, 0x4)

    def lambda_5646():
        OP_8E(0xFE, 0x7D0, 0xFFFFFC18, 0xFFFFB55A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5646)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_566B():
        OP_96(0xFE, 0x7D0, 0x0, 0xFFFFC005, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_566B)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_5693():
        OP_8E(0xFE, 0xFFFFD8AA, 0x0, 0xFFFFF24A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5693)
    WaitChrThread(0x155, 0x1)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_15_563B end

    def Function_16_56B3(): pass

    label("Function_16_56B3")


    def lambda_56B9():
        OP_8E(0xFE, 0xFFFFBC44, 0x3B6, 0xDE8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56B9)
    WaitChrThread(0x10, 0x1)

    def lambda_56D9():
        OP_8E(0xFE, 0xFFFFC180, 0x3B6, 0xBF4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56D9)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_56FE():
        OP_96(0xFE, 0xFFFFC798, 0x0, 0xAAA, 0x190, 0x708)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56FE)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x5A)
    ClearChrFlags(0x10, 0x4)

    def lambda_572B():
        OP_8E(0xFE, 0xFFFFCAC2, 0x0, 0xA1E, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_572B)
    WaitChrThread(0x10, 0x1)

    def lambda_574B():
        OP_8E(0xFE, 0xFFFFD35A, 0x0, 0xFFFFEF34, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_574B)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_16_56B3 end

    def Function_17_5766(): pass

    label("Function_17_5766")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57EA")

    def lambda_5775():
        OP_8F(0xFE, 0xFFFFD936, 0x0, 0xFFFFE854, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5775)
    WaitChrThread(0x155, 0x1)
    OP_22(0x8E, 0x0, 0x55)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 3)

    def lambda_57A4():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_57A4)

    def lambda_57BE():
        OP_8F(0xFE, 0xFFFFD62A, 0x0, 0xFFFFEBEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_57BE)
    WaitChrThread(0x155, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_57E7")
    Jump("loc_57EA")

    label("loc_57E7")

    Jump("Function_17_5766")

    label("loc_57EA")

    Return()

    # Function_17_5766 end

    def Function_18_57EB(): pass

    label("Function_18_57EB")


    def lambda_57F1():
        OP_8F(0xFE, 0xFFFFD936, 0x0, 0xFFFFE854, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_57F1)
    WaitChrThread(0x155, 0x1)
    SetChrFlags(0x10, 0x20)

    label("loc_5810")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5898")
    OP_22(0x84, 0x0, 0x64)

    def lambda_5824():
        OP_97(0xFE, 0xFFFFD936, 0xFFFFE854, 0xFFFA81C0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5824)

    def lambda_5840():
        OP_8C(0xFE, 69, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_5840)
    WaitChrThread(0x155, 0x2)

    def lambda_5853():
        OP_8C(0xFE, 339, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_5853)
    WaitChrThread(0x155, 0x2)

    def lambda_5866():
        OP_8C(0xFE, 249, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_5866)
    WaitChrThread(0x155, 0x2)

    def lambda_5879():
        OP_8C(0xFE, 159, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_5879)
    WaitChrThread(0x155, 0x2)
    WaitChrThread(0x10, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5895")
    Jump("loc_5898")

    label("loc_5895")

    Jump("loc_5810")

    label("loc_5898")

    Return()

    # Function_18_57EB end

    def Function_19_5899(): pass

    label("Function_19_5899")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2140, 450, -1440, 180)
    SetChrPos(0x101, -5190, 0, -16790, 180)
    OP_6D(2800, 450, -4000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x3C)
    OP_73(0x0)

    def lambda_5929():
        OP_6D(2480, 0, -12740, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5929)

    def lambda_5941():
        OP_6B(2980, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5941)

    def lambda_5951():
        OP_67(0, 7500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_5951)

    def lambda_5969():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFCC70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5969)
    Sleep(1200)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_20(0x3E8)

    NpcTalk(    #171
        0x101,
        "惨叫",
        "#5P啊啊啊啊…………！？\x02",
    )

    Jump("loc_59D4")

    label("loc_59D4")

    OP_7C(0x5, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 225, 400)
    OP_1D(0x98)
    Sleep(500)

    ChrTalk(    #172
        0x10,
        (
            "#1678F#5P这声音是…………艾丝蒂尔！？\x02\x03",

            "#1670F难不成……发生了什么事？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10)

    ChrTalk(    #173
        0x10,
        (
            "#1677F#5P（不，既然是那女孩……\x01",
            "  很可能只是摔倒而已……）\x02\x03",

            "#1675F（不，但是…………）\x02\x03",

            "(………………………………)\x02\x03",

            "#1676F（无论如何……\x01",
            "  ……应该都跟我没关系……）\x02\x03",

            "（那女孩无论发生什么事，\x01",
            "  都跟我……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10, 9)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #174
        0x10,
        "#1672F#5P#4S可恶……！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/C0302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_5899 end

    SaveToFile()

Try(main)
