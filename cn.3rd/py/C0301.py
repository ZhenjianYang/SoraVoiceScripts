from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0301.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        '魔兽',                                 # 9
        '目标用照相机',                         # 10
        '',                                     # 11
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10240 ._CH',             # 00
        'ED6_DT09/CH10241 ._CH',             # 01
        'ED6_DT26/CH20789 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT09/CH10240P._CP',             # 00
        'ED6_DT09/CH10241P._CP',             # 01
        'ED6_DT26/CH20789P._CP',             # 02
    )

    DeclNpc(
        X                   = 51470,
        Z                   = 0,
        Y                   = 20950,
        Direction           = 315,
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


    ScpFunction(
        "Function_0_102",          # 00, 0
        "Function_1_118",          # 01, 1
        "Function_2_119",          # 02, 2
    )


    def Function_0_102(): pass

    label("Function_0_102")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_117")

    Return()

    # Function_0_102 end

    def Function_1_118(): pass

    label("Function_1_118")

    Return()

    # Function_1_118 end

    def Function_2_119(): pass

    label("Function_2_119")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(9680, -300, -6520, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(4030, 0)
    OP_6C(257000, 0)
    OP_6E(262, 0)
    LoadEffect(0x0, "map\\\\mp287_00.eff")
    OP_11(0x46, 0x6E, 0x78, 0x4E20, 0x13880, 0x0)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    StopSound(0x7530, 0x13880, 0xFA0)

    def lambda_1A7():
        OP_6D(8610, -330, -6740, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1A7)

    def lambda_1BF():
        OP_6B(3530, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BF)

    def lambda_1CF():
        OP_67(0, 4970, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1CF)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    Fade(500)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, 8080, -40, -14430, 0)

    def lambda_216():
        OP_8E(0xFE, 0x2A12, 0xFFFFFEB6, 0xFFFFE782, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_216)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#290F哈哈哈，\x01",
            "已经闻到猎物的气味了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 120, 400)
    Sleep(800)
    OP_8C(0x101, 310, 400)
    Sleep(800)

    ChrTalk(    #1
        0x101,
        "#296F唔，就在这附近吧。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    OP_8C(0x101, 260, 400)

    def lambda_2B9():
        OP_8E(0xFE, 0x1B3A, 0x46, 0xFFFFDFE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B9)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 210, 400)
    Sleep(1500)
    OP_8C(0x101, 300, 400)
    Sleep(300)

    def lambda_2F1():
        OP_8F(0xFE, 0x16A8, 0x12C, 0xFFFFE804, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        (
            "#291F#6P好，就决定在这棵树下了！\x01",
            "这就是所谓的自我主张吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x23, 0x0, 0x64)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFF, 5280, 1300, -5560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #3
        0x101,
        (
            "#291F#6P刷刷…………\x02\x03",

            "#290F嗯，这样就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 35, 400)

    def lambda_3E7():
        OP_8E(0xFE, 0x3340, 0x12C, 0xC3A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E7)
    Sleep(2500)
    Fade(2000)
    OP_6D(13730, 300, 5680, 0)
    OP_67(0, 2870, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(13000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(300)
    OP_8C(0x101, 220, 400)
    Sleep(300)

    ChrTalk(    #4
        0x101,
        (
            "#292F…………目标就只有大家伙。\x02\x03",

            "不管怎么说，那可是传说中的虫啊。\x01",
            "肯定也会让约修亚吓一跳的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#291F哇哈哈…………\x02",
    )


    def lambda_4EE():
        OP_6D(15860, 300, 7490, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4EE)

    def lambda_506():
        OP_67(0, 2510, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_506)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 23860, 100, 13050, 220)
    OP_9F(0x10, 0x0, 0x0, 0x0, 0xFF, 0x0)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)

    def lambda_549():
        OP_8F(0xFE, 0x410A, 0x64, 0x1464, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_549)
    WaitChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0x11, 0x0)
    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_57E():
        OP_6B(3530, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_57E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_119 end

    SaveToFile()

Try(main)
