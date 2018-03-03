from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4168   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4168.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -15730,
        Y                   = -1000,
        Z                   = -18230,
        Range               = -26740,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xFFFFD6B6,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -19450,
        TriggerZ            = 0,
        TriggerY            = -15500,
        TriggerRange        = 1000,
        ActorX              = -20540,
        ActorZ              = -500,
        ActorY              = -17840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20540,
        TriggerZ            = -700,
        TriggerY            = -17840,
        TriggerRange        = 1000,
        ActorX              = -19600,
        ActorZ              = 500,
        ActorY              = -14960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_193",          # 01, 1
        "Function_2_1B0",          # 02, 2
        "Function_3_1B7",          # 03, 3
        "Function_4_B5E",          # 04, 4
        "Function_5_BC5",          # 05, 5
        "Function_6_C02",          # 06, 6
        "Function_7_C6E",          # 07, 7
        "Function_8_D52",          # 08, 8
        "Function_9_DAA",          # 09, 9
        "Function_10_DF4",         # 0A, 10
        "Function_11_E30",         # 0B, 11
        "Function_12_E5E",         # 0C, 12
        "Function_13_F42",         # 0D, 13
        "Function_14_F9A",         # 0E, 14
        "Function_15_FE4",         # 0F, 15
        "Function_16_1020",        # 10, 16
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Return()

    # Function_0_192 end

    def Function_1_193(): pass

    label("Function_1_193")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x1, 0x64)
    OP_1C(0x1, 0x0, 0x2)
    Return()

    # Function_1_193 end

    def Function_2_1B0(): pass

    label("Function_2_1B0")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_2_1B0 end

    def Function_3_1B7(): pass

    label("Function_3_1B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C7")
    Return()

    label("loc_1C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9")
    Return()

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 1)), scpexpr(EXPR_END)), "loc_1E1")
    Return()

    label("loc_1E1")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D")
    SetChrPos(0x109, -18500, 0, -12300, 180)
    SetChrPos(0x10F, -19930, 0, -12100, 180)
    SetChrPos(0x10B, -18970, 0, -14180, 180)
    SetChrPos(0x102, -20120, 0, -13800, 180)
    Jump("loc_2C2")

    label("loc_23D")

    SetChrPos(0x109, -18790, 0, -12570, 180)
    SetChrPos(0x10F, -17690, 0, -11000, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292")
    SetChrPos(0x10B, -18970, 0, -14180, 180)
    SetChrPos(0xF1, -19380, 0, -10920, 180)
    Jump("loc_2C2")

    label("loc_292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2")
    SetChrPos(0x10B, -18970, 0, -14180, 180)
    SetChrPos(0xF0, -19380, 0, -10920, 180)

    label("loc_2C2")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-21040, 0, -16650, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(224000, 0)
    OP_6E(362, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x10B,
        (
            "#213F#6PH-How did it end up here?\x02\x03",

            "#215FMaybe Kyle had to make an emergency landing\x01",
            "or something...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47D")

    ChrTalk(    #1
        0x102,
        "#1513F#12PI'm sure he would've been able to, anyway.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    Sleep(300)

    ChrTalk(    #2
        0x102,
        (
            "#1500F#11PWell, what should we do? Should we go have\x01",
            "a look inside together?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 270, 400)
    Sleep(300)

    ChrTalk(    #3
        0x10B,
        "#210F#6PO-Oh... Yeah, if you wouldn't mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_505")

    label("loc_47D")


    ChrTalk(    #4
        0x109,
        (
            "#1065F#6PMaybe.\x02\x03",

            "#1060FWell, what do you want to do? Do you want\x01",
            "to have a look inside?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 0, 400)
    Sleep(300)

    ChrTalk(    #5
        0x10B,
        "#210F#5P...Yeah. I would.\x02",
    )

    CloseMessageWindow()

    label("loc_505")

    Sleep(300)

    def lambda_510():
        OP_6D(-22370, 0, -23640, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_510)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_586")
    SetChrPos(0x109, -18920, 0, -14160, 180)
    SetChrPos(0x10F, -17790, 0, -12650, 180)
    SetChrPos(0x10B, -23540, -610, -23920, 0)
    SetChrPos(0x102, -23540, -610, -23920, 0)
    Jump("loc_60B")

    label("loc_586")

    SetChrPos(0x109, -18920, 0, -14160, 180)
    SetChrPos(0x10F, -17790, 0, -12650, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0x10B, -23540, -610, -23920, 0)
    SetChrPos(0xF1, -19650, 0, -13060, 180)
    Jump("loc_60B")

    label("loc_5DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60B")
    SetChrPos(0x10B, -23540, -610, -23920, 0)
    SetChrPos(0xF0, -19650, 0, -13060, 180)

    label("loc_60B")

    OP_6D(-23270, -610, -24000, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(224000, 0)
    OP_6E(273, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C3")

    def lambda_686():
        OP_6D(-20010, 0, -17300, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_686)

    def lambda_69E():
        OP_6B(3260, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_69E)
    OP_43(0x10B, 0x0, 0x0, 0x5)
    OP_43(0x102, 0x0, 0x0, 0x6)
    WaitChrThread(0x10B, 0x0)
    WaitChrThread(0x102, 0x0)
    Jump("loc_6F7")

    label("loc_6C3")


    def lambda_6C9():
        OP_6D(-21170, -750, -17200, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C9)

    def lambda_6E1():
        OP_6B(3260, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E1)
    OP_43(0x10B, 0x0, 0x0, 0x4)
    WaitChrThread(0x10B, 0x0)

    label("loc_6F7")

    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #6
        0x10B,
        "#413F#5PSorry for the wait.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ED")

    ChrTalk(    #7
        0x109,
        (
            "#1067F#6PYou finish up looking everywhere you\x01",
            "wanted to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10B,
        "#215F#5PYeah... I've seen all I need to see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#1503F#5PThe engines wouldn't respond no matter\x01",
            "what we did, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_897")

    label("loc_7ED")


    ChrTalk(    #10
        0x109,
        (
            "#1067F#6PYou finish up looking everywhere you\x01",
            "wanted to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10B,
        (
            "#215F#5PYeah... I've seen all I need to see.\x02\x03",

            "The engines won't respond no matter\x01",
            "what I do, either...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_897")


    ChrTalk(    #12
        0x109,
        "#1841F#6PYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#12PAll we can do for now is keep going.\x02\x03",

            "#1448FI'm sure the Goddess will bless us if we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10B,
        (
            "#210F#5PI guess so.\x02\x03",

            "#211F...Right! Let's get back to work! I'm gonna find\x01",
            "them and make sure they never forget they owe\x01",
            "me one!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D7")

    ChrTalk(    #15
        0x102,
        "#1514F#5P...I think that's a great idea.\x02",
    )

    CloseMessageWindow()

    label("loc_9D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A11")

    ChrTalk(    #16
        0x107,
        "#067F#12PHeehee. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7F")

    label("loc_A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4B")

    ChrTalk(    #17
        0x10E,
        "#179F#12PHaha... That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7F")

    label("loc_A4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7F")

    ChrTalk(    #18
        0x10D,
        "#278F#12PHeh. That's the spirit.\x02",
    )

    CloseMessageWindow()

    label("loc_A7F")

    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-18680, 0, -12910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -18680, 0, -12910, 0)
    SetChrPos(0x1, -18680, 0, -12910, 0)
    SetChrPos(0x2, -18680, 0, -12910, 0)
    SetChrPos(0x3, -18680, 0, -12910, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2711)
    OP_28(0x2C, 0x1, 0x100)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_3_1B7 end

    def Function_4_B5E(): pass

    label("Function_4_B5E")


    def lambda_B64():
        OP_8E(0xFE, 0xFFFFA592, 0xFFFFFD9E, 0xFFFFAC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B64)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x1, 89)
    OP_70(0x1, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFAFEC, 0xFFFFFF9C, 0xFFFFABA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB064, 0xFFFFFCA4, 0xFFFFB78A, 0x7D0, 0x0)
    OP_71(0x1001, 0x0)
    ExitThread()
    Return()

    # Function_4_B5E end

    def Function_5_BC5(): pass

    label("Function_5_BC5")

    OP_8E(0xFE, 0xFFFFA592, 0xFFFFFD9E, 0xFFFFAC18, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAFEC, 0xFFFFFF9C, 0xFFFFABA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB064, 0xFFFFFCA4, 0xFFFFB78A, 0x7D0, 0x0)
    Return()

    # Function_5_BC5 end

    def Function_6_C02(): pass

    label("Function_6_C02")

    Sleep(700)

    def lambda_C0D():
        OP_8E(0xFE, 0xFFFFA592, 0xFFFFFD9E, 0xFFFFAC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0D)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x1, 89)
    OP_70(0x1, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFAFEC, 0xFFFFFF9C, 0xFFFFABA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFB262, 0xFFFFFDD0, 0xFFFFB3C0, 0x7D0, 0x0)
    OP_71(0x1001, 0x0)
    ExitThread()
    Return()

    # Function_6_C02 end

    def Function_7_C6E(): pass

    label("Function_7_C6E")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0xB)
    OP_43(0x1, 0x1, 0x0, 0xA)
    OP_43(0x2, 0x1, 0x0, 0x9)
    OP_43(0x3, 0x1, 0x0, 0x8)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_7_C6E end

    def Function_8_D52(): pass

    label("Function_8_D52")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_D52 end

    def Function_9_DAA(): pass

    label("Function_9_DAA")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_DAA end

    def Function_10_DF4(): pass

    label("Function_10_DF4")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_DF4 end

    def Function_11_E30(): pass

    label("Function_11_E30")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_E30 end

    def Function_12_E5E(): pass

    label("Function_12_E5E")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x10)
    OP_43(0x1, 0x1, 0x0, 0xF)
    OP_43(0x2, 0x1, 0x0, 0xE)
    OP_43(0x3, 0x1, 0x0, 0xD)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_12_E5E end

    def Function_13_F42(): pass

    label("Function_13_F42")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_F42 end

    def Function_14_F9A(): pass

    label("Function_14_F9A")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_14_F9A end

    def Function_15_FE4(): pass

    label("Function_15_FE4")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_FE4 end

    def Function_16_1020(): pass

    label("Function_16_1020")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_1020 end

    SaveToFile()

Try(main)
