from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0600_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0600_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_E8E",          # 01, 1
        "Function_2_110A",         # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xF7, -1300, 0, -6990, 0)
    SetChrPos(0xF8, -500, 0, -7670, 0)
    SetChrPos(0xF9, 950, 0, -6790, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F")
    SetChrPos(0xF9, -500, 0, -7670, 0)
    SetChrPos(0xF8, 750, 0, -6790, 0)

    label("loc_11F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E")
    SetChrPos(0xF9, -500, 0, -7670, 0)
    SetChrPos(0xF8, 750, 0, -6790, 0)

    label("loc_14E")

    OP_6D(1300, 0, -3480, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#1011F#5PI was wondering what we were\x01",
            "going to find here...\x02\x03",

            "#1015F...but it's just a bunch of junk.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20A():
        OP_90(0xFE, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20A)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253")

    ChrTalk(    #1 op#A
        0x108,
        "#076F#8AEstelle, hold on!\x02",
    )

    Jump("loc_2CF")

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284")

    ChrTalk(    #2 op#A
        0x106,
        "#054F#8AEstelle, watch out!\x02",
    )

    Jump("loc_2CF")

    label("loc_284")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0")

    ChrTalk(    #3 op#A
        0x104,
        "#530F#8AEstelle, wait!\x02",
    )

    Jump("loc_2CF")

    label("loc_2B0")


    ChrTalk(    #4 op#A
        0x103,
        "#024F#8AEstelle, look out!\x02",
    )


    label("loc_2CF")

    Sleep(500)
    OP_44(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)

    def lambda_2FA():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFE890, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FA)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 0, 0, 2200, 180)
    SetChrPos(0x9, 2200, 0, 2200, 180)
    SetChrPos(0xA, -2200, 0, 2200, 180)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_20(0x7D0)
    OP_22(0x26D, 0x0, 0x64)
    OP_82(0x80, 0x2)
    OP_79(0x0, 0x2)
    OP_7B()
    OP_77(0xE0, 0xE0, 0xE0, 0x0, 0x320)
    Sleep(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Sleep(1000)
    OP_22(0x26D, 0x0, 0x64)
    OP_82(0x80, 0x2)
    OP_79(0x0, 0x2)
    OP_7B()
    OP_77(0xC0, 0xC0, 0xC0, 0x0, 0x7D0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xA, 0x800)
    OP_22(0x28C, 0x0, 0x64)
    OP_43(0x8, 0x2, 0x1, 0x2)

    def lambda_42C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_42C)
    Sleep(200)
    OP_43(0x9, 0x2, 0x1, 0x2)

    def lambda_44A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_44A)
    Sleep(100)
    OP_43(0xA, 0x2, 0x1, 0x2)

    def lambda_468():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_468)
    Sleep(2000)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_496")
    SetChrChipByIndex(0x104, 4)

    label("loc_496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A9")
    SetChrChipByIndex(0x105, 5)

    label("loc_4A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BC")
    SetChrChipByIndex(0x106, 6)

    label("loc_4BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CF")
    SetChrChipByIndex(0x107, 7)

    label("loc_4CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E2")
    SetChrChipByIndex(0x108, 8)

    label("loc_4E2")

    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    SetChrChipByIndex(0x101, 2)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x9, 0x2)
    WaitChrThread(0xA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_546")
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #5
        0x107,
        "#065FUh oh...\x02",
    )

    CloseMessageWindow()

    label("loc_546")


    ChrTalk(    #6
        0x101,
        "#1005F#2PWhat the heck are--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#024FAsk questions later!\x02\x03",

            "For now, stand your ground\x01",
            "and fight!\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5BF():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_5BF)

    def lambda_5DD():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_5DD)

    def lambda_5FB():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5FB)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 0)
    SetChrChipByIndex(0xA, 0)
    Sleep(200)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    Battle(0xCE4, 0x0, 0x0, 0x0, 0xFF)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_655"),
        (SWITCH_DEFAULT, "loc_658"),
    )


    label("loc_655")

    OP_B4(0x0)
    Return()

    label("loc_658")

    FadeToDark(0, 0, -1)
    OP_82(0x80, 0x0)
    EventBegin(0x0)
    OP_6D(1300, 0, -2480, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 0, -3000, 0)
    SetChrPos(0xF7, -1500, 0, -4190, 270)
    SetChrPos(0xF8, -500, 0, -5670, 180)
    SetChrPos(0xF9, 1150, 0, -4090, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_717")
    SetChrPos(0xF9, -500, 0, -5670, 180)
    SetChrPos(0xF8, 750, 0, -4790, 90)

    label("loc_717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746")
    SetChrPos(0xF9, -500, 0, -5670, 180)
    SetChrPos(0xF8, 750, 0, -4790, 90)

    label("loc_746")

    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x103, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_763")
    SetChrChipByIndex(0x104, 4)

    label("loc_763")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_776")
    SetChrChipByIndex(0x105, 5)

    label("loc_776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_789")
    SetChrChipByIndex(0x106, 6)

    label("loc_789")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79C")
    SetChrChipByIndex(0x107, 7)

    label("loc_79C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AF")
    SetChrChipByIndex(0x108, 8)

    label("loc_7AF")

    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xA, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_79(0x0, 0x2)
    OP_7B()
    OP_77(0xC0, 0xC0, 0xC0, 0x0, 0x0)
    OP_6D(240, 0, -3900, 0)
    SetChrPos(0xB, 0, 0, -3900, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #8
        0x101,
        "#1002FPhew!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_849")

    ChrTalk(    #9
        0x108,
        "#070FThat takes care of that!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F1")

    label("loc_849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88D")

    ChrTalk(    #10
        0x106,
        (
            "#050FOne less thing to worry about,\x01",
            "I guess. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F1")

    label("loc_88D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B7")

    ChrTalk(    #11
        0x104,
        "#030FArtfully done.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8F1")

    label("loc_8B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F1")

    ChrTalk(    #12
        0x105,
        "#042FLooks like we pushed them back...\x02",
    )

    CloseMessageWindow()

    label("loc_8F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91E")

    ChrTalk(    #13
        0x107,
        "#561FThat was scary...\x02",
    )

    CloseMessageWindow()
    Jump("loc_981")

    label("loc_91E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_941")

    ChrTalk(    #14
        0x105,
        "#042FIndeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_981")

    label("loc_941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #15
        0x104,
        "#031FIndeed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_981")

    label("loc_964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_981")

    ChrTalk(    #16
        0x106,
        "#051FYep.\x02",
    )

    CloseMessageWindow()

    label("loc_981")

    OP_22(0x86, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    Sleep(400)
    OP_82(0x80, 0x2)
    OP_79(0x0, 0x2)
    OP_7B()
    Sleep(800)
    OP_22(0x86, 0x0, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7A(0x0, 0x2)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(500)
    SetChrChipByIndex(0x101, 65535)

    def lambda_A2A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A2A)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(200)
    SetChrChipByIndex(0x103, 65535)

    def lambda_A47():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_A47)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A67")
    SetChrChipByIndex(0x104, 65535)

    label("loc_A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7A")
    SetChrChipByIndex(0x105, 65535)

    label("loc_A7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8D")
    SetChrChipByIndex(0x106, 65535)

    label("loc_A8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA0")
    SetChrChipByIndex(0x107, 65535)

    label("loc_AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB3")
    SetChrChipByIndex(0x108, 65535)

    label("loc_AB3")


    def lambda_AB9():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_AB9)

    def lambda_AC7():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_AC7)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x103, 0x3)
    WaitChrThread(0xF8, 0x3)
    WaitChrThread(0xF9, 0x3)

    ChrTalk(    #17
        0x101,
        (
            "#1007FOh, man, I'm still shaking.\x02\x03",

            "Having something like that come\x01",
            "at you from outta nowhere... Be still,\x01",
            "my quaking nerves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#027FYeah, I've never seen monsters\x01",
            "quite like those before.\x02\x03",

            "I suppose this is our phantom\x01",
            "thief's way of saying hello?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5C")

    ChrTalk(    #19
        0x104,
        (
            "#030FFor an uncouth villain such as he?\x01",
            "Likely.\x02\x03",

            "This seems to be the last obstacle,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCE")

    label("loc_C5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD0")

    ChrTalk(    #20
        0x106,
        (
            "#050FKnowing him, wouldn't surprise\x01",
            "me.\x02\x03",

            "Still, I think he's run out of stuff to\x01",
            "throw at us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCE")

    label("loc_CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D42")

    ChrTalk(    #21
        0x108,
        (
            "#070FSeems likely, from what I've heard.\x02\x03",

            "I think that's the last of his surprises,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCE")

    label("loc_D42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCE")

    ChrTalk(    #22
        0x105,
        (
            "#047FKnowing him, it wouldn't surprise me.\x02\x03",

            "#040FI don't think we'll have any more\x01",
            "problems from here on out, at least. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCE")


    ChrTalk(    #23
        0x103,
        (
            "#020FRight, all that remains now is\x01",
            "getting that commission letter\x01",
            "back.\x02\x03",

            "Let's look around. It must be in\x01",
            "this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015FOh, right, probably shouldn't\x01",
            "forget that...\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x77, 0x1, 0x4000)
    OP_65(0x2, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_E8E(): pass

    label("Function_1_E8E")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "Found the #2C#16IOre Mine Commission Letter#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #26
        0x101,
        "#1018FOkay! Letter recovered!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F68")

    ChrTalk(    #27
        0x107,
        (
            "#060FLet's go return it!\x02\x03",

            "I'm sure Mr. Gaton is waiting\x01",
            "for us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C5")

    label("loc_F68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCD")

    ChrTalk(    #28
        0x105,
        (
            "#040FLet's return it as soon as possible.\x02\x03",

            "I'm sure the mine chief is worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C5")

    label("loc_FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1061")

    ChrTalk(    #29
        0x104,
        (
            "#031FCome then, let us fly away\x01",
            "to return it.\x02\x03",

            "No doubt our dear mine chief\x01",
            "has worried himself silly over\x01",
            "this little thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C5")

    label("loc_1061")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C5")

    ChrTalk(    #30
        0x106,
        (
            "#051FLet's get out of here, then.\x02\x03",

            "I'm sure the old man is worried\x01",
            "sick over it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C5")


    ChrTalk(    #31
        0x103,
        "#021FProbably.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #32
        0x101,
        "#1006FRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0111   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_1_E8E end

    def Function_2_110A(): pass

    label("Function_2_110A")

    OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_2_110A end

    SaveToFile()

Try(main)
