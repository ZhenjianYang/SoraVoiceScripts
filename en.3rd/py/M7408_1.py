from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7408_1 ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/M7408   ._SN',
            'ED6_DT21/M7408_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_213",          # 02, 2
        "Function_3_2C7",          # 03, 3
        "Function_4_42CD",         # 04, 4
        "Function_5_42F0",         # 05, 5
        "Function_6_4313",         # 06, 6
        "Function_7_4351",         # 07, 7
        "Function_8_43A0",         # 08, 8
        "Function_9_43F4",         # 09, 9
        "Function_10_444D",        # 0A, 10
        "Function_11_449C",        # 0B, 11
        "Function_12_44F0",        # 0C, 12
        "Function_13_4553",        # 0D, 13
        "Function_14_45A8",        # 0E, 14
        "Function_15_45F7",        # 0F, 15
        "Function_16_4627",        # 10, 16
        "Function_17_4676",        # 11, 17
        "Function_18_46CA",        # 12, 18
        "Function_19_4799",        # 13, 19
        "Function_20_47B3",        # 14, 20
        "Function_21_4874",        # 15, 21
        "Function_22_4890",        # 16, 22
        "Function_23_48C5",        # 17, 23
        "Function_24_4914",        # 18, 24
        "Function_25_4968",        # 19, 25
        "Function_26_499D",        # 1A, 26
        "Function_27_49CD",        # 1B, 27
        "Function_28_4A1C",        # 1C, 28
        "Function_29_4A70",        # 1D, 29
        "Function_30_4A8C",        # 1E, 30
        "Function_31_4AAD",        # 1F, 31
        "Function_32_4AFC",        # 20, 32
        "Function_33_4B50",        # 21, 33
        "Function_34_4B80",        # 22, 34
        "Function_35_4BB5",        # 23, 35
        "Function_36_4C04",        # 24, 36
        "Function_37_4C58",        # 25, 37
        "Function_38_4C9C",        # 26, 38
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x334), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_109")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x335), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x336), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_133")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xE16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A")
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x49), scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16A")

    label("loc_161")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16A")

    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    OP_71(0x40E, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_71(0x410, 0x0)
    ExitThread()
    OP_71(0x411, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x421, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    Return()

    # Function_1_AB end

    def Function_2_213(): pass

    label("Function_2_213")

    Sleep(1500)
    OP_24(0x32E, 0x5A)
    OP_24(0x2F2, 0x5A)
    OP_24(0x137, 0x5A)
    Sleep(300)
    OP_24(0x32E, 0x50)
    OP_24(0x2F2, 0x50)
    OP_24(0x137, 0x50)
    Sleep(300)
    OP_24(0x32E, 0x46)
    OP_24(0x2F2, 0x46)
    OP_24(0x137, 0x46)
    Sleep(300)
    OP_24(0x32E, 0x3C)
    OP_24(0x2F2, 0x3C)
    OP_24(0x137, 0x3C)
    Sleep(300)
    OP_24(0x32E, 0x32)
    OP_24(0x2F2, 0x32)
    OP_24(0x137, 0x32)
    Sleep(300)
    OP_24(0x32E, 0x28)
    OP_24(0x2F2, 0x28)
    OP_24(0x137, 0x28)
    Sleep(300)
    OP_24(0x32E, 0x1E)
    OP_24(0x2F2, 0x1E)
    OP_24(0x137, 0x1E)
    Sleep(300)
    OP_24(0x32E, 0x14)
    OP_24(0x2F2, 0x14)
    OP_24(0x137, 0x14)
    Sleep(300)
    OP_24(0x32E, 0xA)
    OP_24(0x2F2, 0xA)
    OP_24(0x137, 0xA)
    Sleep(300)
    OP_24(0x32E, 0x0)
    OP_24(0x2F2, 0x0)
    OP_24(0x137, 0x0)
    OP_23(0x32E)
    OP_23(0x2F2)
    OP_23(0x137)
    Return()

    # Function_2_213 end

    def Function_3_2C7(): pass

    label("Function_3_2C7")

    EventBegin(0x0)
    Fade(1000)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x4, "map\\mp278_00.eff")
    OP_D2(0x270020, 0x270023, 0x0)
    OP_D2(0x26036B, 0x260370, 0x1)
    OP_D2(0x26036C, 0x260371, 0x1B)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrFlags(0x6, 0x80)
    SetChrFlags(0x7, 0x80)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x1F, -1220, 0, 23600, 0)
    SetChrPos(0x1D, -970, 0, 25400, 0)
    SetChrPos(0x15, 150, 0, 23210, 0)
    SetChrPos(0x21, -100, 0, 21400, 0)
    SetChrPos(0x20, -1480, 0, 21440, 0)
    SetChrChipByIndex(0x22, 19)
    SetChrSubChip(0x22, 0)
    SetChrFlags(0x22, 0x4)
    SetChrPos(0x22, 5500, 800, 32189, 225)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)

    def lambda_456():

        label("loc_456")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_456")

    QueueWorkItem2(0x22, 0, lambda_456)
    PlayEffect(0x0, 0x7, 0x22, 0, 900, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    def lambda_49E():

        label("loc_49E")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_49E")

    QueueWorkItem2(0x22, 3, lambda_49E)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0x40D, 0x0)
    ExitThread()
    OP_72(0x40E, 0x0)
    ExitThread()
    OP_71(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x258)
    OP_71(0x200D, 0x0)
    ExitThread()
    OP_6F(0xD, 0)
    OP_70(0xD, 0x320)
    OP_71(0x200E, 0x0)
    ExitThread()
    OP_6F(0xE, 0)
    OP_70(0xE, 0x12C)
    OP_E5(0x2, 0x1, 0x0, 200)
    OP_E5(0x2, 0x1, 0x1, 100)
    OP_E5(0x2, 0x1, 0x2, 100)
    OP_E5(0x2, 0xA, 0x0, 300)
    OP_E5(0x2, 0xA, 0x1, 300)
    OP_E5(0x2, 0xA, 0x2, 300)
    OP_E5(0x2, 0xA, 0x3, 300)
    OP_E5(0x2, 0xB, 0x0, 300)
    OP_E5(0x2, 0xB, 0x1, 300)
    OP_E5(0x2, 0xB, 0x2, 300)
    OP_E5(0x2, 0xB, 0x3, 300)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x40F, 0x0)
    ExitThread()
    OP_72(0x410, 0x0)
    ExitThread()
    OP_72(0x411, 0x0)
    ExitThread()
    OP_72(0x412, 0x0)
    ExitThread()
    OP_72(0x413, 0x0)
    ExitThread()
    OP_72(0x414, 0x0)
    ExitThread()
    OP_72(0x415, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_72(0x417, 0x0)
    ExitThread()
    OP_72(0x418, 0x0)
    ExitThread()
    OP_72(0x419, 0x0)
    ExitThread()
    OP_72(0x41A, 0x0)
    ExitThread()
    OP_72(0x41B, 0x0)
    ExitThread()
    OP_72(0x41C, 0x0)
    ExitThread()
    OP_72(0x41D, 0x0)
    ExitThread()
    OP_72(0x41E, 0x0)
    ExitThread()
    OP_72(0x41F, 0x0)
    ExitThread()
    OP_72(0x420, 0x0)
    ExitThread()
    OP_72(0x421, 0x0)
    ExitThread()
    OP_72(0x422, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_B0(0xB, 0x32)
    OP_6F(0xB, 600)
    OP_70(0xB, 0x258)
    OP_6D(-170, 0, 22600, 0)
    OP_67(0, 4510, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(148000, 0)
    OP_6E(229, 0)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    def lambda_63D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_63D)
    Sleep(100)

    def lambda_650():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_650)
    Sleep(100)
    OP_8C(0x21, 315, 400)
    Sleep(500)

    ChrTalk(    #0
        0x1D,
        (
            "#1015F#6PYou okay, Renne? You've been kinda quiet\x01",
            "for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x1F,
        (
            "#1307F#11P#40W...Why...?\x02\x03",

            "Why is everyone smiling...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x1D,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x15,
        "#1504F#5PWhat do you mean?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 1)
    SetChrSubChip(0x1F, 0)
    OP_99(0x1F, 0x0, 0x2, 0x4B0)
    Sleep(500)

    ChrTalk(    #4
        0x1F,
        (
            "#1300F#11P#40WI mean...you're all saying goodbye.\x02\x03",

            "For all you know, you might never\x01",
            "get to see each other again...\x02\x03",

            "#268FSo why do you all look so happy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x1D,
        "#1026F#6POh...\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(300)

    ChrTalk(    #6
        0x1F,
        (
            "#266F#11PEveryone keeps saying they're sad to see one\x01",
            "another go... Why don't you all just stay here,\x01",
            "then?\x02\x03",

            "#1301FAs long as the garden's here, everyone can stay\x01",
            "and turn this place into whatever they want it to\x01",
            "be!\x02\x03",

            "We can laugh and have fun tea parties forever\x01",
            "and ever and ever!\x02\x03",

            "#1300FSo why?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(300)
    SetChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 27)
    SetChrSubChip(0x15, 0)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #7
        0x15,
        (
            "#1505F#5P...I get it now.\x02\x03",

            "#1503FIt hurts you to think that you might never see\x01",
            "them again, doesn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x1F, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(400)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)

    ChrTalk(    #8
        0x1F,
        "#1309F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x1D,
        "#1004F#6PJoshua...?\x02",
    )

    CloseMessageWindow()

    def lambda_A94():
        OP_6B(3700, 15000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A94)
    Sleep(500)

    ChrTalk(    #10
        0x15,
        (
            "#1505F#5PIt hurts that no matter how much you care about\x01",
            "someone...\x02\x03",

            "...no matter how much you want to be with them...\x02\x03",

            "...you might never see them again... Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x1D,
        "#1020F#6PWait...\x02",
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #12
        0x1F,
        (
            "#1301F#11PN-No! Of course not!\x02\x03",

            "That's not even possible!\x02\x03",

            "#1303FEven when I heard that Loewe was dead,\x01",
            "that didn't hurt one bit!\x02\x03",

            "I was sad, but it didn't hurt!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #13
        0x15,
        (
            "#1514F#5PThat's because that's not the same.\x02\x03",

            "The reason it didn't hurt is because you were able\x01",
            "to accept Loewe's death.\x02\x03",

            "#1513FYou knew that there was no chance you'd ever be\x01",
            "able to see him again, and that was why you were\x01",
            "able to grieve.\x02\x03",

            "#1503FBut this is a case of knowing that you could meet\x01",
            "the people you care about, but at the same time,\x01",
            "maybe you can't.\x02\x03",

            "In some ways, that's even more painful than never\x01",
            "being able to see someone ever again.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #14
        0x1F,
        "#1309F#11P#40WNo! You're wrong!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x15,
        "#1505F#5PThat's why you...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)

    def lambda_FF4():
        OP_6B(3500, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_FF4)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #16
        0x1F,
        "#1303F#11P#4SYou're wrong! Wrong, wrong, wrong!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_44(0x15, 0x1)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x20C, 0x0, 0x50)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    SetChrSubChip(0x15, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x1D,
        "#1026F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_10D4():
        OP_6D(-170, 0, 22200, 1500)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_10D4)
    OP_8E(0x1D, 0xFFFFFBAA, 0x0, 0x60D6, 0x1F4, 0x0)
    WaitChrThread(0x23, 0x0)
    Fade(250)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1D, 0x800)
    SetChrChipByIndex(0x1D, 27)
    SetChrSubChip(0x1D, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x1D,
        (
            "#1006F#6PShould I tell you, Renne?\x02\x03",

            "Tell you why everyone was able to smile\x01",
            "as they said goodbye to us all.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #19
        0x1F,
        "#1303F#11P#40WI don't want to know! I don't need to know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1D,
        (
            "#1012F#6PWell, too bad. I'm going to tell you anyway.\x02\x03",

            "It's because no matter how much you love\x01",
            "someone or how much you hate someone...\x02\x03",

            "#1025F...eventually, you'll end up having to part from\x01",
            "them. That goes for everyone. No exceptions.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0xFFFFFF9C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x1F, 0x1D, 0x1F, 0x3E8)
    Sleep(300)

    ChrTalk(    #21
        0x1F,
        "#1308F#11P#40W...Everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1D,
        (
            "#1007F#6PYep. Even me and Joshua.\x02\x03",

            "#1003FEven if we get married, have kids, and live\x01",
            "out the rest of our days happily together...\x02\x03",

            "...eventually, one of us is going to die and\x01",
            "leave the other one behind.\x02\x03",

            "#1025FWe can't rule out the possibility that one or \x01",
            "both of us might lose our lives in an accident.\x01",
            "We could even fall out of love someday.\x02\x03",

            "Every day you spend with someone could turn\x01",
            "out to be the last, and that's a reality all\x01",
            "of us have to face up to and fight every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1F,
        "#1307F#11PEvery day...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x15,
        "#1503F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x20,
        "#1935F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x21,
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()
    OP_99(0x1D, 0x11, 0x14, 0x5DC)
    Sleep(500)

    ChrTalk(    #27
        0x1D,
        "#1018F#6PAnd that's why we have to smile!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #28
        0x1F,
        "#1308F#11P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1D,
        (
            "#1001F#6PWhen everyone smiles, we don't have to\x01",
            "worry about the sad stuff, and we can be\x01",
            "positive together!\x02\x03",

            "#1018FWe know we're not alone and that everyone\x01",
            "else feels the same way we do!\x02\x03",

            "And best of all, it fills us with excitement at\x01",
            "the thought of when and how we might see\x01",
            "each other next.\x02\x03",

            "#1012FSo we put on our bravest face and promise to\x01",
            "meet again--whether it comes true of not--and\x01",
            "we go back to our lives and keep on going.\x02\x03",

            "#1006FThat's how it is for everyone, I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #30
        0x1F,
        "#1307F#11PIt's really everyone...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1D,
        (
            "#1012F#6PEveryone.\x02\x03",

            "#1008FYou, too. So...will you try and smile with us?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x1F,
        "#1308F#11P#40WMe...?\x02",
    )

    CloseMessageWindow()
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #33
        0x1D,
        (
            "#1007F#6PMaybe I can't promise we can be together\x01",
            "forever.\x02\x03",

            "#1017F#6PBut I can tell you that we really, really love you.\x02\x03",

            "That's why I want to watch over you, at least\x01",
            "until you become a grownup.\x02\x03",

            "If that's what you want, too, then I'll do what\x01",
            "I can to be by your side no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x1F,
        "#1307F#11P#60WI... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1D,
        (
            "#1012F#6PThen when you grow up, maybe you'll decide you \x01",
            "want to do something with your life that means\x01",
            "we have to part ways.\x02\x03",

            "And if that happens, that's okay.\x02\x03",

            "#1025FBut if it does, then we'll part ways with a big\x01",
            "smile.\x02\x03",

            "#1016FHow does that sound? Good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x1F,
        (
            "#1309F#11P#50W*sniffle*...*sniffle*...\x02\x03",

            "I... Umm...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #37
        0x15,
        (
            "#1513F#5PYou don't need to decide what you want to do now.\x02\x03",

            "#5PThe choice is yours to make. We've already made up\x01",
            "our minds what we want to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(500)

    ChrTalk(    #38
        0x15,
        "#1501F#5PWe want to be your family, Renne.\x02",
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0x1F, 0x1F, 0x22, 0x708)
    Sleep(300)

    ChrTalk(    #39
        0x1F,
        "#1308F#11P#40W...M-My...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x1D,
        (
            "#1016F#6PLike Joshua said, we can't force you. If you don't\x01",
            "wanna be with us, that's fine.\x02\x03",

            "#1008FDad's given his okay. All that's left is yours.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1F, 0x22, 0x26, 0x5DC)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_99(0x1F, 0x2D, 0x33, 0x5DC)

    def lambda_1E81():

        label("loc_1E81")

        OP_99(0xFE, 0x34, 0x37, 0x5DC)
        OP_48()
        Jump("loc_1E81")

    QueueWorkItem2(0x1F, 0, lambda_1E81)
    Sleep(300)

    ChrTalk(    #41
        0x1F,
        "#1309F#11P#40W...*sniffle*...\x02",
    )

    CloseMessageWindow()
    OP_44(0x1F, 0x0)
    OP_99(0x1F, 0x38, 0x41, 0x7D0)
    Sleep(600)
    Fade(250)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(400)

    ChrTalk(    #42
        0x1F,
        "#1303F#11P#4SEnough! Enough!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    def lambda_1F30():
        OP_6D(-1200, 0, 22310, 1000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_1F30)

    def lambda_1F48():
        OP_6B(3930, 1000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1F48)

    def lambda_1F58():
        OP_6C(136000, 1000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1F58)

    def lambda_1F68():
        OP_6E(229, 1000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_1F68)
    OP_43(0x1F, 0x0, 0x1, 0xD)

    def lambda_1F7F():

        label("loc_1F7F")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_1F7F")

    QueueWorkItem2(0x21, 3, lambda_1F7F)

    def lambda_1F90():

        label("loc_1F90")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_1F90")

    QueueWorkItem2(0x20, 3, lambda_1F90)
    WaitChrThread(0x1F, 0x0)
    SetChrPos(0x22, 3500, 800, 29190, 225)
    Fade(250)
    ClearChrFlags(0x1D, 0x2)
    ClearChrFlags(0x1D, 0x800)
    SetChrChipByIndex(0x1D, 16)
    SetChrSubChip(0x1D, 0)

    def lambda_1FD0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_1FD0)
    ClearChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 8)
    SetChrSubChip(0x15, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x23, 0x0)

    ChrTalk(    #43
        0x1D,
        "#1026F#5PRenne...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 1)
    SetChrSubChip(0x1F, 66)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x43), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x1F,
        (
            "#1303F#12PIf that's what you want, then I'm gonna run\x01",
            "and run and run!\x02\x03",

            "I'm gonna run so fast, you'll never be able to\x01",
            "catch me!\x02\x03",

            "So... So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x15,
        (
            "#1513F#5PWe're ready for that.\x02\x03",

            "#1501FYou can keep running for as long as it takes to\x01",
            "make up your mind one way or the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1D,
        (
            "#1029F#5PHeehee. But just so you know, I'm REALLY bad at\x01",
            "knowing when to call it quits.\x02\x03",

            "#1028FYou might be really good at playing hide-and-seek,\x01",
            "but no hiding place can stay undiscovered forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1F,
        "#1309F#12P#40W*hic* I hate you...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)

    def lambda_225D():
        OP_6B(3730, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_225D)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x45), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #48
        0x1F,
        "#1303F#12P#3SI hate you both!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x47), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    Sleep(500)

    ChrTalk(    #49
        0x1F,
        "#1309F#12P#40WBut... But I love you both just as much...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    PlayEffect(0x4, 0x1, 0xFF, 0, 13000, 56500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 18)
    SetChrSubChip(0x1F, 0)
    OP_8C(0x1F, 0, 400)

    def lambda_237A():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_237A)

    def lambda_2392():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2392)

    def lambda_23AA():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_23AA)

    def lambda_23BA():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_23BA)

    def lambda_23CA():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_23CA)
    OP_43(0x1F, 0x0, 0x1, 0xC)

    def lambda_23E1():

        label("loc_23E1")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_23E1")

    QueueWorkItem2(0x1D, 3, lambda_23E1)

    def lambda_23F2():

        label("loc_23F2")

        TurnDirection(0xFE, 0x1F, 400)
        OP_48()
        Jump("loc_23F2")

    QueueWorkItem2(0x15, 3, lambda_23F2)
    Sleep(100)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x1D, 0x3)
    OP_44(0x15, 0x3)
    OP_44(0x22, 0x3)
    SetMessageWindowPos(180, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #50
        (
            "\x07\x00#1016F#40WAhaha...\x02\x03",

            "#1017FWe finally got to tell her...\x02\x03",

            "#1027FWe finally got to tell her how we feel...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(280, 320, -1, -1)
    SetChrName("Joshua...")

    AnonymousTalk(    #51
        "\x07\x00#1514FYeah, we did...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(700, 0, 25540, 0)
    OP_67(0, 4510, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(230, 0)
    OP_D2(0x270001, 0x270005, 0x0)
    OP_D2(0x27003B, 0x270040, 0x1)
    OP_D2(0x26036D, 0x260372, 0x1B)
    SetChrPos(0x1D, -1250, 0, 24410, 0)
    SetChrPos(0x15, -120, 0, 24450, 270)
    SetChrPos(0x21, -700, 0, 21500, 0)
    SetChrPos(0x20, -2180, 0, 21440, 0)

    def lambda_2617():

        label("loc_2617")

        TurnDirection(0xFE, 0x1D, 400)
        OP_48()
        Jump("loc_2617")

    QueueWorkItem2(0x22, 3, lambda_2617)
    SetChrPos(0x22, 3500, 800, 29190, 225)
    OP_0D()
    Sleep(300)
    OP_8C(0x1D, 90, 400)
    SetChrFlags(0x1D, 0x20)

    def lambda_264B():
        OP_6D(1200, 0, 25540, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_264B)

    def lambda_2663():
        OP_8F(0xFE, 0xFFFFFD58, 0x0, 0x5F50, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2663)

    def lambda_267E():
        OP_99(0xFE, 0x4, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_267E)
    WaitChrThread(0x1D, 0x1)
    WaitChrThread(0x1D, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 27)
    SetChrSubChip(0x15, 0)
    SetChrFlags(0x1D, 0x8)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_22(0x8F, 0x0, 0x64)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)
    OP_99(0x15, 0x6, 0x8, 0x3E8)
    OP_99(0x15, 0x6, 0x8, 0x3E8)
    OP_99(0x15, 0x6, 0x8, 0x3E8)
    SetChrSubChip(0x15, 5)
    Sleep(300)

    ChrTalk(    #52
        0x1D,
        (
            "#1027F#6P#60W*sniffle*...*sniffle*...\x02\x03",

            "Joshua... Joshua...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_99(0x15, 0x9, 0xB, 0x4B0)
    Sleep(300)

    ChrTalk(    #53
        0x15,
        "#1513F#11PYou did great, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_99(0x15, 0xC, 0xF, 0x4B0)
    Sleep(300)

    ChrTalk(    #54
        0x15,
        "#1501F#11PStill, the hardest part's still yet to come.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Sleep(300)

    ChrTalk(    #55
        0x1D,
        (
            "#1027F#6P#40WYeah... You're right...\x02\x03",

            "#1007F...*sniffle*...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x15, 0x2)
    SetChrChipByIndex(0x15, 8)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x1D, 0x20)
    ClearChrFlags(0x1D, 0x8)
    SetChrSubChip(0x1D, 0)

    def lambda_28EB():
        OP_8F(0xFE, 0xFFFFFB1E, 0x0, 0x5F5A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_28EB)
    WaitChrThread(0x1D, 0x1)
    Sleep(500)

    def lambda_2910():
        OP_6D(700, 0, 24950, 1000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_2910)
    OP_8C(0x1D, 180, 400)
    OP_8C(0x15, 180, 400)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #56
        0x1D,
        (
            "#1007F#5P#40WSorry for making you wait through that, guys.\x02\x03",

            "#1025FBut now I think it's time we went, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x21,
        (
            "#1840F#12PDon't sweat it. You're gonna get back to chasing\x01",
            "her the second you get out of here, right?\x02\x03",

            "Good luck. Don't give in, and I'm sure it'll work\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x20,
        (
            "#1937F#6PMay the Goddess' blessing be with all three of you.\x02\x03",

            "#1932FI'll be looking forward to the next time we meet.\x02\x03",

            "...And I'll be praying that the three of you will all\x01",
            "be together when that time comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x1D,
        "#1017F#5PWe will! I'll make it happen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x15,
        "#1501F#5PTill next time!\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_2B75():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_2B75)
    Sleep(100)
    OP_8C(0x15, 0, 400)

    def lambda_2B8F():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_2B8F)

    def lambda_2BA7():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2BA7)

    def lambda_2BBF():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2BBF)

    def lambda_2BCF():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_2BCF)

    def lambda_2BDF():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2BDF)
    OP_43(0x1D, 0x0, 0x1, 0xA)
    OP_43(0x15, 0x0, 0x1, 0xB)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x23, 0x0)
    Sleep(2000)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #61
        "\x07\x00#1840F...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #62
        "\x07\x00#1946FThose two really are something special...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #63
        "\x07\x00#1846FYeah... You're tellin' me.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(-800, 0, 28830, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(321000, 0)
    OP_6E(255, 0)
    SetChrPos(0x21, 1450, 0, 24990, 0)
    SetChrPos(0x20, 110, 0, 24940, 0)
    OP_44(0x22, 0x3)
    SetChrPos(0x22, 3500, 800, 29190, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #64
        0x21,
        (
            "#1075F#6PJust looking at those two...\x02\x03",

            "#1840F...I can't help but feel that maybe Rufina's\x01",
            "dream isn't so impossible after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x20,
        (
            "#1937F#6PMe, too...\x02\x03",

            "#1946FWhich means all the more that we'll need to\x01",
            "get to work on making it a reality.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x17, 0x3, 0x1, 0x4)
    OP_22(0x85, 0x1, 0x3C)
    Sleep(1000)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #66
        0x22,
        (
            "\x07\x0C#1615F#11PI'm afraid this place likely doesn't have much\x01",
            "time left.\x02\x03",

            "#1610FI think you should leave before it's too late.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x21,
        "#1078F#6POh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x20,
        "#1934F#6PActually...\x02",
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x21, 270, 400)
    Sleep(300)

    ChrTalk(    #69
        0x21,
        "#1079F#12PHmm? Somethin' wrong?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x20, 90, 400)
    Sleep(300)

    ChrTalk(    #70
        0x20,
        (
            "#1943F#5PI just...can't help but feel like we've forgotten\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x21)
    OP_63(0x20)
    OP_63(0x22)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 390, 0, 9890, 0)

    NpcTalk(    #71
        0x23,
        "Voice",
        "#2PHeeeeeeeeey!\x02",
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_30C7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_30C7)
    Sleep(100)

    def lambda_30DA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_30DA)
    Sleep(100)
    OP_8C(0x22, 180, 400)
    Sleep(300)

    ChrTalk(    #72
        0x21,
        "#1064F#12POh!\x02",
    )


    ChrTalk(    #73
        0x20,
        "#1934F#5POops...\x02",
    )


    ChrTalk(    #74
        0x22,
        "\x07\x0C#1614F#5POh, my...\x07\x00\x02",
    )

    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(400)
    SetChrPos(0x23, 480, 0, -14760, 0)
    Fade(1000)
    OP_6D(70, 0, 120, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(225000, 0)
    OP_6E(331, 0)

    def lambda_3197():
        OP_8E(0xFE, 0x50, 0x0, 0x5B86, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_3197)

    def lambda_31B2():
        OP_6D(-470, 0, 24670, 5000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_31B2)

    def lambda_31CA():
        OP_67(0, 4840, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31CA)

    def lambda_31E2():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_31E2)

    def lambda_31F2():
        OP_6E(310, 5000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_31F2)
    OP_82(0x1, 0x0)
    SetChrPos(0x21, 1430, 0, 25900, 180)
    SetChrPos(0x20, 130, 0, 26110, 180)
    SetChrPos(0x22, 3500, 800, 29190, 180)
    OP_0D()
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x23, 0x0)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #75
        0x23,
        "#1228F#40W#5P*pant*...*pant*...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x23, 45, 600)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x23,
        (
            "#1225F#5PY-You're awful!\x02\x03",

            "Was giving me that halfhearted explanation\x01",
            "and then vanishing the best you could do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x22,
        (
            "\x07\x0C#1613F#6PI-I'm sorry... I did have a lot to do at the time.\x02\x03",

            "#1614FStill, that explanation was enough to allow you\x01",
            "to reach here, wasn't it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x23,
        (
            "#1224F#5PE-Eventually, but I had a heck of a time getting\x01",
            "here! I'm no good with directions!\x02\x03",

            "#1228FI had groups of angels chasing after me... \x01",
            "Chariots trying to run me over...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x23, 0, 400)
    Sleep(300)

    ChrTalk(    #79
        0x23,
        "#1224F#5PA-Anyway! What's with all the shaking?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x21,
        (
            "#1840F#6POh. Right. So apparently, this castle's going\x01",
            "to vanish soon.\x02\x03",

            "That door up there will let you return to our\x01",
            "world, so go ahead and run on through it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x23,
        (
            "#1227F#5PWh-Why are you only telling me this NOW?!\x02\x03",

            "#1225FI'm outta here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x20,
        (
            "#1937F#12PBy all means.\x02\x03",

            "#1932F...Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #83
        0x23,
        "#1224F#5PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x21,
        (
            "#1078F#6PHey, you played an important part in us making it\x01",
            "through all this.\x02\x03",

            "#1075FWhen we get out of here, we'll be enemies again, \x01",
            "but there's no harm in acknowledging that.\x02\x03",

            "#1840FJust don't go causing too much trouble out there\x01",
            "so we have to go after you, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x23,
        (
            "#1221F#5PHa...haha...\x02\x03",

            "#1226FHeh! Worry about yourselves first!\x02\x03",

            "Next time we meet, I'll be a changed man!\x01",
            "Higher ranking and much, MUCH stronger!\x02\x03",

            "#1221FYou mark my words!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x23, 315, 600)
    PlayEffect(0x4, 0x1, 0xFF, 0, 13000, 56500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)

    def lambda_3829():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3829)

    def lambda_3841():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3841)

    def lambda_3859():
        OP_6B(2950, 5000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3859)

    def lambda_3869():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3869)

    def lambda_3879():
        OP_6E(308, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3879)
    OP_43(0x23, 0x0, 0x1, 0x9)

    def lambda_3890():

        label("loc_3890")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_3890")

    QueueWorkItem2(0x21, 3, lambda_3890)

    def lambda_38A1():

        label("loc_38A1")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_38A1")

    QueueWorkItem2(0x20, 3, lambda_38A1)

    def lambda_38B2():

        label("loc_38B2")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_38B2")

    QueueWorkItem2(0x22, 3, lambda_38B2)
    WaitChrThread(0x23, 0x0)
    OP_44(0x21, 0x3)
    OP_44(0x20, 0x3)
    OP_44(0x22, 0x3)
    WaitChrThread(0x11, 0x0)
    Sleep(2000)
    SetMessageWindowPos(300, 320, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #86
        "\x07\x00#1077FHaha...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #87
        "\x07\x00#1946F...Heehee...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    Fade(1000)
    OP_6D(3600, 0, 29100, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(324, 0)
    SetChrPos(0x20, 130, 0, 26110, 0)
    SetChrPos(0x22, 3500, 800, 29050, 0)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_43(0x17, 0x3, 0x1, 0x5)
    OP_22(0x85, 0x1, 0x46)
    Sleep(300)
    OP_22(0x85, 0x1, 0x50)
    Sleep(300)
    OP_22(0x85, 0x1, 0x5A)
    OP_8C(0x22, 225, 400)
    Sleep(300)

    ChrTalk(    #88
        0x22,
        (
            "\x07\x0C#1615F#5PNow please, hurry.\x02\x03",

            "#1612FI doubt this castle has more than a few more\x01",
            "minutes before it disappears.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A4C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3A4C)
    Sleep(100)
    OP_8C(0x20, 45, 400)
    Sleep(300)

    ChrTalk(    #89
        0x21,
        (
            "#1065F#6P...Got it.\x02\x03",

            "#1063FWhat will happen to you after that, by the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x22,
        (
            "\x07\x0C#1616F#5PI imagine I will return to my lengthy slumber in\x01",
            "the garden, in the same state I was before the\x01",
            "Lord of Phantasma first appeared.\x02\x03",

            "...And I will remain that way until this land of\x01",
            "Phantasma eventually finishes disappearing.\x02\x03",

            "#1611FAfter that...I will finally be free from the duty\x01",
            "which keeps me here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x21,
        (
            "#1067F#6PReally...?\x02\x03",

            "#1840FThanks for everything. I don't know if words\x01",
            "can express how grateful we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x20,
        "#1937F#6PMay your dreams be pleasant indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x22,
        (
            "\x07\x0C#1616F#5PHeehee. Thank you very much.\x02\x03",

            "#1610FAfter you've stepped through the gate, I will\x01",
            "disable the Recluse Cube's functionality.\x02\x03",

            "Its power will never return again, so deal with\x01",
            "it however you see fit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x21,
        (
            "#1075F#6PUnderstood.\x02\x03",

            "#1078FI know exactly who's going to be getting it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x20, 90, 400)
    Sleep(300)

    ChrTalk(    #95
        0x20,
        "#1934F#6PYou're thinking of giving it to the professor?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x21, 270, 400)
    Sleep(300)

    ChrTalk(    #96
        0x21,
        (
            "#1068F#11PYou honestly think she'll let all of this slide\x01",
            "if we don't?\x02\x03",

            "Especially after her daughter got caught up\x01",
            "in it. She's gonna be unbearable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x20,
        "#1946F#6P...Good point.\x02",
    )

    CloseMessageWindow()

    def lambda_3ECD():
        OP_6D(2230, 0, 27400, 2000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_3ECD)

    def lambda_3EE5():
        OP_67(0, 4910, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_3EE5)

    def lambda_3EFD():
        OP_6B(2580, 2000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_3EFD)

    def lambda_3F0D():
        OP_6E(318, 2000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_3F0D)
    WaitChrThread(0x23, 0x0)
    Sleep(500)

    ChrTalk(    #98
        0x21,
        "#1078F#11PWell, then, Ries. Time for us to go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x20,
        (
            "#1936F#6PIndeed.\x02\x03",

            "#1938F...Would you like to hold hands?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x21,
        "#1064F#11PWha...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_1D(0xCA)
    OP_24(0x85, 0x50)
    Sleep(200)
    OP_24(0x85, 0x46)
    Sleep(800)

    ChrTalk(    #101 op#A op#5
        0x20,
        (
            "#1937F#6P#16AHeehee. I was only joking, of course.\x02\x03",

            "#1946F#18ABut I do want us to step through together.\x02\x03",

            "#40AJust like how together, we'll make Rufina's\x01",
            "dream come true.\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #102 op#A op#5
        0x21,
        "#1840F#11P#16AHeh. Yeah.\x05\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #103 op#A op#5
        0x21,
        "#1078F#11P#25AI'm counting on you, partner!\x05\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #104 op#A op#5
        0x20,
        "#1932F#6P#16AAlways!\x05\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x21, 0, 400)
    OP_8C(0x20, 0, 400)
    OP_D2(0x270081, 0x270085, 0x0)
    OP_D2(0x2705A7, 0x2705AB, 0x1)

    def lambda_4138():

        label("loc_4138")

        TurnDirection(0xFE, 0x21, 400)
        OP_48()
        Jump("loc_4138")

    QueueWorkItem2(0x22, 3, lambda_4138)
    OP_43(0x21, 0x0, 0x1, 0x7)
    OP_43(0x20, 0x0, 0x1, 0x8)

    def lambda_4157():
        OP_6D(0, 11800, 52460, 5000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_4157)

    def lambda_416F():
        OP_67(0, 2950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_416F)

    def lambda_4187():
        OP_6B(2900, 5000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_4187)

    def lambda_4197():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_4197)

    def lambda_41A7():
        OP_6E(300, 5000)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_41A7)
    WaitChrThread(0x23, 0x0)
    Sleep(1000)

    def lambda_41C1():
        OP_6D(0, 14000, 52460, 8000)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_41C1)

    def lambda_41D9():
        OP_67(0, 2000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_41D9)

    def lambda_41F1():
        OP_6B(4300, 8000)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_41F1)

    def lambda_4201():
        OP_6E(400, 8000)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_4201)
    Sleep(4000)
    FadeToDark(3000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_44(0x23, 0x0)
    OP_44(0x23, 0x1)
    OP_44(0x23, 0x2)
    OP_44(0x23, 0x3)
    OP_44(0x22, 0x0)
    OP_44(0x22, 0x1)
    OP_44(0x22, 0x2)
    OP_44(0x22, 0x3)
    OP_82(0x1, 0x0)
    OP_43(0x23, 0x0, 0x1, 0x6)
    WaitChrThread(0x23, 0x0)
    FadeToBright(2600, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_dt51.dat", 0x0, 0x0)

    label("loc_4289")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42A3")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_42A0")
    Jump("loc_42A3")

    label("loc_42A0")

    Jump("loc_4289")

    label("loc_42A3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2C7 end

    def Function_4_42CD(): pass

    label("Function_4_42CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42EF")
    OP_7C(0x14, 0x14, 0x3E8, 0x384)
    Sleep(1000)
    Jump("Function_4_42CD")

    label("loc_42EF")

    Return()

    # Function_4_42CD end

    def Function_5_42F0(): pass

    label("Function_5_42F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4312")
    OP_7C(0x1E, 0x1E, 0x3E8, 0x384)
    Sleep(1000)
    Jump("Function_5_42F0")

    label("loc_4312")

    Return()

    # Function_5_42F0 end

    def Function_6_4313(): pass

    label("Function_6_4313")

    OP_24(0x85, 0x3C)
    Sleep(340)
    OP_24(0x85, 0x32)
    Sleep(340)
    OP_24(0x85, 0x28)
    Sleep(340)
    OP_24(0x85, 0x1E)
    Sleep(340)
    OP_24(0x85, 0x14)
    Sleep(340)
    OP_24(0x85, 0xA)
    Sleep(340)
    OP_24(0x85, 0x0)
    OP_23(0x85)
    Return()

    # Function_6_4313 end

    def Function_7_4351(): pass

    label("Function_7_4351")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4375():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4375)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_4351 end

    def Function_8_43A0(): pass

    label("Function_8_43A0")

    Sleep(200)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_43C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43C9)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_43A0 end

    def Function_9_43F4(): pass

    label("Function_9_43F4")

    OP_8E(0xFE, 0xFFFFFA92, 0x0, 0x648C, 0x1770, 0x0)
    OP_8E(0xFE, 0x0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4422():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4422)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_43F4 end

    def Function_10_444D(): pass

    label("Function_10_444D")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4471():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4471)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_444D end

    def Function_11_449C(): pass

    label("Function_11_449C")

    Sleep(300)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_44C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44C5)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_449C end

    def Function_12_44F0(): pass

    label("Function_12_44F0")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0x7A3A, 0x1770, 0x0)
    OP_8E(0xFE, 0x0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4528():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4528)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_44F0 end

    def Function_13_4553(): pass

    label("Function_13_4553")

    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x800)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_4572():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4572)

    def lambda_4580():
        OP_96(0xFE, 0xFFFFEF3E, 0x0, 0x5EEC, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4580)
    WaitChrThread(0xFE, 0x2)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_13_4553 end

    def Function_14_45A8(): pass

    label("Function_14_45A8")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_45CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45CC)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_45A8 end

    def Function_15_45F7(): pass

    label("Function_15_45F7")

    OP_8E(0xFE, 0x50A, 0x0, 0x648C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1E, 0x0, 0x74F4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_15_45F7 end

    def Function_16_4627(): pass

    label("Function_16_4627")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_464B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_464B)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_4627 end

    def Function_17_4676(): pass

    label("Function_17_4676")

    Sleep(500)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_469F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_469F)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_4676 end

    def Function_18_46CA(): pass

    label("Function_18_46CA")

    Fade(250)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 2)
    ClearChrFlags(0x12, 0x20)
    OP_22(0x8C, 0x0, 0x64)
    ClearChrFlags(0x17, 0x8)
    SetChrChipByIndex(0x17, 27)

    def lambda_46F3():

        label("loc_46F3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_46F3")

    QueueWorkItem2(0xFE, 1, lambda_46F3)

    def lambda_4706():
        OP_8F(0xFE, 0x1F4, 0xBB8, 0x7454, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_4706)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    WaitChrThread(0x17, 0x2)
    WaitChrThread(0x17, 0x2)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x17, 10)
    OP_97(0x17, 0x0, 0x6D60, 0x3F7A0, 0x1388, 0x1)
    OP_8E(0x17, 0x0, 0x30D4, 0xD73C, 0x1770, 0x0)

    def lambda_476E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_476E)
    OP_22(0x99, 0x0, 0x64)
    OP_8F(0x17, 0x0, 0x30D4, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_46CA end

    def Function_19_4799(): pass

    label("Function_19_4799")

    Sleep(600)
    OP_8F(0xFE, 0x4F6, 0x0, 0x5E38, 0x3E8, 0x0)
    Return()

    # Function_19_4799 end

    def Function_20_47B3(): pass

    label("Function_20_47B3")

    OP_22(0x197, 0x0, 0x64)
    Sleep(800)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 10)
    SetChrPos(0xFE, 2760, 4000, 12950, 0)

    def lambda_47E8():

        label("loc_47E8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_47E8")

    QueueWorkItem2(0xFE, 1, lambda_47E8)
    OP_22(0x8C, 0x0, 0x64)
    OP_8F(0xFE, 0x7D0, 0xBB8, 0x7148, 0x1770, 0x0)
    OP_97(0xFE, 0x1F4, 0x7454, 0xFFF810C0, 0x1B58, 0x1)
    SetChrChipByIndex(0xFE, 27)
    OP_8C(0xFE, 135, 200)

    def lambda_4835():
        OP_8F(0xFE, 0x1F4, 0x12C, 0x7454, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4835)
    Sleep(500)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 2)
    WaitChrThread(0x17, 0x2)
    Fade(250)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x17, 0x8)
    OP_0D()
    Return()

    # Function_20_47B3 end

    def Function_21_4874(): pass

    label("Function_21_4874")

    OP_8E(0xFE, 0x64, 0x0, 0x704E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_21_4874 end

    def Function_22_4890(): pass

    label("Function_22_4890")

    Sleep(400)
    OP_8E(0xFE, 0x3E8, 0x0, 0x70BC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x320, 0x0, 0x74A4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_22_4890 end

    def Function_23_48C5(): pass

    label("Function_23_48C5")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_48E9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48E9)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_48C5 end

    def Function_24_4914(): pass

    label("Function_24_4914")

    Sleep(300)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_493D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_493D)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_4914 end

    def Function_25_4968(): pass

    label("Function_25_4968")

    Sleep(400)
    OP_8E(0xFE, 0xABE, 0x0, 0x65AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2EE, 0x0, 0x75F8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_25_4968 end

    def Function_26_499D(): pass

    label("Function_26_499D")

    OP_8E(0xFE, 0xABE, 0x0, 0x65AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFC68, 0x0, 0x75DA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_26_499D end

    def Function_27_49CD(): pass

    label("Function_27_49CD")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_49F1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_49F1)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_49CD end

    def Function_28_4A1C(): pass

    label("Function_28_4A1C")

    Sleep(300)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4A45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A45)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_4A1C end

    def Function_29_4A70(): pass

    label("Function_29_4A70")

    OP_8E(0xFE, 0x1A4, 0x0, 0x758A, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_29_4A70 end

    def Function_30_4A8C(): pass

    label("Function_30_4A8C")

    Sleep(300)
    OP_8E(0xFE, 0xFFFFFB50, 0x0, 0x7530, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_30_4A8C end

    def Function_31_4AAD(): pass

    label("Function_31_4AAD")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4AD1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AD1)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_4AAD end

    def Function_32_4AFC(): pass

    label("Function_32_4AFC")

    Sleep(500)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4B25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B25)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_4AFC end

    def Function_33_4B50(): pass

    label("Function_33_4B50")

    OP_8E(0xFE, 0xFFFFF2A4, 0x0, 0x6554, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0x7274, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_33_4B50 end

    def Function_34_4B80(): pass

    label("Function_34_4B80")

    Sleep(400)
    OP_8E(0xFE, 0xFFFFF2A4, 0x0, 0x693C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF9DE, 0x0, 0x768E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_34_4B80 end

    def Function_35_4BB5(): pass

    label("Function_35_4BB5")

    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4BD9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4BD9)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFCE0, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_4BB5 end

    def Function_36_4C04(): pass

    label("Function_36_4C04")

    Sleep(200)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x320, 0x2710, 0xD73C, 0x1770, 0x0)

    def lambda_4C2D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4C2D)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x320, 0x2710, 0xE86C, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_4C04 end

    def Function_37_4C58(): pass

    label("Function_37_4C58")

    OP_8E(0xFE, 0xD0C, 0x0, 0x645A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7E4, 0x0, 0x6A9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB64, 0x0, 0x7580, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_37_4C58 end

    def Function_38_4C9C(): pass

    label("Function_38_4C9C")

    Sleep(400)
    OP_8E(0xFE, 0xD0C, 0x0, 0x645A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7E4, 0x0, 0x6A9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14A, 0x0, 0x759E, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_38_4C9C end

    SaveToFile()

Try(main)
