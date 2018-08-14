from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4151   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4151.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '基尔巴特',                             # 9
        '',                                     # 10
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
        'ED6_DT07/CH02420 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02420P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_F0",           # 02, 2
        "Function_3_8EC",          # 03, 3
        "Function_4_933",          # 04, 4
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_EE")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_EE")

    Return()

    # Function_0_D2 end

    def Function_1_EF(): pass

    label("Function_1_EF")

    Return()

    # Function_1_EF end

    def Function_2_F0(): pass

    label("Function_2_F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 70000, 1720, 14920, 180)
    SetChrPos(0x10F, 70000, 1720, 14920, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 78160, 1250, 13000, 225)
    OP_6D(70110, 3350, 17060, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(0, 0)
    OP_6E(390, 0)

    def lambda_18D():
        OP_6D(70110, 3350, 13660, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_18D)

    def lambda_1A5():
        OP_67(0, 5000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1A5)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(800)
    OP_43(0x10F, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    Sleep(3000)
    OP_44(0x10F, 0x2)
    Fade(1000)
    OP_6D(70700, 250, 5590, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(44000, 0)
    OP_6E(344, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x3)

    ChrTalk(    #0
        0x109,
        (
            "#1068F#6P竟然一个不留\x01",
            "全部都买下来了……\x02\x03",

            "那个售货员小姐\x01",
            "可是被你吓得不轻吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        (
            "#1442F#2P这也是女神的引导。\x02\x03",

            "食物如果没人买就会被丢掉，\x01",
            "这样只是将其有效利用罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1840F#6P真没办法……\x02\x03",

            "骑士团的俸禄，\x01",
            "全部被你花在吃上面了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1447F#2P……不劳你担心。\x02\x03",

            "我敢说没有比我对限时优惠\x01",
            "更有热情的女性了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1840F#6P呼……好吧好吧。\x02\x03",

            "#1068F不过嘛，\x01",
            "虽然我的穿着已经够怪异了……\x02\x03",

            "但穿着修女服\x01",
            "去百货店大扫荡也太……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1801F#2P凯文，你真啰嗦。\x02\x03",

            "#1447F……时间差不多了，\x01",
            "我们这就去飞艇坪吧。\x02\x03",

            "我的肚子开始叫苦连天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1840F#6P好好──\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x109,
        "#1063F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        "#1444F#2P怎么了……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(79250, 1250, 14670, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)

    def lambda_5C1():
        OP_8F(0xFE, 0x13150, 0x4E2, 0x3B74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5C1)
    OP_0D()
    Sleep(1500)

    def lambda_5E2():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5E2)
    OP_6D(70700, 250, 5590, 3000)
    Sleep(300)

    ChrTalk(    #9
        0x10F,
        "#1801F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1840F#6P（……现在好像并不是\x01",
            "  悠闲地吃面包的时候。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1446F#2P（……不可饶恕……）\x02\x03",

            "#1801F（虽然不知道是谁，\x01",
            "  至少也得把他打个半死才行……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x109,
        (
            "#1068F#6P（……我明白你的感受，\x01",
            "  不过请你保持冷静。）\x02\x03",

            "#1060F（话说回来，这可真是\x01",
            "  超级拙劣的跟踪方式啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1443F#2P（感觉不过是个新手罢了……）\x02\x03",

            "（但似乎也受过一点训练。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6P（哎呀……）\x02\x03",

            "#1063F（没办法了。\x01",
            "  只有放弃乘坐最后一趟飞艇了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10F,
        "#1443F#2P（你准备将他引到某个地方吗……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1075F#6P（嗯……）\x02\x03",

            "#1060F（我想到一个与目前的情况\x01",
            "  相配的绝佳场所。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4404   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_F0 end

    def Function_3_8EC(): pass

    label("Function_3_8EC")


    def lambda_8F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8F2)
    OP_8E(0xFE, 0x11260, 0x4E2, 0x3156, 0x7D0, 0x0)
    OP_8E(0xFE, 0x113FA, 0xFA, 0x1202, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_3_8EC end

    def Function_4_933(): pass

    label("Function_4_933")


    def lambda_939():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_939)
    OP_8E(0xFE, 0x110A8, 0x4E2, 0x3156, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10CE8, 0xFA, 0x1194, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_933 end

    SaveToFile()

Try(main)
