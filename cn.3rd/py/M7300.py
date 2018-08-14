from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7300   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        'ED6_DT26/CH20722 ._CH',             # 00
        'ED6_DT26/CH20718 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20722P._CP',             # 00
        'ED6_DT26/CH20718P._CP',             # 01
    )

    DeclActor(
        TriggerX            = 3410,
        TriggerZ            = 4950,
        TriggerY            = 27060,
        TriggerRange        = 1000,
        ActorX              = 3410,
        ActorZ              = 5800,
        ActorY              = 27060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_DE",           # 00, 0
        "Function_1_FB",           # 01, 1
        "Function_2_11F",          # 02, 2
        "Function_3_15C5",         # 03, 3
        "Function_4_160A",         # 04, 4
        "Function_5_1621",         # 05, 5
        "Function_6_1638",         # 06, 6
    )


    def Function_0_DE(): pass

    label("Function_0_DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_FA")

    Return()

    # Function_0_DE end

    def Function_1_FB(): pass

    label("Function_1_FB")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230093)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 3)), scpexpr(EXPR_END)), "loc_11E")
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)

    label("loc_11E")

    Return()

    # Function_1_FB end

    def Function_2_11F(): pass

    label("Function_2_11F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 440, 1550, -12260, 180)
    SetChrPos(0x10F, 440, 1550, -12260, 90)
    SetChrFlags(0x109, 0x8)
    SetChrChipByIndex(0x10F, 0)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    SetChrFlags(0x10F, 0x800)
    OP_6D(-350, 1550, -11450, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(266, 0)
    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName("青年的声音")

    AnonymousTalk(    #0
        (
            "\x07\x00…………喂喂…………………\x02\x03",

            "……莉丝……………\x01",
            "…………振作点………啊…………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #1
        (
            "\x07\x00#1633F#40W唔……\x02\x03",

            "#1632F……凯……文………？\x02",
        )
    )

    Jump("loc_26F")

    label("loc_26F")

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x109, 0x3, 0x0, 0x3)

    def lambda_27F():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_27F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #2
        0x10F,
        "#1631F#6P#40W……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1840F#2P……你还好吗？\x01",
            "感觉…身体状况如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #4
        0x10F,
        (
            "#1635F#6P#40W唔……\x01",
            "好像……没什么事。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(300)

    ChrTalk(    #5
        0x10F,
        (
            "#1632F#6P#40W凯文……为什么………\x02\x03",

            "我………\x01",
            "…我……从裂缝掉了下来……\x02\x03",

            "#1634F可是……\x01",
            "为什么连凯文也……\x02",
        )
    )

    Jump("loc_4DA")

    label("loc_4DA")

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #6
        0x109,
        "#1069F#2P#4S你这个傻瓜……！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(150)
    OP_99(0x10F, 0x3, 0x6, 0x3E8)
    OP_22(0x19E, 0x0, 0x64)
    OP_99(0x10F, 0x7, 0xF, 0x5DC)
    Sleep(300)

    ChrTalk(    #7
        0x10F,
        "#1631F#6P………哎………………\x02",
    )

    CloseMessageWindow()
    OP_1D(0xAD)
    Sleep(500)

    ChrTalk(    #8
        0x109,
        (
            "#1069F#2P怎么能完全不经考虑\x01",
            "就向对方挑衅呢！\x02\x03",

            "『做得到的话你就试试看』！？\x02\x03",

            "『无论落到哪里\x01",
            "  都一定会活下去』！？\x02\x03",

            "你说出这番话\x01",
            "究竟事先有没有考虑过啊！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #9
        0x10F,
        "#1634F#6P……可、可是…………\x02",
    )

    CloseMessageWindow()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #10
        0x109,
        (
            "#1069F#2P你，还是随从骑士对吧！？\x02\x03",

            "一个判断力和实践力都没有的新人，\x01",
            "不要随意以自己的臆断去行事！\x02\x03",

            "如果连这个也无法遵守的话……\x01",
            "索性退出骑士团算了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        "#1632F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #12
        0x109,
        (
            "#1841F#2P……其实我本来是\x01",
            "想这么好好教训你一顿的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #13
        0x109,
        (
            "#1840F#2P不过我也没资格说别人，\x01",
            "就用刚才弹脑门那下抵了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        "#1631F#6P……哎……………\x02",
    )

    CloseMessageWindow()
    OP_99(0x10F, 0x15, 0x17, 0x3E8)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(300)
    OP_99(0x10F, 0x17, 0x19, 0x5DC)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x10F, 26)
    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 450, 1550, -11800, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x109, 90, 400)

    def lambda_8F5():
        OP_8E(0xFE, 0x8C0, 0x60E, 0xFFFFD256, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8F5)

    def lambda_910():
        OP_6D(600, 1550, -11450, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_910)
    OP_99(0x10F, 0x1A, 0x1D, 0x5DC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #15
        0x109,
        (
            "#1067F#5P看看，这景象……\x02\x03",

            "这就是『第七星层』啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        "#1634F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(600, 1550, -11450, 0)
    OP_67(0, 9250, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(335, 0)
    OP_43(0x109, 0x2, 0x0, 0x4)

    def lambda_9EF():
        OP_6B(7000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_9EF)

    def lambda_9FF():
        OP_6C(330000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_9FF)
    OP_C8(0x200, 0x46, "C_PLAC37._CH", 0x0, 0x7D0)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(600, 1550, -11450, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(266, 0)
    OP_43(0x109, 0x2, 0x0, 0x5)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    ClearChrFlags(0x10F, 0x800)
    SetChrPos(0x10F, 500, 1550, -12260, 90)
    OP_0D()
    Sleep(300)

    def lambda_AAD():
        OP_6D(1040, 1550, -11290, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_AAD)

    def lambda_AC5():
        OP_8E(0xFE, 0x7E4, 0x60E, 0xFFFFCE14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_AC5)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #17
        0x10F,
        "#1630F#5P……『炼狱』…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1065F#5P是啊……\x01",
            "的确是那样一番光景呢。\x02\x03",

            "#1067F而且……\x01",
            "这种景象的始作俑者，\x01",
            "多半就是我自己……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #19
        0x10F,
        "#1634F#6P………啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        (
            "#1067F#5P这个『影之国』是\x01",
            "能够反映人们意念的世界……\x02\x03",

            "不知因为什么理由……\x01",
            "让露菲娜姐姐在这个地方复活了。\x02\x03",

            "虽然有着姐姐本身的记忆和性格，\x01",
            "但她仅仅是作为惩罚我的存在。\x02\x03",

            "#1065F……而且，对我来说，\x01",
            "这的确是至高无上的『惩罚』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1632F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1075F#5P我……\x01",
            "的确很愿意接受『惩罚』。\x02\x03",

            "而且，我坚信只要我得到『惩罚』，\x01",
            "所有事情就可以得到解决。\x02\x03",

            "我觉得，如果牺牲了自己，\x01",
            "就可以像姐姐那时候做的那样，\x01",
            "将你们从困境之中解救出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #23
        0x109,
        "#1840F#11P不过……那不正是错的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10F,
        (
            "#1635F#6P嗯……\x02\x03",

            "#1632F那时候，姐姐甘愿作出自我牺牲，\x01",
            "去解救失去理智的凯文……\x02\x03",

            "恐怕是因为……\x01",
            "她觉得那是一条别无选择的路。\x02\x03",

            "#1633F我在一旁昏迷着……\x01",
            "她也没有办法撤退……\x02\x03",

            "必须牺牲其中一个人，\x01",
            "的确是没有丝毫的选择余地啊……\x02\x03",

            "#1630F所以……\x01",
            "姐姐才决定选择了那条路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1075F#11P……是啊。\x02\x03",

            "姐姐绝对不是认为\x01",
            "单纯的自我牺牲是正确的。\x02\x03",

            "#1840F在竭尽一切手段也不起作用的情况下，\x01",
            "她唯有作出尽可能好的最后决断。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        (
            "#1633F#6P可是……\x01",
            "这次的情况和那时候不同啊。\x02\x03",

            "这里有我，还有其他伙伴。\x02\x03",

            "#1632F如果我们同心协力的话，\x01",
            "应该可以找到其它的道路……\x02\x03",

            "如果我们使劲去思考的话，\x01",
            "应该能找到别的解决对策……\x02\x03",

            "但是……\x01",
            "你却选择了用懈怠的方式去逃避。\x02\x03",

            "#1635F……是吧？\x02",
        )
    )

    Jump("loc_10FE")

    label("loc_10FE")

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1841F#11P啊……\x01",
            "看来的确是这样啊。\x02\x03",

            "没想到会让我这个\x01",
            "『守护骑士』丢尽脸面……\x02\x03",

            "#1840F哈哈……\x01",
            "我才是没有资格做骑士的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1634F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1075F#11P也罢。\x01",
            "后悔自己懦弱也无济于事……\x02\x03",

            "#1078F好了，如果没事的话，\x01",
            "就马上出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x10F,
        "#1631F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1840F#11P怎么了，瞪着我干什么。\x02\x03",

            "难道你以为我会留下来，\x01",
            "等待接受『惩罚』什么的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10F,
        (
            "#1632F#6P……那个………\x02\x03",

            "我是在想……\x01",
            "你是不是打算留在这里等姐姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1075F#11P听我说，莉丝。\x02\x03",

            "#1840F……的确，\x01",
            "我也许在期盼得到『惩罚』。\x02\x03",

            "即使以这种方式和姐姐相会……\x01",
            "也的确是让人感到高兴。\x02\x03",

            "#1065F……但是，这次另当别论。\x02\x03",

            "#1063F从你被卷入这里来的那一刻起，\x01",
            "这地方就不是久留之地。\x02\x03",

            "#1069F就算是无用的挣扎也好，\x01",
            "我们说什么也要一起离开这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        (
            "#1631F#6P………啊…………\x02\x03",

            "#1635F嗯……好的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14AF():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_14AF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    OP_44(0xEE, 0x0)
    OP_A2(0x2C0B)
    OP_BB(0xE, 0x1, 0x16)
    OP_BD()
    OP_AA(65282)
    OP_28(0x3C, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x20)
    OP_28(0x3D, 0x4, 0x4)
    OP_28(0x3D, 0x4, 0x8)
    OP_28(0x3D, 0x1, 0x1)
    OP_6D(10, 1550, -11670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 1550, -11670, 0)
    SetChrPos(0x1, 0, 1550, -11670, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E6(0x2)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_1D(0xAF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x17B, 0x64)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_2_11F end

    def Function_3_15C5(): pass

    label("Function_3_15C5")

    OP_22(0x17B, 0x1, 0x0)
    Sleep(300)
    OP_24(0x17B, 0xA)
    Sleep(300)
    OP_24(0x17B, 0x14)
    Sleep(300)
    OP_24(0x17B, 0x1E)
    Sleep(300)
    OP_24(0x17B, 0x28)
    Sleep(300)
    OP_24(0x17B, 0x32)
    Sleep(300)
    OP_24(0x17B, 0x3C)
    Sleep(300)
    OP_24(0x17B, 0x46)
    Return()

    # Function_3_15C5 end

    def Function_4_160A(): pass

    label("Function_4_160A")

    OP_24(0x17B, 0x50)
    Sleep(300)
    OP_24(0x17B, 0x5A)
    Sleep(300)
    OP_24(0x17B, 0x64)
    Return()

    # Function_4_160A end

    def Function_5_1621(): pass

    label("Function_5_1621")

    OP_24(0x17B, 0x5A)
    Sleep(300)
    OP_24(0x17B, 0x50)
    Sleep(300)
    OP_24(0x17B, 0x46)
    Return()

    # Function_5_1621 end

    def Function_6_1638(): pass

    label("Function_6_1638")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05有一股不可思议的力量涌出。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    Jump("loc_16A6")

    label("loc_16A6")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16D0"),
        (1, "loc_176E"),
        (SWITCH_DEFAULT, "loc_176E"),
    )


    label("loc_16D0")

    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x86, 0x0)
    OP_1D(0xAF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_176E")

    TalkEnd(0xFF)
    SetMapFlags(0x100000)
    Return()

    # Function_6_1638 end

    SaveToFile()

Try(main)
