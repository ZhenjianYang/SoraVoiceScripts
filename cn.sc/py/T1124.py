from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1124   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '卢格兰老人',                           # 9
        '梅贝尔市长',                           # 10
        '雪拉扎德',                             # 11
        '奥利维尔',                             # 12
        '科洛丝',                               # 13
        '金',                                   # 14
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
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT07/CH02360 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT07/CH02360P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
    )

    DeclNpc(
        X                   = 180,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x114,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_19B",          # 01, 1
        "Function_2_1C1",          # 02, 2
        "Function_3_1278",         # 03, 3
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Return()

    # Function_0_19A end

    def Function_1_19B(): pass

    label("Function_1_19B")

    OP_B1("T1121_2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1C0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1C0")

    Return()

    # Function_1_19B end

    def Function_2_1C1(): pass

    label("Function_2_1C1")

    EventBegin(0x0)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    OP_6D(480, 0, 2930, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -70, 0, 2350, 0)
    SetChrPos(0xA, -1140, 0, 2340, 0)
    SetChrPos(0xD, -50, 0, 250, 0)
    SetChrPos(0xC, -320, 0, 1350, 0)
    SetChrPos(0xB, -1360, 0, 970, 0)
    SetChrPos(0x9, 970, 0, 1880, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#634F哎呀……\x01",
            "真是辛苦你们了。\x02\x03",

            "#632F不过真没想到阿加特那家伙\x01",
            "还有那样的过去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#618F#4P是啊……\x02\x03",

            "#615F听了你们的话，\x01",
            "我总算明白了。\x02\x03",

            "那时阿加特的\x01",
            "心情是怎样的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D)
    Sleep(50)

    def lambda_360():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_360)
    Sleep(50)

    def lambda_373():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_373)
    Sleep(50)

    def lambda_386():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_386)
    Sleep(50)
    OP_8C(0xB, 90, 400)

    ChrTalk(    #2
        0x101,
        "#1004F那时？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #3
        0x9,
        (
            "#612F#2P１０年前……\x02\x03",

            "『百日战役』刚结束，\x01",
            "阿加特曾经\x01",
            "来过我家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1020F咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xC,
        "#044F#6P去了前辈的家？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#615F#2P嗯，他当时气势汹汹地\x01",
            "逼问还身为市长的父亲。\x02\x03",

            "身为柏斯市长，肩负统辖\x01",
            "整个地方的责任……\x02\x03",

            "#612F可为什么要抛下\x01",
            "拉文努村不管，他这样质问父亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1026F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#618F#2P还是孩子的我，\x01",
            "看着责备父亲的阿加特\x01",
            "感到很恼火……\x02\x03",

            "所以忍不住就冲出去\x01",
            "打了阿加特一记耳光。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1007F啊～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        "#524F#6P总之，是件不幸的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#618F#2P嗯……\x02\x03",

            "#612F结果，家父也未能对\x01",
            "阿加特的问题做出回答。\x02\x03",

            "而是告诉他准备把复兴村子的\x01",
            "援助金送过去。\x02\x03",

            "听完解释之后的阿加特\x01",
            "将拳头指向了父亲……\x02\x03",

            "#615F……可是，最后他把拳头放了下来，\x01",
            "然后就奔跑着离开了我家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015F有那么一回事啊……\x02\x03",

            "所以阿加特和市长你，\x01",
            "彼此之间有一种奇怪的氛围呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#615F#2P……双方都对那时的\x01",
            "事怀有芥蒂呢。\x02\x03",

            "#618F可是我没想到阿加特的\x01",
            "妹妹在那场战争中丧生了……\x02\x03",

            "我……\x01",
            "好像误解了他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1025F好了，他不把事情说出来\x01",
            "自己也有责任的。\x02\x03",

            "市长你没必要太介怀的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#615F#2P呵呵……是吗。\x02\x03",

            "#612F……阿加特的\x01",
            "伤势怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1006F嗯，不用担心。\x02\x03",

            "过两三天就\x01",
            "应该能活动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#630F呼……\x01",
            "可以说是不幸中的万幸了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#611F#2P嗯……\x01",
            "没有大碍就好。\x02\x03",

            "#618F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        (
            "#043F#6P对了，前辈……\x02\x03",

            "莉拉小姐的\x01",
            "情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#618F#2P……那个……\x02\x03",

            "对伤势是做了处理，\x01",
            "不过现在还没有醒……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "#049F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "#032F嗯……\x01",
            "真让人痛心啊。\x02\x03",

            "那美丽又可爱的小姐\x01",
            "本应是世上最珍贵的珍宝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#611F#2P呵呵……等莉拉醒了\x01",
            "我会转达给她的。\x02\x03",

            "#610F不过说起来……\x01",
            "摩尔根将军说的话真能鼓励人呢。\x02\x03",

            "如果军队能和协会联手的话，\x01",
            "那是最令人安心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "#026F#6P虽然还没有决定下来，\x01",
            "所以不能轻易地下保证……\x02\x03",

            "#027F不过我们会尽\x01",
            "自己所能的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A8E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A8E)
    Sleep(50)

    def lambda_AA1():

        label("loc_AA1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AA1")

    QueueWorkItem2(0x101, 3, lambda_AA1)
    Sleep(50)

    def lambda_AB7():

        label("loc_AB7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AB7")

    QueueWorkItem2(0xA, 3, lambda_AB7)
    Sleep(50)

    def lambda_ACD():

        label("loc_ACD")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_ACD")

    QueueWorkItem2(0xD, 3, lambda_ACD)
    Sleep(50)

    def lambda_AE3():

        label("loc_AE3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AE3")

    QueueWorkItem2(0xC, 3, lambda_AE3)
    Sleep(50)

    def lambda_AF9():

        label("loc_AF9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_AF9")

    QueueWorkItem2(0xB, 3, lambda_AF9)
    Sleep(50)

    def lambda_B0F():

        label("loc_B0F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_B0F")

    QueueWorkItem2(0x9, 3, lambda_B0F)
    Sleep(100)

    def lambda_B25():
        OP_6D(760, 0, 3570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B25)
    OP_8E(0x8, 0x794, 0x0, 0x1252, 0x5DC, 0x0)
    OP_8C(0x8, 0, 400)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #25
        0x8,
        (
            "#630F#4P这里是游击士协会所属\x01",
            "柏斯支部……\x02\x03",

            "#633F啊，是将军阁下。\x01",
            "我们等您很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006F（来了来了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#027F#6P（看看……\x01",
            "到底会怎么样呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#632F#4P嗯嗯……噢噢。\x02\x03",

            "#633F哦，真没想到会这样！\x02\x03",

            "#630F原来如此……\x01",
            "明早10点，国际空港。\x02\x03",

            "#631F我明白了。\x01",
            "我会准确地传达的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)
    OP_8C(0x8, 270, 400)

    def lambda_CEE():
        OP_6D(480, 0, 2930, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CEE)
    OP_8E(0x8, 0xB4, 0x0, 0x1130, 0x5DC, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0xA, 0x3)
    OP_44(0xD, 0x3)
    OP_44(0xC, 0x3)
    OP_44(0x9, 0x3)
    OP_44(0xB, 0x3)

    def lambda_D32():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D32)

    def lambda_D40():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D40)

    def lambda_D4E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D4E)

    def lambda_D5C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D5C)

    def lambda_D6A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D6A)
    OP_8C(0xB, 0, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #29
        0x101,
        "#1006F怎么样！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#632F王国军明日要用飞行舰队\x01",
            "展开捕龙作战计划。\x02\x03",

            "你们也可以以观察员的身份\x01",
            "登上军舰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1004F使用飞行舰队进行捕龙作战！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "#035F哇喔……\x01",
            "好壮观的行动。\x02\x03",

            "#030F那是王国军最精锐的部队吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#026F#6P虽然观察员其实\x01",
            "干不了什么……\x02\x03",

            "#027F不过能够近距离地观察龙的样子，\x01",
            "老实说真是求之不得呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "#070F#4P嗯，如果军队作战失败\x01",
            "就轮到我们出场了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1006F嗯……\x01",
            "看来不能掉以轻心。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #36
        0x9,
        (
            "#611F#2P呵呵……\x01",
            "总算看见一线希望了。\x02\x03",

            "#618F…………啊…………………\x02",
        )
    )

    CloseMessageWindow()
    Fade(800)

    def lambda_F7C():
        OP_6D(530, 0, 2880, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F7C)
    Sleep(400)

    def lambda_F99():
        OP_6D(480, 0, 2930, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F99)
    Sleep(400)
    OP_0D()
    Sleep(500)

    def lambda_FBC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_FBC)
    Sleep(50)

    def lambda_FCF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCF)
    Sleep(50)

    def lambda_FE2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FE2)
    Sleep(50)

    def lambda_FF5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FF5)
    Sleep(50)
    OP_8C(0xB, 90, 400)

    ChrTalk(    #37
        0xC,
        "#043F#6P前、前辈……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1020F怎、怎么了，市长？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#617F#2P不……没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "#032F刚才你好像有些头晕吧？\x01",
            "你似乎很累。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#618F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#524F#6P虽然知道你有很多事情，\x01",
            "不过太勉强自己就不好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "#617F#2P呵呵……我没有勉强自己。\x02\x03",

            "#610F『百日战役』时，\x01",
            "父亲采用了各种手段\x01",
            "确保了柏斯市民的安全。\x02\x03",

            "有时还会为了欺骗帝国军\x01",
            "而进行危险的交易。\x02\x03",

            "和那时相比较……\x01",
            "这不算什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1026F市长先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        "#043F#6P梅贝尔前辈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "#611F#2P艾丝蒂尔小姐，还有大家。\x01",
            "就请你们多多关照了。\x02\x03",

            "请为柏斯市民和\x01",
            "拉文努村的大伙们消除不安吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1006F嗯……交给我们吧！\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1211   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C1 end

    def Function_3_1278(): pass

    label("Function_3_1278")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_132F"),
        (1, "loc_1335"),
        (SWITCH_DEFAULT, "loc_133B"),
    )


    label("loc_132F")

    OP_A2(0x1200)
    Jump("loc_133B")

    label("loc_1335")

    OP_A2(0x1201)
    Jump("loc_133B")

    label("loc_133B")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_3_1278 end

    SaveToFile()

Try(main)
