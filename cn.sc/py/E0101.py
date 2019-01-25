from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0101   ._SN',
        MapName             = 'event',
        Location            = 'E0101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '乔丝特',                               # 9
        '吉尔',                                 # 10
        '多伦',                                 # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
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
        'ED6_DT27/CH03010 ._CH',             # 00
        'ED6_DT27/CH03100 ._CH',             # 01
        'ED6_DT26/CH20370 ._CH',             # 02
        'ED6_DT26/CH20400 ._CH',             # 03
        'ED6_DT07/CH02120 ._CH',             # 04
        'ED6_DT27/CH03015 ._CH',             # 05
        'ED6_DT26/CH20401 ._CH',             # 06
        'ED6_DT27/CH03101 ._CH',             # 07
        'ED6_DT26/CH20398 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT27/CH03010P._CP',             # 00
        'ED6_DT27/CH03100P._CP',             # 01
        'ED6_DT26/CH20370P._CP',             # 02
        'ED6_DT26/CH20400P._CP',             # 03
        'ED6_DT07/CH02120P._CP',             # 04
        'ED6_DT27/CH03015P._CP',             # 05
        'ED6_DT26/CH20401P._CP',             # 06
        'ED6_DT27/CH03101P._CP',             # 07
        'ED6_DT26/CH20398P._CP',             # 08
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_161",          # 01, 1
        "Function_2_181",          # 02, 2
        "Function_3_10ED",         # 03, 3
        "Function_4_10FD",         # 04, 4
        "Function_5_1112",         # 05, 5
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_160")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_160")

    Return()

    # Function_0_152 end

    def Function_1_161(): pass

    label("Function_1_161")

    OP_22(0x79, 0x1, 0x3C)
    OP_22(0x1C3, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_180")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180")

    Return()

    # Function_1_161 end

    def Function_2_181(): pass

    label("Function_2_181")

    EventBegin(0x0)
    ClearParty()
    AddParty(0x1, 0xF6, 0xFF)
    SetChrFlags(0x102, 0x80)
    OP_48()
    OP_6D(-289560, 30000, -136650, 0)
    OP_67(0, 2320, -10000, 0)
    OP_6B(12030, 0)
    OP_6C(66000, 0)
    OP_6E(300, 0)
    StopSound(0xD6D8, 0x7A120, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    OP_BD()
    FadeToBright(2000, 0)
    StopSound(0xD6D8, 0x33450, 0x32C8)

    def lambda_1FC():
        OP_6D(-99550, 5550, -94010, 13000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FC)

    def lambda_214():
        OP_6B(2800, 13000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_214)

    def lambda_224():
        OP_6E(334, 13000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_224)
    Sleep(7000)
    OP_72(0x3, 0x20)

    def lambda_23E():
        OP_6C(35000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23E)
    OP_67(0, 7540, -10000, 6000)
    OP_22(0x6A, 0x0, 0x64)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(1000)
    SetChrFlags(0x8, 0x4)
    SetChrBattleFlags(0x8, 0x20)
    SetChrPos(0x8, -99440, 5550, -91440, 0)
    ClearChrFlags(0x8, 0x80)
    OP_8E(0x8, 0xFFFE7B72, 0x15A4, 0xFFFE90F8, 0x7D0, 0x0)

    ChrTalk(    #0
        0x8,
        "#213F#5P咦……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 90, 400)
    Sleep(500)
    SetChrPos(0x102, -100000, 5550, -89500, 0)
    SetChrFlags(0x102, 0x4)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 2)
    SetChrSubChip(0x102, 2)
    OP_43(0x8, 0x1, 0x0, 0x5)

    def lambda_32C():
        OP_6D(-98020, 5550, -89450, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_32C)
    OP_6C(225000, 8000)

    ChrTalk(    #1
        0x8,
        "#210F什么啊，原来在这里啊。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(500)

    ChrTalk(    #2
        0x102,
        (
            "#1031F……从这边可以\x01",
            "比较清楚地看到月亮呢。\x02\x03",

            "肌肤也能感受到到风的流动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#211F啊哈哈！又～在\x01",
            "装模作样了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_418():
        OP_6D(-99380, 5550, -89500, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_418)

    def lambda_430():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_430)

    def lambda_440():
        OP_8E(0x8, 0xFFFE7D34, 0x15AE, 0xFFFEA296, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_440)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x102, 0x1)
    Fade(250)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #4
        0x8,
        (
	        "#210F……哟咻。\x02\x03",

	        "#413F这并不是在\x01",
	        "装模作样耍帅……\x02\x03",

	        "#215F而是必要的，对吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(500)

    ChrTalk(    #7
        0x102,
        (
            "#1035F#5P月光的亮度、云的位置、风的流动…\x01",
            "在此时都变得相当重要。\x02\x03",

            "#1031F我希望把失败的可能性\x01",
            "尽量降到最低。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "#212F尽、尽量……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 4)
    Sleep(300)

    ChrTalk(    #9
        0x8,
        (
            "#214F你啊……\x01",
            "可别说什么能尽力而为的话哦！\x02\x03",

            "失败了就是死路一条啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1035F#5P别担心，失败的可能性很小。\x02\x03",

            "这种危险程度的任务，\x01",
            "以前可是每天都会接触到。\x02\x03",

            "#1033F真正的危险……\x01",
            "不如说是在任务成功之后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#212F………………………………\x02\x03",

            "#413F……我问你，约修亚。\x02\x03",

            "你真的有必要\x01",
            "做到这种地步吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(500)

    ChrTalk(    #12
        0x102,
        "#1034F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#215F你也和我们一样是\x01",
            "埃雷波尼亚出身的吧。\x02\x03",

            "#413F虽然说彼此或许各有隐情\x01",
            "而不能返回故乡也说不定……\x02\x03",

            "#212F但就算是这样，你也没必要\x01",
            "对这个国家尽什么义务不是吗？\x02\x03",

            "『结社』要做什么的话，\x01",
            "随他们去做不就好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#1033F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#210F好不好，现在还来得及。\x02\x03",

            "就这个样子和我们一起\x01",
            "离开利贝尔……\x02\x03",

            "去找个自治州\x01",
            "揭竿而起怎么样？\x02\x03",

            "如果不想做空贼，\x01",
            "也可以找其它的工作。\x02\x03",

            "#211F我和哥哥他们谈过，\x01",
            "利用这艘飞船的速度\x01",
            "来做运输业应该也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 5)
    Sleep(75)
    SetChrSubChip(0x102, 6)
    Sleep(400)

    ChrTalk(    #16
        0x102,
        (
            "#1035F用飞船做运输业吗……\x02\x03",

            "这方面的需求今后还会增加，\x01",
            "或许是相当有前途的行业呢。\x02\x03",

            "至少应该能赚得\x01",
            "比当空贼还多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#210F那、那么就！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 5)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(500)

    ChrTalk(    #18
        0x102,
        (
            "#1031F说得也是……\x02\x03",

            "毁灭『结社』的计划之后，\x01",
            "如果我还活着的话\x01",
            "就考虑考虑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "#213F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1034F嗯嗯，你不用担心，\x01",
            "我们的契约到此就结束了。\x02\x03",

            "#1031F只要帮忙这个作战计划，\x01",
            "之前欠我的人情就一笔勾销了。\x02\x03",

            "你们随时都可以出发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "#215F……够了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1034F哎。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_8C(0x8, 270, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x8,
        (
            "#214F笨蛋！\x01",
            "谁在说什么欠人情的事！\x02\x03",

            "#215F算了！\x01",
            "我不管你了！\x02\x03",

            "你爱跳入火坑，\x01",
            "爱送死去的话就尽管去好了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x8, 90, 600)
    SetChrChipByIndex(0x8, 7)
    OP_8E(0x8, 0xFFFE8E3C, 0x15AE, 0xFFFEA070, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFE8DA6, 0x15AE, 0xFFFE94FE, 0x1770, 0x0)
    OP_8E(0x8, 0xFFFE7BC2, 0x15AE, 0xFFFE910C, 0x1770, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_71(0x0, 0x10)
    Sleep(500)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(800)
    SetChrSubChip(0x102, 1)
    Sleep(140)
    SetChrSubChip(0x102, 2)
    Sleep(800)

    ChrTalk(    #24
        0x102,
        "#1035F#5P……对不起，乔丝特。\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x9, 0x20)
    SetChrPos(0x9, -103120, 13050, -91360, 10)
    OP_6F(0x1, 35)
    Sleep(500)

    NpcTalk(    #25
        0x9,
        "青年的声音",
        (
            "#6P真是的……\x01",
            "假装迟钝可真没意思啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(50)
    SetChrSubChip(0x102, 0)
    OP_62(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x9, -103120, 9050, -91360, 10)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0x9, 0x80)
    Fade(500)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()

    def lambda_C81():
        OP_6D(-100330, 5550, -92350, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C81)

    def lambda_C99():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C99)

    def lambda_CB1():
        OP_6C(144000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_CB1)

    def lambda_CC1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC1)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #26
        0x102,
        "#1034F#6P……吉尔兄。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "#200F那家伙一样也是\x01",
            "脱离不了小孩子个性……\x02\x03",

            "不过，刚才毕竟是\x01",
            "你的说话方式不对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1035F#6P……是啊。\x02\x03",

            "#1033F虽然并不打算道歉，\x01",
            "但还是觉得对不起她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#203F真是的……\x01",
            "虽然知道这就是你\x01",
            "关心别人的方式。\x02\x03",

            "#200F不过，刚才的话\x01",
            "你还是认真考虑一下吧。\x02\x03",

            "等一切都了结之后，\x01",
            "要是你不打算回那个\x01",
            "游击士小姑娘身边的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1031F#6P哈哈……那当然不会。\x02\x03",

            "毕竟，我和她\x01",
            "生存的世界差距太大了。\x02\x03",

            "已经不可能再走到一起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#200F呼……\x01",
            "嗯，这倒也不错。\x02\x03",

            "#202F那样的话\x01",
            "也不算是件坏事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1031F#6P是啊……\x01",
            "我会好好考虑的。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAB, 0x1, 0x50)
    Sleep(500)
    OP_20(0x3E8)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x9,
        "#201F出现了吗！\x02",
    )

    CloseMessageWindow()

    def lambda_F42():
        OP_8F(0xFE, 0xFFFE6D30, 0x2198, 0xFFFE9B20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F42)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x9, 0x1)
    OP_1D(0x56)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #34
        0x9,
        "#201F#5P大哥，来了吗！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, -103120, 6550, -91360, 270)

    NpcTalk(    #35
        0xA,
        "多伦的声音",
        (
            "#2P哦哦！\x01",
            "正如那小子预料的一样！\x02\x03",

            "从东北方\x01",
            "不断接近中呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF2():
        OP_8F(0xFE, 0xFFFE6D30, 0x235A, 0xFFFE9B20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_FF2)
    OP_8C(0x9, 10, 400)
    WaitChrThread(0x9, 0x1)
    Sleep(300)

    ChrTalk(    #36
        0x9,
        (
            "#206F你听到了吧？\x01",
            "马上到舰桥来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        "#1032F#6P知道了。\x02",
    )

    CloseMessageWindow()

    def lambda_105B():
        OP_6D(-100000, 5550, -89480, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_105B)

    def lambda_1073():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1073)

    def lambda_108B():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_108B)

    def lambda_109B():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_109B)

    def lambda_10AB():
        OP_6E(262, 1500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10AB)
    OP_8C(0x9, 270, 400)
    OP_43(0x9, 0x1, 0x0, 0x4)
    OP_23(0xAB)
    OP_6F(0x1, 35)
    OP_70(0x1, 0x0)
    OP_43(0x9, 0x0, 0x0, 0x3)
    OP_A2(0x1C00)
    OP_D6(0x0)
    WaitChrThread(0x102, 0x1)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_181 end

    def Function_3_10ED(): pass

    label("Function_3_10ED")

    Sleep(800)
    OP_22(0xE6, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_3_10ED end

    def Function_4_10FD(): pass

    label("Function_4_10FD")

    OP_8F(0xFE, 0xFFFE6D30, 0x17A2, 0xFFFE9B20, 0x7D0, 0x0)
    Return()

    # Function_4_10FD end

    def Function_5_1112(): pass

    label("Function_5_1112")

    OP_8E(0xFE, 0xFFFE8F54, 0x15AE, 0xFFFE951C, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8EC8, 0x15AE, 0xFFFE9FC6, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8C52, 0x15AE, 0xFFFEA0FC, 0x5DC, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_5_1112 end

    SaveToFile()

Try(main)
