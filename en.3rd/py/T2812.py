from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2812   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2812.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Leo',                                  # 11
        'Dummy',                                # 12
        'Target Camera',                        # 13
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02680 ._CH',             # 02
        'ED6_DT07/CH02393 ._CH',             # 03
        'ED6_DT26/CH20785 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02680P._CP',             # 02
        'ED6_DT07/CH02393P._CP',             # 03
        'ED6_DT26/CH20785P._CP',             # 04
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


    DeclActor(
        TriggerX            = 3000,
        TriggerZ            = 4000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = 3000,
        ActorZ              = 4500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3000,
        TriggerZ            = 4000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -3000,
        ActorZ              = 4500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3000,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = 3000,
        ActorZ              = 500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3000,
        TriggerZ            = 0,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -3000,
        ActorZ              = 500,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_234",          # 01, 1
        "Function_2_285",          # 02, 2
        "Function_3_11B3",         # 03, 3
        "Function_4_11CA",         # 04, 4
        "Function_5_130C",         # 05, 5
        "Function_6_13C7",         # 06, 6
        "Function_7_140B",         # 07, 7
        "Function_8_14A3",         # 08, 8
        "Function_9_153B",         # 09, 9
        "Function_10_160D",        # 0A, 10
        "Function_11_28F1",        # 0B, 11
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_221")
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_233")

    label("loc_221")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_233")

    Return()

    # Function_0_202 end

    def Function_1_234(): pass

    label("Function_1_234")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_284")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_1B(0x0, 0x0, 0x6)

    label("loc_284")

    Return()

    # Function_1_234 end

    def Function_2_285(): pass

    label("Function_2_285")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-87500, -1500, 340, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, -89200, 0, -5000, 90)
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x42B, 0x0)
    ExitThread()

    def lambda_2F1():
        OP_6D(-87500, 2400, 340, 8000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2F1)
    OP_43(0x14, 0x1, 0x0, 0x3)
    FadeToBright(2000, 0)

    def lambda_319():
        OP_8E(0xFE, 0xFFFEB7E0, 0x7D0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_319)
    WaitChrThread(0x105, 0x1)

    def lambda_339():
        OP_8E(0xFE, 0xFFFEB7E0, 0xFA0, 0xFFFFFD30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_339)
    WaitChrThread(0x105, 0x1)

    def lambda_359():
        OP_8E(0xFE, 0xFFFE9454, 0xFA0, 0xFFFFFD30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_359)
    WaitChrThread(0x105, 0x1)
    Sleep(100)
    OP_8C(0x105, 90, 700)
    Sleep(800)
    OP_8C(0x105, 180, 700)
    Sleep(800)
    OP_8C(0x105, 90, 700)
    Sleep(800)
    OP_8C(0x105, 0, 700)
    Sleep(300)
    OP_70(0x4, 0x1E)
    OP_73(0x4)

    def lambda_3B8():
        OP_8E(0xFE, 0xFFFE9454, 0xFA0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-119350, 0, -4310, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x105, 0xFF)
    SetChrPos(0x105, -120860, 0, -9500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, -120460, 0, -9100, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_D7(0x1, 20000, 19)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_467():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_467)

    def lambda_479():
        OP_8E(0xFE, 0xFFFE28C0, 0x0, 0xFFFFE1E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_479)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x105,
        (
            "#044F#12PH-Huh? The lights are already off?\x02\x03",

            "#043FJill must have gone to sleep already.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -120860, 0, -3600, 180)
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x64)
    OP_D7(0x0, 20000, 19)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #1
        0x105,
        "#044F#12P#3SA-Aaah!#2S\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#649F#5P#3S#80WGood eeeeeevening, my dear.#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        (
            "#045F#12PH-Hello...\x02\x03",

            "#542FUmm... What are you standing there for?\x02\x03",

            "Especially with the lights off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#645F#5POh, I was just feeling so lonely without my\x01",
            "beloved Kloe around to keep me company\x01",
            "that I opted to turn the lights off and sulk.\x02\x03",

            "You're never around on our days off lately.\x01",
            "I don't know where you're always going, but \x01",
            "you sure seem to love it there.\x02\x03",

            "#649FWhere've you been, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#540F#12PI'm sorry for being out so late... I didn't mean\x01",
            "to break curfew, but it just happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#648F#5PEh, no big deal. The teachers don't suspect a\x01",
            "thing! I took care of that.\x02\x03",

            "That might not be the case forever if it keeps\x01",
            "happening, though. They might notice at some\x01",
            "point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        (
            "#045F#12PY-Yes... I suppose you're right.\x02\x03",

            "#542FI'll try and make sure to return earlier\x01",
            "in the future.\x02\x03",

            "#540F(Matron Theresa might start getting\x01",
            "annoyed if I keep staying out so late,\x01",
            "too...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_960():
        OP_6D(-119940, 0, -1990, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_960)

    def lambda_978():
        OP_67(0, 4270, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_978)

    def lambda_990():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_990)

    def lambda_9A0():

        label("loc_9A0")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_9A0")

    QueueWorkItem2(0x10, 2, lambda_9A0)

    def lambda_9B1():
        OP_8E(0xFE, 0xFFFE21A4, 0x0, 0xFFFFEA20, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9B1)
    WaitChrThread(0x105, 0x1)

    def lambda_9D1():
        OP_8E(0xFE, 0xFFFE21A4, 0x0, 0xFFFFF1F0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x14, 0x0)

    ChrTalk(    #8
        0x10,
        "#641F#11P...So?\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x105, 0x10, 400)
    Sleep(500)

    ChrTalk(    #9
        0x105,
        "#044F#6P...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#649F#11PYou didn't answer, by the way.\x01",
            "Where HAVE you been going?\x02\x03",

            "#100WI knooow...\x02\x03",

            "#659F#20W#3SIt's a boy, isn't it?#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #11
        0x105,
        (
            "#542F#6PN-No way! It isn't!\x02\x03",

            "#045FI've just been going to...an acquaintance's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#649F#11PAn acquaintance's house, huh? Oho...\x02\x03",

            "And what relationship do you have with this\x01",
            "'acquaintance,' dare I ask?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #13
        0x105,
        (
            "#045F#6PU-Umm...\x02\x03",

            "#048FIt's a place called Mercia Orphanage.\x02\x03",

            "I owe a lot to the matron there, so since\x01",
            "I live in the region now, I've been able to\x01",
            "go visit more often than I could before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#643F#11PAn orphanage?\x02\x03",

            "Oh, hold up! That's the place between here\x01",
            "and Manoria, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x10,
        (
            "#645F#11PAww, phooey... I was hoping it was gonna be\x01",
            "somewhere a little more scandalous.\x02\x03",

            "#648FI should've known with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    Sleep(150)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #16
        0x105,
        "#044F#6P#40W...What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#644F#11PWell, your answer's such a 'good girl' answer.\x01",
            "Spending your days off helping the poor little\x01",
            "orphans and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        "#043F#60W#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #19
        0x10,
        (
            "#641F#11PYou're a true model student, aren't you?\x01",
            "I'm impressed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#049F#60W#6P...P-P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #21
        0x105,
        (
            "#046F#4S#20W#6PPoor little orphans?! Don't you dare call\x01",
            "them that!#2S\x02",
        )
    )

    OP_7C(0x64, 0xDC, 0xBB8, 0x64)

    def lambda_F40():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_F40)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #22
        0x10,
        "#643F#11PWha...?\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB7)
    Sleep(500)

    ChrTalk(    #23
        0x105,
        (
            "#042F#6PWhat right do you have to talk about them\x01",
            "like they're objects of pity?!#2S\x02\x03",

            "And I am not a 'good girl'!#2S\x02",
        )
    )

    CloseMessageWindow()
    Sleep(600)
    OP_8C(0x105, 180, 600)
    Sleep(300)

    ChrTalk(    #24
        0x105,
        "#049F#4S#5PExcuse me!#2S\x02",
    )

    OP_7C(0x0, 0xB4, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1036():
        OP_6D(-118900, 0, -4460, 1500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1036)

    def lambda_104E():
        OP_8E(0xFE, 0xFFFE21A4, 0x0, 0xFFFFE8A4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_104E)
    WaitChrThread(0x105, 0x1)

    def lambda_106E():
        OP_8E(0xFE, 0xFFFE2910, 0x0, 0xFFFFE1D8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_106E)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 700)
    OP_22(0x6, 0x0, 0x64)
    Sleep(200)

    def lambda_109F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_109F)

    def lambda_10B1():
        OP_8E(0xFE, 0xFFFE2910, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_10B1)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_22(0x18B, 0x0, 0x64)
    Sleep(2500)

    ChrTalk(    #25
        0x10,
        (
            "#643F#5P...\x02\x03",

            "I-I didn't think I'd ever see her like that...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #26
        0x10,
        (
            "#1892F#5P#40W...I've done it again, haven't I?\x02\x03",

            "Me and my big mouth...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1191():
        OP_6B(3060, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1191)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_285 end

    def Function_3_11B3(): pass

    label("Function_3_11B3")

    Sleep(1500)
    ClearMapFlags(0x10000000)
    SetPlaceName(0x6D)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_11B3 end

    def Function_4_11CA(): pass

    label("Function_4_11CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-800, 4000, -3280, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13B, 0, -500, -9250, 0)
    OP_9F(0x13B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_123A():
        OP_6D(-800, 0, -3280, 5000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_123A)
    FadeToBright(2000, 0)
    OP_0D()
    ClearMapFlags(0x10000000)
    SetPlaceName(0x6C)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x14, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_127C():
        OP_8E(0xFE, 0x0, 0xFFFFFF06, 0xFFFFE570, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_127C)

    def lambda_1297():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_1297)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x13B, 0x1)
    Sleep(300)
    OP_62(0x13B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #27
        0x13B,
        "#1892F#6P(Maybe I should talk to Hans?)\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_11CA end

    def Function_5_130C(): pass

    label("Function_5_130C")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Call Out\x01",        # 0
            "Do Nothing\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1368")
    Call(0, 10)
    Jump("loc_13C3")

    label("loc_1368")

    OP_62(0x13B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #28
        0x13B,
        (
            "#647F(Should I really do it?)\x02\x03",

            "#1892F(I'm not sure...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C3")

    TalkEnd(0xFF)
    Return()

    # Function_5_130C end

    def Function_6_13C7(): pass

    label("Function_6_13C7")

    EventBegin(0x2)

    ChrTalk(    #29
        0x13B,
        "#1892F(Should I talk to Hans?)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13B, 0, 400)
    OP_90(0x13B, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    EventEnd(0x4)
    Return()

    # Function_6_13C7 end

    def Function_7_140B(): pass

    label("Function_7_140B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1436")

    ChrTalk(    #30
        0x13B,
        "#647FThis isn't Hans' room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_149F")

    label("loc_1436")


    ChrTalk(    #31
        0x13B,
        (
            "#647FThis isn't Hans' room.\x02\x03",

            "#1892FI don't really want to talk to anyone else\x01",
            "right now, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_149F")

    TalkEnd(0xFF)
    Return()

    # Function_7_140B end

    def Function_8_14A3(): pass

    label("Function_8_14A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14CE")

    ChrTalk(    #32
        0x13B,
        "#647FThis isn't Hans' room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1537")

    label("loc_14CE")


    ChrTalk(    #33
        0x13B,
        (
            "#647FThis isn't Hans' room.\x02\x03",

            "#1892FI don't really want to talk to anyone else\x01",
            "right now, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1537")

    TalkEnd(0xFF)
    Return()

    # Function_8_14A3 end

    def Function_9_153B(): pass

    label("Function_9_153B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1597")

    ChrTalk(    #34
        0x13B,
        (
            "#1892FIt's past curfew, so I really don't want \x01",
            "Mr. Effort to know I'm here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1609")

    label("loc_1597")


    ChrTalk(    #35
        0x13B,
        (
            "#1892FIt's past curfew, so I really don't want \x01",
            "Mr. Effort to know I'm here.\x02\x03",

            "I'd get in tons of trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1609")

    TalkEnd(0xFF)
    Return()

    # Function_9_153B end

    def Function_10_160D(): pass

    label("Function_10_160D")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(2330, 4000, 900, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(320000, 0)
    OP_6E(358, 0)
    SetChrPos(0x13B, 3200, 4000, -1000, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 3200, 4000, 1500, 180)
    Sleep(1000)
    OP_62(0x13B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13B)
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x13B,
        "#1890F#6PYou in there, Hans?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#1PY-Yeah. That you, Jill?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#1PHold on. I'll open the door.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_172D():
        OP_8E(0xFE, 0xC1C, 0xFA0, 0x12C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_172D)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #39
        0x11,
        (
            "#733F#11PWhat the heck are you doing here?\x01",
            "It's late.\x02\x03",

            "#732FDid something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x13B,
        "#1892F#6P...Not really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        (
            "#734F#11PYour face tells me that's a big, ol' lie.\x02\x03",

            "#730FCome on in. I'm by myself at the moment,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x13B,
        "#649F#6PDon't try any funny business, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        "#734F#11PAs if I would. Now get your butt inside.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 500)

    def lambda_18A4():
        OP_8E(0xFE, 0xC80, 0xFA0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18A4)
    WaitChrThread(0x11, 0x1)

    def lambda_18C4():
        OP_8E(0xFE, 0xC80, 0xFA0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_18C4)
    WaitChrThread(0x13B, 0x1)
    Fade(1000)
    OP_6D(29860, 0, -5000, 0)
    OP_67(0, 5960, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13B, 30800, 0, -9500, 0)
    SetChrPos(0x11, 30800, 0, -9500, 0)
    OP_9F(0x13B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_195E():
        OP_6D(29860, 0, -1000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_195E)

    def lambda_1976():
        OP_67(0, 4960, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1976)

    def lambda_198E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_198E)

    def lambda_19A0():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19A0)
    Sleep(1000)

    def lambda_19C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_19C0)

    def lambda_19D2():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFF128, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_19D2)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x11, 0x1)

    def lambda_19FC():

        label("loc_19FC")

        TurnDirection(0xFE, 0x13B, 500)
        OP_48()
        Jump("loc_19FC")

    QueueWorkItem2(0x11, 2, lambda_19FC)
    WaitChrThread(0x13B, 0x1)

    def lambda_1A12():
        OP_6D(28440, 0, -1490, 2500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1A12)

    def lambda_1A2A():
        OP_8E(0xFE, 0x7274, 0x0, 0xFFFFF128, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1A2A)
    WaitChrThread(0x13B, 0x1)
    OP_8C(0x13B, 180, 500)
    Sleep(300)
    SetChrFlags(0x13B, 0x4)

    def lambda_1A5B():
        OP_96(0xFE, 0x7274, 0x1CC, 0xFFFFF3A8, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1A5B)
    WaitChrThread(0x13B, 0x1)
    SetChrChipByIndex(0x13B, 3)
    SetChrSubChip(0x13B, 0)
    OP_22(0x8F, 0x0, 0x64)
    WaitChrThread(0x14, 0x0)
    OP_44(0x11, 0x2)
    Sleep(500)

    ChrTalk(    #44
        0x11,
        (
            "#735F#12PSo, what happened?\x02\x03",

            "#730F...Something to do with Kloe, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #45
        0x13B,
        "#645F#11P*sigh* Can't keep anything from you, can I?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x13B, 1)
    Sleep(500)

    ChrTalk(    #46
        0x13B,
        "#1890F#5PHave you ever fought with her before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#735F#12PNot yet, no.\x02\x03",

            "She's the type to just apologize before offering\x01",
            "her opinion on anything, so we've got nothing to\x01",
            "fight about, really.\x02\x03",

            "#732FYou asking because you have?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x13B, 0)
    Sleep(500)

    ChrTalk(    #48
        0x13B,
        (
            "#1892F#11P#40W...Yeah.\x02\x03",

            "...\x02\x03",

            "I really hate myself sometimes, Hans.\x02\x03",

            "I just can't seem to stop myself from blurting\x01",
            "out insensitive stuff even when I don't mean it...\x02\x03",

            "...She was really angry, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#733F#12PAngry? Kloe?!\x02\x03",

            "#735FMan, I can't even imagine that...\x01",
            "I wish I could've seen it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_59()
    Fade(100)
    SetChrSubChip(0x13B, 1)
    Sleep(300)

    ChrTalk(    #50
        0x13B,
        "#1893F#5PCan you be serious, Hans?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#732F#12PI am! I am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x13B,
        (
            "#1892F#5PUgh... I just...\x02\x03",

            "#645FI'm just not sure how to face her now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(500)

    ChrTalk(    #53
        0x13B,
        (
            "#1892F#5PSo I don't wanna go back to my room tonight.\x02\x03",

            "#1890FCan I sleep here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#734F#12PProposal denied. You're sleeping in your\x01",
            "own room, and that's final.\x02\x03",

            "#730FI don't know what you said, but I'm sure\x01",
            "she'll forgive you if you apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x13B,
        "#1892F#5PI dunno...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x13B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13B)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Stay Here\x01",      # 0
            "Go Back\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D7")

    ChrTalk(    #56
        0x13B,
        (
            "#1892F#5P(Even if I do try and apologize, there's every\x01",
            "chance she'll ignore me...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x186, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x13B, 28780, 460, -2560, 180)
    SetChrFlags(0x13B, 0x2)
    SetChrFlags(0x13B, 0x800)
    SetChrChipByIndex(0x13B, 4)
    SetChrSubChip(0x13B, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x13B,
        "#1892F#5P*sigh*\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(300)

    ChrTalk(    #58
        0x11,
        (
            "#735F(It wouldn't be the first time she's lost a\x01",
            "friend over something like this.)\x02\x03",

            "#736F(All delaying going back is going to do is \x01",
            "postpone the inevitable, but I can hardly\x01",
            "blame her for being scared...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0xFFFFFE3E, 1350, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x13B)
    Sleep(1000)

    ChrTalk(    #59
        0x13B,
        "#5PZzz...\x02",
    )

    CloseMessageWindow()
    OP_62(0x13B, 0xFFFFFE3E, 1350, 0x1C, 0x21, 0x12C, 0x0)

    ChrTalk(    #60
        0x11,
        "#733F#12PHow are you already asleep?!\x02",
    )

    CloseMessageWindow()

    def lambda_21DA():
        OP_6D(29860, 0, -3000, 1200)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_21DA)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 30960, 0, -9500, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_2218():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2218)

    def lambda_222A():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFE318, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_222A)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x11, 0x12, 500)

    ChrTalk(    #61
        0x11,
        "#733F#11P...Leo?!\x02",
    )

    CloseMessageWindow()

    def lambda_2272():
        OP_8F(0xFE, 0x79A4, 0x0, 0xFFFFF100, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2272)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #62
        0x11,
        "#731F#11PW-Wow... Y-You're sure back late today!\x02",
    )

    CloseMessageWindow()

    def lambda_22C8():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFEA0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_22C8)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    TurnDirection(0x12, 0x13B, 500)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_8C(0x11, 270, 600)
    Sleep(500)
    OP_8C(0x11, 180, 600)
    OP_63(0x12)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #63
        0x11,
        (
            "#733F#11PUmm... You see, there's a perfectly good\x01",
            "reason why Jill is here...\x02\x03",

            "#731FI tried to say that she should go back to\x01",
            "her own room, but wouldn't you know it!\x01",
            "She wouldn't listen! Then... Then...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 300)
    Sleep(500)

    ChrTalk(    #64
        0x12,
        (
            "#1782F#6PHow this situation arose is of no consequence.\x02\x03",

            "#1780FWe will be sleeping outside tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x11,
        "#734F#11P(I can't even tell if he believed me or not...)\x02",
    )

    CloseMessageWindow()

    def lambda_24BF():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_24BF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_28D2")

    label("loc_24D7")

    OP_59()
    Fade(300)
    SetChrSubChip(0x13B, 0)
    Sleep(500)

    ChrTalk(    #66
        0x13B,
        "#645F#5P*sigh*\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2506():
        OP_96(0xFE, 0x7274, 0x0, 0xFFFFF128, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_2506)
    WaitChrThread(0x13B, 0x1)
    SetChrChipByIndex(0x13B, 65535)
    SetChrSubChip(0x13B, 0)
    ClearChrFlags(0x13B, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #67
        0x13B,
        "#648F#5PAll right. Later gator! ☆\x02",
    )

    CloseMessageWindow()

    def lambda_256A():
        OP_6D(29860, 0, -3000, 1200)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_256A)

    def lambda_2582():

        label("loc_2582")

        TurnDirection(0xFE, 0x13B, 500)
        OP_48()
        Jump("loc_2582")

    QueueWorkItem2(0x11, 2, lambda_2582)

    def lambda_2593():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFF128, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_2593)
    WaitChrThread(0x13B, 0x1)

    def lambda_25B3():
        OP_8E(0xFE, 0x7850, 0x0, 0xFFFFDAE4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_25B3)
    OP_43(0x13B, 0x3, 0x0, 0xB)
    Sleep(600)

    ChrTalk(    #68
        0x11,
        "#733F#11P...Jill?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13B, 0x1)
    WaitChrThread(0x13B, 0x3)
    OP_44(0x11, 0x2)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #69
        0x11,
        (
            "#735F#11P(It wouldn't be the first time she's lost\x01",
            "a friend over something like this.)\x02\x03",

            "#736F(I hope it works out for her...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 30960, 0, -9500, 0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_26CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_26CC)

    def lambda_26DE():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFE318, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_26DE)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x11, 0x12, 500)

    ChrTalk(    #70
        0x11,
        (
            "#733F#11POh, Leo...\x02\x03",

            "#731FY-You're sure back late tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        (
            "#1782F#6PI just walked past Jill, too.\x02\x03",

            "#1780FShe was crying.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #72
        0x11,
        "#733F#11PWell... Umm... That's because...\x02",
    )

    CloseMessageWindow()

    def lambda_27F4():
        OP_8E(0xFE, 0x78F0, 0x0, 0xFFFFEA0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_27F4)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_8C(0x12, 330, 500)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)
    TurnDirection(0x12, 0x11, 400)
    Sleep(300)

    ChrTalk(    #73
        0x12,
        "#1783F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x11,
        (
            "#734F#11P(Stop staring at me with that blank look!\x01",
            "It's scarier than shouting at me!)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28BD():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_28BD)
    FadeToDark(2000, 0, -1)
    OP_0D()

    label("loc_28D2")

    ClearParty()
    AddParty(0x4, 0xEE, 0xFF)
    OP_BB(0x4, 0x1, 0x4)
    OP_BD()
    Sleep(1000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_160D end

    def Function_11_28F1(): pass

    label("Function_11_28F1")

    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)

    def lambda_2901():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_2901)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_11_28F1 end

    SaveToFile()

Try(main)
