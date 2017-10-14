from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4222   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4222.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Libra',                                # 9
        'Ekle',                                 # 10
        'Head Maid Hilda',                      # 11
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
        'ED6_DT06/CH20008 ._CH',             # 00
        'ED6_DT06/CH20107 ._CH',             # 01
        'ED6_DT07/CH00127 ._CH',             # 02
        'ED6_DT07/CH02460 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT06/CH20008P._CP',             # 00
        'ED6_DT06/CH20107P._CP',             # 01
        'ED6_DT07/CH00127P._CP',             # 02
        'ED6_DT07/CH02460P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
    )

    DeclNpc(
        X                   = -138710,
        Z                   = 0,
        Y                   = 7150,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -74270,
        Z                   = 0,
        Y                   = 1530,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_187",          # 01, 1
        "Function_2_1AD",          # 02, 2
        "Function_3_32A",          # 03, 3
        "Function_4_34E",          # 04, 4
        "Function_5_359",          # 05, 5
        "Function_6_601",          # 06, 6
        "Function_7_82B",          # 07, 7
        "Function_8_1271",         # 08, 8
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_14B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_14B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -144740, 0, 7150, 0)

    label("loc_16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A")
    SetChrFlags(0x9, 0x80)

    label("loc_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186")
    Event(0, 7)

    label("loc_186")

    Return()

    # Function_0_13A end

    def Function_1_187(): pass

    label("Function_1_187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A3")
    OP_B1("t4222_y")
    Jump("loc_1AC")

    label("loc_1A3")

    OP_B1("t4222_n")

    label("loc_1AC")

    Return()

    # Function_1_187 end

    def Function_2_1AD(): pass

    label("Function_2_1AD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_314")

    label("loc_1D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_314")

    label("loc_1EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_314")

    label("loc_204")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_314")

    label("loc_21D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_314")

    label("loc_236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_314")

    label("loc_24F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_314")

    label("loc_268")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_314")

    label("loc_281")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_314")

    label("loc_29A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_314")

    label("loc_2B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_314")

    label("loc_2CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_314")

    label("loc_2E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_314")

    label("loc_2FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_314")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_314")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_329")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_314")

    label("loc_329")

    Return()

    # Function_2_1AD end

    def Function_3_32A(): pass

    label("Function_3_32A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34D")
    OP_8D(0xFE, -75980, 4000, -69120, -620, 2000)
    Jump("Function_3_32A")

    label("loc_34D")

    Return()

    # Function_3_32A end

    def Function_4_34E(): pass

    label("Function_4_34E")

    TalkBegin(0xA)
    Call(0, 8)
    TalkEnd(0xA)
    Return()

    # Function_4_34E end

    def Function_5_359(): pass

    label("Function_5_359")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3FC")

    ChrTalk(    #0
        0xFE,
        (
            "I need to finish all my work before\x01",
            "the sun sets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "With orbments no longer working,\x01",
            "everything gets pitch black with the\x01",
            "setting of the sun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4F4")

    ChrTalk(    #2
        0xFE,
        (
            "So the last of the Intelligence\x01",
            "Division have been caught, have they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Justice served in my book.\x01",
            "Those ruffians were nothing\x01",
            "but trouble for all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "We must have them pay for\x01",
            "their crimes, together with\x01",
            "Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5FD")

    ChrTalk(    #5
        0xFE,
        (
            "Castle Blueprints, The Seven Treasures,\x01",
            "the Full Details of the Hundred Days War...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I was asked by Her Highness to\x01",
            "compose a list of the books removed\x01",
            "by the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I wonder what they were investigating.\x01",
            "A curious selection...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FD")

    TalkEnd(0xFE)
    Return()

    # Function_5_359 end

    def Function_6_601(): pass

    label("Function_6_601")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_699")

    ChrTalk(    #8
        0xFE,
        "Duke Dunan is almost like a new man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Lately, he's even gone so far as to\x01",
            "hear petitions from the citizenry in\x01",
            "the audience room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_79D")

    ChrTalk(    #10
        0xFE,
        (
            "I've heard tell that Duke Dunan\x01",
            "was taken as a hostage in last\x01",
            "night's events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "That's what he gets for wandering\x01",
            "out and about so late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "He was even put under house\x01",
            "arrest out at the villa, but I see now\x01",
            "that he hasn't learned a thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827")

    label("loc_79D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_827")

    ChrTalk(    #13
        0xFE,
        (
            "Oh, well. Time to start cleaning\x01",
            "the guest rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Once I'm done with the guest rooms,\x01",
            "it's off to help tidy the library.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827")

    TalkEnd(0xFE)
    Return()

    # Function_6_601 end

    def Function_7_82B(): pass

    label("Function_7_82B")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetMapFlags(0x80)
    SetChrPos(0x103, -79000, 0, 9200, 180)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -29660, 350, 60680, 177)
    OP_69(0x101, 0x0)

    ChrTalk(    #15
        0x101,
        "#007F...Mrrrmrmrr... So...bright...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    Sleep(200)
    SetChrSubChip(0x101, 16)
    Sleep(200)
    SetChrSubChip(0x101, 0)
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    Sleep(1500)

    def lambda_8D4():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D4)

    ChrTalk(    #16 op#5
        0x101,
        "#007F*yaaaaaaaaaawn*\x05\x02",
    )

    OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)

    def lambda_911():
        OP_99(0xFE, 0xC, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_911)
    Sleep(1000)
    SetChrSubChip(0x101, 14)
    Sleep(200)
    SetChrSubChip(0x101, 17)
    Sleep(200)
    SetChrSubChip(0x101, 18)
    Sleep(200)

    ChrTalk(    #17
        0x101,
        (
            "#007FAaaaahhhhh, that felt good.\x01",
            "I haven't slept like that since...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 18)
    Sleep(500)
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 18)
    Sleep(500)
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 18)
    Sleep(400)

    ChrTalk(    #18
        0x101,
        (
            "#004FWha...?\x02\x03",

            "...\x02\x03",

            "#000FOh, right.\x01",
            "We stayed in the castle last night.\x02\x03",

            "#505FJoshua and I were out enjoying the\x01",
            "celebrations, then...we had some\x01",
            "ice cream on the way home...\x02\x03",

            "Then we all went to the dinner party...\x02\x03",

            "And then...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_AD(0x240027, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    OP_AD(0x240028, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    OP_AD(0x240029, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    OP_AD(0x24002A, 0x0, 0x0, 0x96)
    Sleep(3000)
    OP_AE(0xC8)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x101,
        (
            "#580F...\x02\x03",

            "N-N-N-No...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    Fade(500)
    OP_6B(3000, 0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, -31510, 0, 60590, 176)
    OP_6A(0x101)
    OP_0D()
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 180, 1000)
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        (
            "#004FThis is... This is Joshua's room.\x02\x03",

            "#505FBut I was staying in the same room\x01",
            "as Schera.\x02\x03",

            "Was... Was all that a dream?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 1)
    SetChrSubChip(0x101, 5)
    Sleep(1000)

    ChrTalk(    #21
        0x101,
        (
            "#580FWhat...?\x02\x03",

            "...\x02\x03",

            "#005FJOSHUAAAAAA!!!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(500)
    OP_8E(0x101, 0xFFFF76EE, 0x0, 0xBEA0, 0x1B58, 0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6D(-67000, 0, 7200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -67000, 0, 7200, 180)
    SetChrPos(0x103, -79000, 0, 9200, 180)
    OP_0D()
    OP_8E(0x101, 0xFFFEFB24, 0x0, 0xCDA, 0x1388, 0x0)
    OP_8C(0x101, 90, 1000)
    Sleep(1000)
    OP_8C(0x101, 270, 1000)
    Sleep(1000)
    OP_8C(0x101, 90, 1000)
    OP_69(0x103, 0x7D0)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)

    def lambda_D81():

        label("loc_D81")

        OP_69(0x103, 0x0)
        OP_48()
        Jump("loc_D81")

    QueueWorkItem2(0x103, 3, lambda_D81)
    OP_8E(0x103, 0xFFFECDDE, 0x0, 0xBFE, 0x7D0, 0x0)
    TurnDirection(0x103, 0x101, 1000)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8E(0x103, 0xFFFEEA08, 0x0, 0x8DE, 0x7D0, 0x0)
    OP_44(0x103, 0x3)

    ChrTalk(    #22
        0x103,
        (
            "#021FA-ha! Good morning, sleepyhead.\x01",
            "You took your sweet time waking up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 1000)

    ChrTalk(    #23
        0x101,
        "#003FSch-Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        (
            "#025FReally, warn me the next time you\x01",
            "aren't going to come back for the\x01",
            "evening. I was getting a bit worried!\x02\x03",

            "#021FAlthoooough, it looks to me like you\x01",
            "and Joshua managed to talk about\x01",
            "QUITE a bi--\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x103, 0x7D0, 0x1388, 0x0)

    ChrTalk(    #25
        0x101,
        "#005FSchera! Where's Joshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        "#023FWhat? Where's...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#005FI'm looking for Joshua!\x02\x03",

            "Schera, have you seen him?!\x01",
            "This is important!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#023FI...haven't seen him yet this morning,\x01",
            "no.\x02\x03",

            "#020FBut weren't you tired yesterday\x01",
            "and stayed over in his room?\x02\x03",

            "He wasn't there when you woke up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#580FWh-Wha...?!\x02\x03",

            "#005FI-I... What?\x01",
            "Who did you hear that from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#020FUm, from Cassius, but why does that--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#580FFrom Dad?!\x02\x03",

            "#005FO-Okay! Where's Dad, then?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x103,
        (
            "#020FWell, last I saw, he was heading up\x01",
            "toward the Garden Terrace, but now wh--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#002FThe Garden Terrace! Okaythanksbye!\x02",
    )

    CloseMessageWindow()

    def lambda_117F():
        OP_8E(0xFE, 0xFFFF23F6, 0x0, 0x58C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_117F)
    Sleep(500)

    ChrTalk(    #34
        0x103,
        "#024FAh, wait, Estelle! WAIT A...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #35
        0x103,
        "#024FWhat on earth has gotten into her...?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x103, 2)
    OP_99(0x103, 0x0, 0xD, 0x7D0)
    Sleep(1000)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 65535)

    ChrTalk(    #36
        0x103,
        (
            "#022F...\x02\x03",

            "#026FOh. Oh, Goddess.\x01",
            "The 'Lovers.' Reversed...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1002)
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x2, 0xFF)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_82B end

    def Function_8_1271(): pass

    label("Function_8_1271")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, -144700, 0, 5700, 360)
    SetChrPos(0x101, -145560, 0, 5680, 360)
    SetChrPos(0x104, -145320, 0, 4460, 360)
    SetChrPos(0x108, -144920, 0, 3690, 360)
    OP_8C(0xA, 180, 0)
    SetChrSubChip(0xA, 0)
    OP_6D(-144440, 0, 6730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #37
        0xA,
        (
            "#712F#6PPrincess Klaudia!\x01",
            "And Miss Estelle, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x105,
        (
            "#542F#4PHello, Hilda. I'm sorry if I startled you,\x01",
            "but I just got back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1006F#2PEr, hi, Hilda!\x01",
            "Sorry I've been out of touch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "#711F#6PIt's quite all right.\x01",
            "I'm glad to see you well.\x02\x03",

            "I understand the princess has been\x01",
            "assisting you, Estelle.\x02\x03",

            "I'm very glad to see the two of you\x01",
            "home safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1025F#2PAww, Hilda...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#041F#4PHaha. You're embarrassing Estelle, Hilda.\x02\x03",

            "#040FSpeaking of helping Estelle, though,\x01",
            "I've returned partially to inquire about\x01",
            "something the guild is investigating.\x02\x03",

            "Could we ask you a few questions, Hilda?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#713F#6PIf I can be of assistance,\x01",
            "ask me anything.\x02\x03",

            "#711FI think there may be a few too many\x01",
            "onlookers to speak here, however...\x02\x03",

            "Let us borrow a guest room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0xA, -34220, 0, -53190, 270)
    SetChrPos(0x101, -35670, 0, -52660, 90)
    SetChrPos(0x105, -35990, 0, -53890, 90)
    SetChrPos(0x108, -37150, 0, -53340, 90)
    SetChrPos(0x104, -35720, 0, -54910, 45)
    OP_6D(-34480, 0, -52400, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #44
        0xA,
        (
            "#712F#4PYes, I see...\x02\x03",

            "You're attending to the investigation of\x01",
            "that letter we received, then.\x02\x03",

            "#710FI take it you want to know if I have any\x01",
            "idea who the sender might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1002F#6PThat's it exactly.\x02\x03",

            "We're investigating all the locations that\x01",
            "received letters to see if we can ferret\x01",
            "out some clues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "#713F#4PWell, firstly, thank you for your efforts.\x01",
            "Just receiving that letter was...\x01",
            "unsettling.\x02\x03",

            "#715FI'm afraid I can be of little aid in\x01",
            "naming suspects, however.\x02\x03",

            "The only thing I can say with confidence\x01",
            "is that it is not the work of anyone in\x01",
            "this castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1007F#6PYeah, we kinda figured that one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#042FWho was the letter here addressed to,\x01",
            "out of curiosity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#714F#4PNo less a person than Her Majesty herself.\x02\x03",

            "I check all letters addressed to the queen,\x01",
            "so I know the contents of the letter.\x02\x03",

            "#716FBelieve me, if I could lay hands on the\x01",
            "rude fool who wrote that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x108,
        (
            "#070F#5PAh, pardon me.\x02\x03",

            "I was wondering, were there any other suspicious\x01",
            "letters delivered to the castle recently?\x02\x03",

            "Ones critical of royal decisions, for example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        "#712F#4PAh. Well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        (
            "#043FHilda, please, help us for my sake,\x01",
            "if no one else's.\x02\x03",

            "We need as much information as we can\x01",
            "in order to make a judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#713F#4PVery well...\x02\x03",

            "#710FThere have been several letters delivered\x01",
            "with no indication as to their senders.\x02\x03",

            "They were not particularly critical of...\x01",
            "royal decisions, per se.\x02\x03",

            "They were, largely, petitions to reduce\x01",
            "or annul Colonel Richard's sentence.\x02\x03",

            "I suspect at least some are from citizens\x01",
            "of Grancel, but the rest I cannot be\x01",
            "sure on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1004F#6PPeople want Colonel Richard freed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x104,
        (
            "#035FNo less than expected of the man\x01",
            "who once strove to be my rival.\x02\x03",

            "His popularity endures, even after his\x01",
            "capture and shaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x105,
        (
            "#542FThe colonel was very skilled and competent,\x01",
            "and everyone knows that...\x02\x03",

            "It isn't unusual at all to see people regret\x01",
            "'losing' him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x108,
        (
            "#072F#5PI would personally bet on those letters\x01",
            "not being related to our little threat.\x02\x03",

            "#074FRequesting something of the royal hand is one\x01",
            "thing, trying to force it to do something is a\x01",
            "whole different thing all together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1015F#6PWell, still, even knowing the letters\x01",
            "exist helps.\x02\x03",

            "#1004FOh, one more thing, Hilda. \x02\x03",

            "I wanted to ask about something else...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05Estelle asked Hilda about the Hayworths.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #60
        0xA,
        (
            "#712F#4PHarold Hayworth, a trader from Crossbell?\x02\x03",

            "Yes, I remember him.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x101,
        "#1005F#6P#3SSay WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        "#044FIs he an acquaintance of yours, Hilda?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#710F#4PNot as such. He asked for a tour of\x01",
            "the castle interior a few days ago.\x02\x03",

            "I happened to be otherwise unoccupied,\x01",
            "so I showed him about.\x02\x03",

            "His wife and daughter were with him,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1008F#6PReally? Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x104,
        (
            "#035FAlas, this provides us with little clue\x01",
            "as to where the Hayworths may have\x01",
            "gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#713F#4PYes, my apologies.\x01",
            "There was...something that bothered me,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        "#044FWhat would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "#714F#4PTheir child greatly enjoyed the tour.\x01",
            "However...\x02\x03",

            "Her parents felt as though they were barely\x01",
            "even present throughout the entire thing.\x02\x03",

            "They seemed even-tempered and normal enough\x01",
            "when they spoke to me, but when combined with\x01",
            "your story, I wonder if they were under strain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x108,
        (
            "#074F#5PNot able to pay attention after coming to\x01",
            "see a place as a tourist...\x02\x03",

            "#072FSounds like something was on their minds,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        (
            "#043FYes, it seems likely they were in some kind\x01",
            "of trouble, even then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x104,
        (
            "#030FHm. This may give us a clue\x01",
            "as to where they went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1006F#6PThank you very much, Hilda.\x02\x03",

            "I think this gave us some good leads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#711F#4PI'm glad I could be of help.\x02\x03",

            "Oh, Princess.\x02\x03",

            "You'll be staying here in the castle tonight,\x01",
            "I trust? And if your friends lack\x01",
            "accommodations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1004F#6PBuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        (
            "#040FI had intended to stay here while in\x01",
            "Grancel, yes, but...you know.\x02\x03",

            "Well, how about it, everyone?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2708")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as already talked to Imperial ambassador\x01",          # 0
            "Set as not already talked to Imperial ambassador\x01",      # 1
            "No change\x01",                                             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26E7"),
        (1, "loc_26FF"),
        (SWITCH_DEFAULT, "loc_2708"),
    )


    label("loc_26E7")

    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)
    Jump("loc_2708")

    label("loc_26FF")

    OP_A3(0x1621)
    OP_A3(0x1622)
    Jump("loc_2708")

    label("loc_2708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_283A")

    ChrTalk(    #76
        0x104,
        (
            "#031FAh, you forget! They are expecting me to be a\x01",
            "pest at the embassy tonight, and I can hardly\x01",
            "disappoint.\x02\x03",

            "I do appreciate the offer, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x108,
        (
            "#070F#5PYeah, and I've got what's basically a\x01",
            "permanent room at the Calvardian embassy.\x02\x03",

            "Thanks, but I think I've got to decline\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2943")

    label("loc_283A")


    ChrTalk(    #78
        0x104,
        (
            "#031FI believe they will want me to remain at\x01",
            "the Erebonian embassy this eve.\x02\x03",

            "I do appreciate the offer, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x108,
        (
            "#070F#5PYeah, and I've got what's basically a\x01",
            "permanent room at the Calvardian embassy.\x02\x03",

            "Thanks, but I think I've got to decline\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29F0")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Chose Agate as an ally in Ch. 1\x01",           # 0
            "Chose Scherazard as an ally in Ch. 1\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29E4"),
        (1, "loc_29EA"),
        (SWITCH_DEFAULT, "loc_29F0"),
    )


    label("loc_29E4")

    OP_A2(0x1201)
    Jump("loc_29F0")

    label("loc_29EA")

    OP_A3(0x1200)
    Jump("loc_29F0")

    label("loc_29F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A63")

    ChrTalk(    #80
        0x101,
        (
            "#1025F#3PI should probably ask Agate and\x02\x03",

            "Tita before committing to anything. We've got Renne, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2A63")


    ChrTalk(    #81
        0x101,
        (
            "#1025F#3PI should probably ask Schera and\x02\x03",

            "Tita before committing to anything. We've got Renne, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACD")


    ChrTalk(    #82
        0x105,
        (
            "#542FThat's true. It sounds like she\x01",
            "loves the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#713F#4PI shall keep the rooms ready in case\x01",
            "you wish to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1017F#6PThanks, Hilda!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x105,
        "#048FThank you, Hilda...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "#711F#4PNot at all.\x02\x03",

            "I must return to the maid quarters.\x01",
            "Please, let me know if you need\x01",
            "anything else.\x02\x03",

            "If you'll pardon me...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    def lambda_2C1A():
        OP_6D(-34470, 0, -49910, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C1A)

    def lambda_2C32():

        label("loc_2C32")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2C32")

    QueueWorkItem2(0x101, 2, lambda_2C32)

    def lambda_2C43():

        label("loc_2C43")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2C43")

    QueueWorkItem2(0x105, 2, lambda_2C43)

    def lambda_2C54():

        label("loc_2C54")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2C54")

    QueueWorkItem2(0x104, 2, lambda_2C54)

    def lambda_2C65():

        label("loc_2C65")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_2C65")

    QueueWorkItem2(0x108, 2, lambda_2C65)
    OP_8E(0xA, 0xFFFF7748, 0x0, 0xFFFF3990, 0x7D0, 0x0)
    Sleep(200)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    OP_8E(0xA, 0xFFFF770C, 0x0, 0xFFFF4156, 0x7D0, 0x0)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x2)
    OP_44(0x104, 0x2)
    OP_44(0x108, 0x2)
    SetChrFlags(0xA, 0x80)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_71(0x0, 0x800)
    OP_6D(-35580, 0, -52640, 1600)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D97")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talked with the queen\x01",              # 0
            "Haven't talked with the queen\x01",      # 1
            "No change\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D8B"),
        (1, "loc_2D91"),
        (SWITCH_DEFAULT, "loc_2D97"),
    )


    label("loc_2D8B")

    OP_A2(0x1625)
    Jump("loc_2D97")

    label("loc_2D91")

    OP_A3(0x1625)
    Jump("loc_2D97")

    label("loc_2D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E7D")
    OP_8C(0x101, 225, 400)

    def lambda_2DAC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2DAC)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #87
        0x101,
        (
            "#1006F#6POkay, so we still need to meet with\x01",
            "the queen.\x02\x03",

            "She should be in her chambers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x105,
        "#040FYes, I'd be surprised if she isn't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x104,
        "#035FLet us not keep her waiting, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F4C")

    label("loc_2E7D")

    OP_8C(0x101, 225, 400)

    def lambda_2E8A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2E8A)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #90
        0x101,
        (
            "#1006F#6POkay, so we've spoken with Hilda\x01",
            "and the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x108,
        (
            "#070F#1PThat about wraps it up here, I think.\x01",
            "Back out into the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1011F#6PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_28(0x8B, 0x2, 0x80)
    OP_28(0x8B, 0x1, 0x100)

    label("loc_2F4C")

    Sleep(100)
    OP_A2(0x1626)
    OP_28(0x8B, 0x1, 0x800)
    OP_28(0x8A, 0x1, 0x4)
    OP_28(0x8A, 0x1, 0x8)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    Return()

    # Function_8_1271 end

    SaveToFile()

Try(main)
