from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3230   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3230.x',
        MapIndex            = 1,
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
        'Mao',                                  # 9
        'Combustion Engine',                    # 10
        'ガソリンタンク',                       # 11
        'ガソリンタンク',                       # 12
        'ガソリンタンク',                       # 13
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT06/CH20020 ._CH',             # 01
        'ED6_DT06/CH20020 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT06/CH20020P._CP',             # 01
        'ED6_DT06/CH20020P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 458753,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966081,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966081,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966081,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_162",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_208",          # 02, 2
        "Function_3_23B",          # 03, 3
        "Function_4_AA9",          # 04, 4
        "Function_5_B15",          # 05, 5
        "Function_6_B86",          # 06, 6
        "Function_7_BD3",          # 07, 7
        "Function_8_C20",          # 08, 8
        "Function_9_DA9",          # 09, 9
        "Function_10_1981",        # 0A, 10
        "Function_11_2031",        # 0B, 11
        "Function_12_20BA",        # 0C, 12
    )


    def Function_0_162(): pass

    label("Function_0_162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176")
    SetMapFlags(0x10000000)
    Event(0, 3)
    Jump("loc_1B9")

    label("loc_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_1B9")

    label("loc_195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_1B9")

    Return()

    # Function_0_162 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1F3")
    SetChrPos(0x9, -20, 250, 8200, 270)
    OP_A1(0x9, 0x3)
    OP_72(0x3, 0x4)
    OP_22(0xA1, 0x1, 0xC8)
    OP_22(0xCF, 0x1, 0x64)
    OP_43(0x9, 0x1, 0x0, 0x2)
    Jump("loc_207")

    label("loc_1F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202")
    Jump("loc_207")

    label("loc_202")

    OP_22(0xA1, 0x1, 0xC8)

    label("loc_207")

    Return()

    # Function_1_1BA end

    def Function_2_208(): pass

    label("Function_2_208")

    OP_22(0xA1, 0x1, 0x64)
    OP_22(0xCF, 0x1, 0x64)
    OP_C4(0x0, 0x20)

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23A")
    OP_7C(0x0, 0x14, 0xBB8, 0x64)
    Sleep(100)
    Jump("loc_218")

    label("loc_23A")

    Return()

    # Function_2_208 end

    def Function_3_23B(): pass

    label("Function_3_23B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_252")
    Call(0, 11)
    Call(0, 12)

    label("loc_252")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-1190, 0, 5790, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(284, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0xF8, 0x1, 0x0, 0x6)
    OP_43(0xF9, 0x1, 0x0, 0x7)

    def lambda_2CF():
        OP_6D(-1190, 0, 5790, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CF)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #0
        0x101,
        "#1015F#5PYeah, it's totally stopped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1035F#6PIt's an old device, but it's still orbal driven.\x02\x03",

            "#1043FIt's affected by the Orbal Shutdown\x01",
            "Phenomenon just like everything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1007F#5PHmmm...\x02\x03",

            "#1015FBut, the pump's ultimately just to deliver\x01",
            "hot water from the spring there, right?\x02\x03",

            "I feel like there might be something\x01",
            "we can do...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C3")

    ChrTalk(    #3
        0x108,
        (
            "#074FWe can't exactly carry it by bucket.\x02\x03",

            "#072FWe've got to find some way to\x01",
            "make this device work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD")

    label("loc_4C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54A")

    ChrTalk(    #4
        0x103,
        (
            "#026F#5PWe can't exactly just carry it all by bucket.\x02\x03",

            "#022FWe've got to find some way to\x01",
            "make this device work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CD")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CD")

    ChrTalk(    #5
        0x106,
        (
            "#053F#5PCan't solve this one just by using a bucket.\x02\x03",

            "#050FWe've got to find some way to\x01",
            "make this device work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #6
        0x101,
        (
            "#1004F#2POh, could we use a Zero Field Generator\x01",
            "on the pump?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #7
        0x102,
        (
            "#1035F#6PMmm, doubtful.\x02\x03",

            "#1040FAccording to the professor, they're limited to\x01",
            "orbments no bigger than ones you can carry \x01",
            "in both hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1007F#2PHmm. Guess not, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#064F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_70C():

        label("loc_70C")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_70C")

    QueueWorkItem2(0x102, 1, lambda_70C)
    Sleep(500)

    ChrTalk(    #10
        0x102,
        "#1044F#7PTita, what is it?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0xC2, 0x1, 0x2)
    Call(0, 9)
    Jump("loc_AA8")

    label("loc_74C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_902")
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x106, 0x102, 400)

    ChrTalk(    #11
        0x106,
        (
            "#052F#5POh, yeah. How about using one of the Zero\x01",
            "Field Generators on the pump?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D3():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F9")

    def lambda_7EE():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7EE)
    Jump("loc_807")

    label("loc_7F9")


    def lambda_7FF():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_7FF)

    label("loc_807")

    TurnDirection(0x102, 0x106, 400)
    Sleep(500)

    ChrTalk(    #12
        0x102,
        (
            "#1035F#7PMmm, doubtful.\x02\x03",

            "#1040FAccording to the professor, they're limited to\x01",
            "orbments no bigger than ones you can carry \x01",
            "in both hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x106,
        "#555F#5PHm... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1007F#2PIsn't there something we can do...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0xC2, 0x1, 0x2)
    EventEnd(0x0)
    Jump("loc_AA8")

    label("loc_902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA8")
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #15
        0x103,
        (
            "#023F#5PCould we possibly use a Zero Field\x01",
            "Generator on the pump?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_97B():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A1")

    def lambda_996():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_996)
    Jump("loc_9AF")

    label("loc_9A1")


    def lambda_9A7():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_9A7)

    label("loc_9AF")

    TurnDirection(0x102, 0x103, 400)
    Sleep(500)

    ChrTalk(    #16
        0x102,
        (
            "#1035F#7PI'm afraid not.\x02\x03",

            "#1040FAccording to the professor, they're limited to\x01",
            "orbments no bigger than ones you can carry \x01",
            "in both hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        "#025F#5PAh... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1007F#2PIsn't there something we can do...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2009)
    OP_28(0xC2, 0x1, 0x2)
    EventEnd(0x0)

    label("loc_AA8")

    Return()

    # Function_3_23B end

    def Function_4_AA9(): pass

    label("Function_4_AA9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AD0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AD0)
    OP_8E(0xFE, 0x1EA, 0x0, 0x11EE, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_AA9 end

    def Function_5_B15(): pass

    label("Function_5_B15")

    Sleep(700)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_B41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B41)
    OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0x119E, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_5_B15 end

    def Function_6_B86(): pass

    label("Function_6_B86")

    Sleep(1400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BB2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB2)
    OP_8E(0xFE, 0x352, 0x0, 0xD16, 0x7D0, 0x0)
    Return()

    # Function_6_B86 end

    def Function_7_BD3(): pass

    label("Function_7_BD3")

    Sleep(2100)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 100, 0, -230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_BFF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BFF)
    OP_8E(0xFE, 0xFFFFFD76, 0x0, 0xD48, 0x7D0, 0x0)
    Return()

    # Function_7_BD3 end

    def Function_8_C20(): pass

    label("Function_8_C20")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-1190, 0, 5790, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(284, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0xF8, 0x1, 0x0, 0x6)
    OP_43(0xF9, 0x1, 0x0, 0x7)

    def lambda_C9F():
        OP_6D(-1190, 0, 5790, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C9F)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #19
        0x101,
        (
            "#1015F#5PHmmm, if only we could do something\x01",
            "to get the pump moving...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#1043F#6PYeah... It would have been nice if we\x01",
            "could use a Zero Field Generator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        "#064F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_D74():

        label("loc_D74")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_D74")

    QueueWorkItem2(0x102, 1, lambda_D74)
    Sleep(500)

    ChrTalk(    #22
        0x102,
        "#1044F#7PTita, what is it?\x02",
    )

    CloseMessageWindow()
    Call(0, 9)
    Return()

    # Function_8_C20 end

    def Function_9_DA9(): pass

    label("Function_9_DA9")


    def lambda_DAF():

        label("loc_DAF")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_DAF")

    QueueWorkItem2(0x101, 1, lambda_DAF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDB")

    def lambda_DCD():

        label("loc_DCD")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_DCD")

    QueueWorkItem2(0xF9, 1, lambda_DCD)
    Jump("loc_DEC")

    label("loc_DDB")


    def lambda_DE1():

        label("loc_DE1")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_DE1")

    QueueWorkItem2(0xF8, 1, lambda_DE1)

    label("loc_DEC")

    Sleep(500)

    ChrTalk(    #23
        0x107,
        "#560F#5PY-Yeah...\x02",
    )

    CloseMessageWindow()

    def lambda_E0E():
        OP_6D(-270, 250, 7300, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E0E)

    def lambda_E26():
        OP_67(0, 6120, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E26)

    def lambda_E3E():
        OP_6B(2620, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E3E)

    def lambda_E4E():
        OP_6E(302, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_E4E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA3")

    def lambda_E6B():
        OP_8E(0xFE, 0x5B4, 0x0, 0x122A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E6B)
    WaitChrThread(0x107, 0x1)

    def lambda_E8B():
        OP_8E(0xFE, 0xFFFFFF38, 0xFA, 0x1D92, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E8B)
    Jump("loc_EDE")

    label("loc_EA3")


    def lambda_EA9():
        OP_8E(0xFE, 0xFFFFF97A, 0x0, 0x1216, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_EA9)
    WaitChrThread(0x107, 0x1)

    def lambda_EC9():
        OP_8E(0xFE, 0xFFFFFF38, 0xFA, 0x1D92, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_EC9)

    label("loc_EDE")

    Sleep(500)
    WaitChrThread(0x107, 0x1)
    Sleep(700)
    OP_8C(0x107, 315, 400)
    OP_8E(0x107, 0xFFFFFABA, 0xFA, 0x1ED2, 0xBB8, 0x0)
    OP_8C(0x107, 270, 300)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_8E(0x107, 0xFFFFFA9C, 0xFA, 0x1A0E, 0xBB8, 0x0)
    OP_8C(0x107, 270, 300)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_8E(0x107, 0x9C4, 0x0, 0x1612, 0xFA0, 0x0)
    OP_8C(0x107, 90, 300)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_8E(0x107, 0x226, 0xFA, 0x1946, 0xBB8, 0x0)
    OP_8E(0x107, 0xA0, 0xFA, 0x2288, 0xBB8, 0x0)
    OP_8C(0x107, 0, 400)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(    #24
        0x107,
        (
            "#062F#6PUm, um...\x02\x03",

            "So this would go like this...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107D")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10BB")

    label("loc_107D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A4")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_10BB")

    label("loc_10A4")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_10BB")

    Jump("loc_1123")

    label("loc_10BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E5")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1123")

    label("loc_10E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110C")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1123")

    label("loc_110C")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1123")

    Sleep(1000)

    ChrTalk(    #25
        0x101,
        "#1016F#5PUmmmm, Tita?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118F")

    ChrTalk(    #26
        0x106,
        (
            "#555F#5POh, man...\x01",
            "She's got that look in her eye again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118F")


    ChrTalk(    #27
        0x107,
        (
            "#560F#6PWell, unlike recent stuff, it doesn't\x01",
            "have a very complex orbal mechanism.\x02\x03",

            "So all I need to do is take this thing\x01",
            "here, then connect it to that thing over\x01",
            "here... \x02\x03",

            "#064FOh, and don't you worry! I'll put things\x01",
            "right back the way things were after the\x01",
            "Orbal Shutdown Phenomenon.\x02\x03",

            "#062F...\x02\x03",

            "#061FYeah... This should do it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)
    Sleep(500)

    ChrTalk(    #28
        0x107,
        (
            "#560F#4PI think I might actually be able\x01",
            "to get the pump working.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139E")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13DC")

    label("loc_139E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C5")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13DC")

    label("loc_13C5")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_13DC")

    Jump("loc_1444")

    label("loc_13DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1406")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1444")

    label("loc_1406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_142D")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1444")

    label("loc_142D")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1444")

    Sleep(1000)

    ChrTalk(    #29
        0x101,
        "#1004F#5PWhaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1044F#5PYou're not going to use a Zero Field\x01",
            "Generator, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        (
            "#067F#4PHeehee, no, no.\x02\x03",

            "#560FYou remember, right, Joshua?\x01",
            "The combustion engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        "#1044F#5PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015F#5PThe combustion engine...\x01",
            "You mean the one we used on the\x01",
            "workshop devices before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x107,
        (
            "#061F#4PYep. ♪\x02\x03",

            "#560FUnlike the workshop equipment,\x01",
            "the pump device doesn't have a very\x01",
            "complex mechanism.\x02\x03",

            "If we can make the combustion engine\x01",
            "drive the parts the orbment was working,\x01",
            "it should work as-is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1004F#5PI, uh, see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1040F#5PI hadn't considered that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D8")

    ChrTalk(    #37
        0x106,
        "#051F#5PSo, where can we find this combustion engine?\x02",
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_16D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_171B")

    ChrTalk(    #38
        0x103,
        "#020F#5PSo, where is this combustion engine?\x02",
    )

    CloseMessageWindow()
    Jump("loc_175B")

    label("loc_171B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175B")

    ChrTalk(    #39
        0x108,
        "#070F#5PSo, where is this combustion engine?\x02",
    )

    CloseMessageWindow()

    label("loc_175B")


    ChrTalk(    #40
        0x107,
        (
            "#560F#4PUmm, I think it was stored at the landing port.\x02\x03",

            "#061FWe should be able to find out if\x01",
            "we ask the maintenance chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1006F#5PMaintenance Chief Gustav at the\x01",
            "landing port, huh.\x02\x03",

            "#1015FThat reminds me, won't we need fuel to\x01",
            "drive the combustion engine?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #42
        0x102,
        (
            "#1040F#5PGasoline, right.\x02\x03",

            "Like before, we should ask down below\x01",
            "at the central factory.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-220, 0, 4610, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -220, 0, 4610, 180)
    SetChrPos(0x1, -220, 0, 4610, 180)
    SetChrPos(0x2, -220, 0, 4610, 180)
    SetChrPos(0x3, -220, 0, 4610, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x200A)
    OP_28(0xC2, 0x1, 0x4)
    OP_28(0xC2, 0x1, 0x100)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_DA9 end

    def Function_10_1981(): pass

    label("Function_10_1981")

    EventBegin(0x0)
    SetChrPos(0xA, -820, 0, 4090, 315)
    SetChrPos(0xB, -40, 0, 4090, 315)
    SetChrPos(0xC, 700, 0, 4090, 315)
    SetChrPos(0x9, -30, 0, 5200, 90)
    OP_A1(0xA, 0x0)
    OP_72(0x0, 0x4)
    OP_A1(0xB, 0x1)
    OP_72(0x1, 0x4)
    OP_A1(0xC, 0x2)
    OP_72(0x2, 0x4)
    OP_A1(0x9, 0x3)
    OP_72(0x3, 0x4)
    SetChrPos(0x101, 850, 0, 1380, 0)
    SetChrPos(0x102, -350, 0, 1530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A43")
    SetChrPos(0xF8, 140, 0, 2750, 180)
    SetChrPos(0xF9, 270, 0, 190, 0)
    Jump("loc_1A65")

    label("loc_1A43")

    SetChrPos(0xF9, 140, 0, 2750, 180)
    SetChrPos(0xF8, 270, 0, 190, 0)

    label("loc_1A65")

    OP_6D(-970, 0, 3460, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(319, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #43
        0x107,
        (
            "#560F#4POkay, I've got the materials...\x02\x03",

            "#061FTime to upgrade the pump!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1006F#5PAh, yeah.\x02\x03",

            "#1016FStill, though, are you sure you don't need help?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #45
        0x107,
        (
            "#560F#4PAh... Umm, um, well...\x02\x03",

            "#061FI've prepared a diagram for the upgrades,\x01",
            "so would you separate the parts like it says?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1001F#5PSure. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1040F#6PThat seems like something even we can do.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C56")

    ChrTalk(    #48
        0x106,
        "#051F#1PFine, guess I'll help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1C56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C96")

    ChrTalk(    #49
        0x103,
        "#021F#1PWell, then, allow me to help too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1C96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CCF")

    ChrTalk(    #50
        0x108,
        "#070F#1PThen I guess I will help too.\x02",
    )

    CloseMessageWindow()

    label("loc_1CCF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_6D(-210, 250, 6480, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, -20, 250, 8200, 270)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    SetChrPos(0x101, 450, 0, 4800, 0)
    SetChrPos(0x102, -670, 0, 4590, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7F")
    SetChrPos(0xF9, -60, 0, 3240, 0)
    Jump("loc_1D90")

    label("loc_1D7F")

    SetChrPos(0xF8, -60, 0, 3240, 0)

    label("loc_1D90")

    SetChrPos(0x107, -10, 250, 6830, 0)
    OP_D2(0x70065, 0x7006D, 0x3)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 3)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x107,
        (
            "#062F#6PAll right...\x01",
            "Yep, it's finished.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #52
        0x101,
        "#1001F#5PAll right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#1049F#6PGood work, Tita.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E93")

    ChrTalk(    #54
        0x106,
        (
            "#051F#1PSame as always.\x01",
            "You sure are good with this stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1E93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC6")

    ChrTalk(    #55
        0x103,
        "#027F#1PAs skillful as ever.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0C")

    ChrTalk(    #56
        0x108,
        "#070F#1PIt's nothing new, but you really are good.\x02",
    )

    CloseMessageWindow()

    label("loc_1F0C")


    ChrTalk(    #57
        0x107,
        (
            "#067F#4PHeehee, we don't know if it'll work\x01",
            "or not yet...\x02\x03",

            "Let's test it right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x107, 3)
    OP_0D()
    Sleep(300)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xA1, 0x1, 0xC8)
    OP_22(0xCF, 0x1, 0x64)

    def lambda_1F9B():

        label("loc_1F9B")

        OP_7C(0x0, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1F9B")

    QueueWorkItem2(0x101, 2, lambda_1F9B)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#1004F#5PWh-Whoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1040F#6PLooks like the rotor in the pump's started moving.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x40C, 3)
    OP_3F(0x40D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1981 end

    def Function_11_2031(): pass

    label("Function_11_2031")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20AD"),
        (1, "loc_20B3"),
        (SWITCH_DEFAULT, "loc_20B9"),
    )


    label("loc_20AD")

    OP_A2(0x1200)
    Jump("loc_20B9")

    label("loc_20B3")

    OP_A2(0x1201)
    Jump("loc_20B9")

    label("loc_20B9")

    Return()

    # Function_11_2031 end

    def Function_12_20BA(): pass

    label("Function_12_20BA")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_12_20BA end

    SaveToFile()

Try(main)
