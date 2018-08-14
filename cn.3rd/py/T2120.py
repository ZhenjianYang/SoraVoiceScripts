from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2120   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2120   ._SN',
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
        '欧尼尔',                               # 9
        '克拉姆',                               # 10
        '目标用照相机',                         # 11
        '',                                     # 12
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
    )

    DeclNpc(
        X                   = 30000,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_133",          # 01, 1
        "Function_2_134",          # 02, 2
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132")
    Event(0, 2)

    label("loc_132")

    Return()

    # Function_0_11A end

    def Function_1_133(): pass

    label("Function_1_133")

    Return()

    # Function_1_133 end

    def Function_2_134(): pass

    label("Function_2_134")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 30400, 0, 2300, 0)
    SetChrPos(0x14E, 32540, 0, 4580, 0)
    OP_6D(30260, 500, 3220, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #0
        0x11,
        "#774F#3S幸福之石～！？\x02",
    )

    OP_7C(0x0, 0xF0, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "嗯，据说是闪耀着\x01",
            "金色光芒的魔法石，\x01",
            "能为拥有它的人带来幸福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "……你知道很久以前\x01",
            "女神创造这片大陆的事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "当时女神的力量\x01",
            "化为细小的光珠撒遍大地，\x01",
            "那真是神奇无比的光辉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "……最后虽然光芒消失了，\x01",
            "但据说在高耸的山峦云霞另一端\x01",
            "还残留有极其稀少的光珠。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "而其在天空近旁\x01",
            "度过了漫长的年月，\x01",
            "一点一点地成长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "……那就是幸福之石。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        "#772F#3S好、好厉害～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "哇哈哈，\x01",
            "是吧是吧！\x02",
        )
    )

    Jump("loc_3B2")

    label("loc_3B2")

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "而且那石头，\x01",
            "可不是随随便便就能找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "因为啊，\x01",
            "那可是生长在高山深处的\x01",
            "神奇石头哦？\x02",
        )
    )

    Jump("loc_429")

    label("loc_429")

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#772F那、那么说……？\x02\x03",

            "欧尼尔叔叔\x01",
            "在最北方的冒险中\x01",
            "找到它了吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "嗯，当然啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "灵峰特基斯，\x01",
            "那可是被冰雪封冻的险峻山峰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "让人目眩的断崖绝壁，\x01",
            "夹杂着冰雹的暴风雪！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "不知何时食物也吃得见底了，\x01",
            "我在茫茫的白色沙漠中彷徨……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "有时被前所未见的魔兽袭击，\x01",
            "有时安全绳索断了，\x01",
            "头朝下摔到危险的谷底。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "但我欧尼尔船长\x01",
            "可不会死在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "我就这样紧紧抓住\x01",
            "剃刀般的冰壁……\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x11, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    OP_95(0x11, 0x0, 0x12C, 0x0, 0x12C, 0x1388)

    ChrTalk(    #19
        0x11,
        "#771F哦哦～太酷了！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "嗯嗯，\x01",
            "无论什么时候都绝对不能放弃哦。\x02",
        )
    )

    Jump("loc_679")

    label("loc_679")

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #21
        0x10,
        (
            "#3S像不屈的男子汉，\x01",
            "我欧尼尔船长一样！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "没错，我经过重重试炼，\x01",
            "终于找到了。\x01",
            "那发出微弱光芒的石头……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "……我用颤抖的手拿起它。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "然后不可思议地，\x01",
            "那样狂暴的风\x01",
            "居然突然就停了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "然后朝阳从云间照射下来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "石头接受了阳光，\x01",
            "开始闪耀出光辉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "那简直就是，\x01",
            "来自另一个世界的美景啊…………！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7FE():
        OP_6B(2860, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7FE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_134 end

    SaveToFile()

Try(main)
