from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4202   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '黑衣人',                               # 9
        '目标用照相机',                         # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT09/CH11120 ._CH',             # 00
        'ED6_DT09/CH11121 ._CH',             # 01
        'ED6_DT09/CH11110 ._CH',             # 02
        'ED6_DT09/CH11111 ._CH',             # 03
        'ED6_DT09/CH11130 ._CH',             # 04
        'ED6_DT09/CH11131 ._CH',             # 05
        'ED6_DT09/CH10040 ._CH',             # 06
        'ED6_DT09/CH10041 ._CH',             # 07
        'ED6_DT09/CH11140 ._CH',             # 08
        'ED6_DT09/CH11141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH11120P._CP',             # 00
        'ED6_DT09/CH11121P._CP',             # 01
        'ED6_DT09/CH11110P._CP',             # 02
        'ED6_DT09/CH11111P._CP',             # 03
        'ED6_DT09/CH11130P._CP',             # 04
        'ED6_DT09/CH11131P._CP',             # 05
        'ED6_DT09/CH10040P._CP',             # 06
        'ED6_DT09/CH10041P._CP',             # 07
        'ED6_DT09/CH11140P._CP',             # 08
        'ED6_DT09/CH11141P._CP',             # 09
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


    DeclMonster(
        X                   = 13590,
        Z                   = 0,
        Y                   = 67390,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13650,
        Z                   = 0,
        Y                   = 73480,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13600,
        Z                   = 0,
        Y                   = 79600,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13660,
        Z                   = 0,
        Y                   = 83670,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13620,
        Z                   = 0,
        Y                   = 90730,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60960,
        Z                   = 0,
        Y                   = 94820,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100830,
        Z                   = 0,
        Y                   = 20580,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 38210,
        Z                   = 0,
        Y                   = -520,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15760,
        Z                   = 0,
        Y                   = -10320,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34200,
        Z                   = 0,
        Y                   = 7700,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 30560,
        Z                   = 0,
        Y                   = -65610,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3B1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 43930,
        TriggerZ            = 0,
        TriggerY            = -6210,
        TriggerRange        = 1000,
        ActorX              = 43860,
        ActorZ              = 1500,
        ActorY              = -5600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41920,
        TriggerZ            = 450,
        TriggerY            = 124030,
        TriggerRange        = 1000,
        ActorX              = 41950,
        ActorZ              = 1950,
        ActorY              = 123110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29340,
        TriggerZ            = 0,
        TriggerY            = 130710,
        TriggerRange        = 1000,
        ActorX              = 28570,
        ActorZ              = 1500,
        ActorY              = 130759,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40750,
        TriggerZ            = 0,
        TriggerY            = 60500,
        TriggerRange        = 1000,
        ActorX              = 40450,
        ActorZ              = -1000,
        ActorY              = 56090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_317",          # 01, 1
        "Function_2_386",          # 02, 2
        "Function_3_39C",          # 03, 3
        "Function_4_F75",          # 04, 4
        "Function_5_F91",          # 05, 5
        "Function_6_101E",         # 06, 6
        "Function_7_115D",         # 07, 7
        "Function_8_1283",         # 08, 8
        "Function_9_13A9",         # 09, 9
        "Function_10_14CF",        # 0A, 10
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316")
    Event(0, 3)

    label("loc_316")

    Return()

    # Function_0_2FE end

    def Function_1_317(): pass

    label("Function_1_317")

    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D")
    OP_6F(0x0, 0)
    Jump("loc_334")

    label("loc_32D")

    OP_6F(0x0, 60)

    label("loc_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    OP_6F(0x1, 0)
    Jump("loc_34D")

    label("loc_346")

    OP_6F(0x1, 60)

    label("loc_34D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F")
    OP_6F(0x2, 0)
    Jump("loc_366")

    label("loc_35F")

    OP_6F(0x2, 60)

    label("loc_366")

    OP_10(0x15, 0x1)
    OP_10(0x16, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D")
    OP_1B(0x15, 0x0, 0x6)

    label("loc_37D")

    OP_22(0x1CD, 0x1, 0x64)
    OP_82(0xB3, 0x0)
    Return()

    # Function_1_317 end

    def Function_2_386(): pass

    label("Function_2_386")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_386")

    label("loc_39B")

    Return()

    # Function_2_386 end

    def Function_3_39C(): pass

    label("Function_3_39C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(86520, 0, 156020, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 84560, 0, 155000, 270)
    SetChrPos(0x151, 87460, 0, 156140, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 80000, 0, 153080, 90)
    OP_D2(0x26030A, 0x26030F, 0xA)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_446():
        OP_8F(0xFE, 0x14DC0, 0x0, 0x25D78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_446)
    WaitChrThread(0x103, 0x1)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #0
        0x10,
        "#2P可恶，上锁了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "#2P让开，我来！\x02",
    )

    CloseMessageWindow()
    OP_22(0x18A, 0x0, 0x64)
    Sleep(800)
    OP_43(0x10, 0x3, 0x0, 0x4)

    def lambda_4B9():
        OP_8E(0xFE, 0x15220, 0x0, 0x261EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4B9)
    WaitChrThread(0x151, 0x1)
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x151, 10)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 315, 0)
    Sleep(800)

    ChrTalk(    #2
        0x151,
        (
            "#1652F（……再用一个吗？\x01",
            "  还有胡椒味的……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(300)

    ChrTalk(    #3
        0x103,
        (
            "#1643F（胡、胡椒味！？\x01",
            "  ……这是自己做的吗！！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x151,
        (
            "#1650F（基本上是白烟，\x01",
            "  不过我加入了些许\x01",
            "  原创的调整。）\x02\x03",

            "（这个则是……）\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 225, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x151, 10)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 315, 0)
    Sleep(500)

    ChrTalk(    #5
        0x151,
        (
            "#1651F（加入了\x01",
            "  笑菇的粉末哦。）\x02\x03",

            "（不知道有没有用……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 225, 0)
    Sleep(500)

    def lambda_683():

        label("loc_683")

        TurnDirection(0xFE, 0x151, 400)
        OP_48()
        Jump("loc_683")

    QueueWorkItem2(0x103, 2, lambda_683)

    def lambda_694():
        OP_8E(0xFE, 0x14A78, 0x0, 0x261EC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_694)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #6
        0x103,
        (
            "#1644F（住、住手啦！\x01",
            "  烟要是飘回来了要怎么办啊！）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x103, 0x2)

    def lambda_70F():
        OP_8E(0xFE, 0x14BA4, 0x0, 0x25F6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_70F)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 500)

    def lambda_736():
        OP_8F(0xFE, 0x153C4, 0x0, 0x25F6C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_736)

    def lambda_751():
        OP_8F(0xFE, 0x15298, 0x0, 0x261EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_751)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #7
        0x10,
        "#2P啧，好结实的门……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#2P来人，拿斧头来！\x01",
            "把它砸开！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#2P那个家伙～……！\x02",
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)
    OP_43(0x10, 0x3, 0x0, 0x5)
    Sleep(3000)
    Sleep(500)

    def lambda_7F0():
        OP_8E(0xFE, 0x151E4, 0x0, 0x25D78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F0)
    WaitChrThread(0x103, 0x1)

    def lambda_810():
        OP_8E(0xFE, 0x14A50, 0x0, 0x25D78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_810)
    WaitChrThread(0x103, 0x1)
    Sleep(1000)

    ChrTalk(    #10
        0x103,
        (
            "#1645F…………呼……\x02\x03",

            "……这下应该能\x01",
            "拖延点时间……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x103, 90, 400)
    Sleep(500)

    ChrTalk(    #11
        0x103,
        (
            "#1644F我说啊，这么危险的东西\x01",
            "不要随便乱用啦！\x02\x03",

            "……不，应该说你就不该做出来。\x01",
            "你不是大小姐吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x151,
        (
            "#1650F#2P但是………………\x02\x03",

            "#1651F派上用场了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#1645F呜…………\x01",
            "这、这我倒不否定……\x02\x03",

            "#1642F真是的，这种伎俩\x01",
            "是从哪里学来的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x151,
        (
            "#1651F#2P呵呵，我祖父是藏书家，\x01",
            "家里也有很正规的图书馆\x01",
            "给祖父专用……\x02\x03",

            "里面留有许多\x01",
            "有用的书哦。\x02\x03",

            "#1650F……雪拉扎德小姐，\x01",
            "你看小说吗？\x02\x03",

            "在某部有名的间谍小说里面，\x01",
            "有主人公制作\x01",
            "发烟筒的场面……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x103,
        (
            "#1645F（在故事里看到的吗。\x01",
            "  这家伙果然是大小姐……）\x02\x03",

            "#1642F……我说，为了你好，\x01",
            "我就实话实说了。\x02\x03",

            "刚才那是凑巧。\x01",
            "不可能次次通用的。\x02\x03",

            "从书上看到的\x01",
            "一知半解的知识，\x01",
            "没什么好值得炫耀的。\x02\x03",

            "今后请不要再\x01",
            "采取这种轻率的举动。\x02\x03",

            "…………明白吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x151,
        "#1652F#2P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#1646F好了，赶快走吧……\x02",
    )

    CloseMessageWindow()

    def lambda_C0C():
        OP_6D(87520, 0, 158020, 2500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C0C)

    def lambda_C24():
        OP_8E(0xFE, 0x14A50, 0x0, 0x265D4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C24)
    Sleep(500)

    def lambda_C44():

        label("loc_C44")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_C44")

    QueueWorkItem2(0x151, 2, lambda_C44)
    WaitChrThread(0x103, 0x1)

    def lambda_C5A():
        OP_8E(0xFE, 0x15144, 0x0, 0x26CDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C5A)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 400)
    OP_44(0x151, 0x2)

    ChrTalk(    #18
        0x103,
        "#1646F…………………………\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    Sleep(500)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)

    ChrTalk(    #19
        0x103,
        (
            "#1646F（……这么说来当时……）\x02\x03",

            "（好像也是在这种地方\x01",
            "  四处逃窜……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x103)

    ChrTalk(    #20
        0x151,
        "#1653F#4P那，那个……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#1648F（感觉……回来了吗。）\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x151,
        (
            "#1652F#4P（我、我说了什么\x01",
            "  不好的话吗……？？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#1646F…………走吧。\x02\x03",

            "这种程度的门，\x01",
            "那些家伙一下就能撬开了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E5D():
        OP_8E(0xFE, 0x15590, 0x0, 0x26CDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E5D)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #24
        0x103,
        (
            "#1642F这里应该也有魔兽出没。\x01",
            "别离我太远。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x151,
        "#1653F#4P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        "#1648F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_EFE():
        OP_8E(0xFE, 0x16210, 0xFFFFF830, 0x26CDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EFE)
    Sleep(100)

    def lambda_F1E():
        OP_8E(0xFE, 0x15298, 0x0, 0x26C78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_F1E)
    WaitChrThread(0x151, 0x1)

    def lambda_F3E():
        OP_8E(0xFE, 0x16238, 0x0, 0x26C78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_F3E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    ClearMapFlags(0x10000000)
    OP_A2(0x2F4D)
    NewScene("ED6_DT21/C4202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_39C end

    def Function_4_F75(): pass

    label("Function_4_F75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F90")
    Sleep(2000)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(800)
    Jump("Function_4_F75")

    label("loc_F90")

    Return()

    # Function_4_F75 end

    def Function_5_F91(): pass

    label("Function_5_F91")

    OP_22(0x1A, 0x0, 0x64)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x5A)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x5A)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x50)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x50)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x46)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x46)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x3C)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x3C)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x32)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x32)
    Sleep(400)
    OP_22(0x1A, 0x0, 0x28)
    Sleep(400)
    OP_22(0x1B, 0x0, 0x28)
    Sleep(400)
    Return()

    # Function_5_F91 end

    def Function_6_101E(): pass

    label("Function_6_101E")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 6)), scpexpr(EXPR_END)), "loc_10B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_105E")
    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #27
        0x103,
        "#1646F……别走这边。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10B4")

    label("loc_105E")

    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #28
        0x103,
        (
            "#1642F……别走这边。\x02\x03",

            "穿过地下水道，\x01",
            "到西街区去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10B4")

    Jump("loc_1146")

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10EE")
    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #29
        0x103,
        "#1646F……赶快走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1146")

    label("loc_10EE")

    OP_8C(0x103, 90, 500)
    Sleep(200)

    ChrTalk(    #30
        0x103,
        (
            "#1642F……赶快走吧。\x02\x03",

            "这种程度的门\x01",
            "很快就会被突破的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1146")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_6_101E end

    def Function_7_115D(): pass

    label("Function_7_115D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1242")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_11D1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_11B6")

    label("loc_11B6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF4)
    Jump("loc_123F")

    label("loc_11D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1220")

    label("loc_1220")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_123F")

    Jump("loc_1275")

    label("loc_1242")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1275")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_115D end

    def Function_8_1283(): pass

    label("Function_8_1283")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1368")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_12F7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x00得到了\x1F\x03\x02\x07\x00。\x02",
    )

    Jump("loc_12DC")

    label("loc_12DC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF5)
    Jump("loc_1365")

    label("loc_12F7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        (
            "宝箱里装有\x1F\x03\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x03\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1346")

    label("loc_1346")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1365")

    Jump("loc_139B")

    label("loc_1368")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_139B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1283 end

    def Function_9_13A9(): pass

    label("Function_9_13A9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_141D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00得到了\x1F\x03\x02\x07\x00。\x02",
    )

    Jump("loc_1402")

    label("loc_1402")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF6)
    Jump("loc_148B")

    label("loc_141D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "宝箱里装有\x1F\x03\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x03\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_146C")

    label("loc_146C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_148B")

    Jump("loc_14C1")

    label("loc_148E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14C1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_13A9 end

    def Function_10_14CF(): pass

    label("Function_10_14CF")

    EventBegin(0x1)

    ChrTalk(    #40
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_14FD():
        OP_6D(40170, 0, 57370, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_14FD)

    def lambda_1515():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1515)

    def lambda_152D():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_152D)

    def lambda_153D():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_153D)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    Jump("loc_156B")

    label("loc_156B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    Jump("loc_1593")

    label("loc_1593")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DE")
    OP_C0(0xE, 0x29, 0x9F7E, 0x0, 0xEC54, 0xB4, 0x9CD6, 0xFFFFFE0C, 0xD73C)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_15ED")

    label("loc_15DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15ED")
    EventEnd(0x1)

    label("loc_15ED")

    Return()

    # Function_10_14CF end

    SaveToFile()

Try(main)
